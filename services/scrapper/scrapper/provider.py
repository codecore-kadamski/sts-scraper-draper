import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
#import chromedriver_binary
import re


SOCCER_SPORT_CLASS = 'sport-1'
CONTINENTS = ['Europa', 'Ameryka Płn.', 'Ameryka Płd.', 'Afryka', 'Azja', 'Oceania', 'Świat']
FUNCTIONS = {
    'Europa': ('get_europe', ['A-G', 'H-N', 'P-W'],),
    'Ameryka Płn.': ('get_america_n', [],),
}

CLIENT_ID = 66

BASE_URL = f"http://stats.betradar.com/s4/?clientid={CLIENT_ID}#" # 2_1,3_47,22_1,5_67233,9_summary


class StsProvider(object):
    def __init__(self):
        self.menu = {}

    def get_page(self, url):
        #self.chromedriver = os.path.join(os.path.dirname(os.path.abspath('../../drivers')), 'drivers', 'chromedriver')
        #import ipdb; ipdb.set_trace()
        #self.chromedriver = os.path.join(os.path.dirname(__file__), 'chromedriver')
        options = webdriver.ChromeOptions()
        options.add_argument('--no-proxy-server')
        options.add_argument('--start-minimized')
        options.add_argument('--disable-cache')
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        self.browser = webdriver.Chrome(options=options)
        self.browser.set_page_load_timeout(10)
        self.browser.get(url)
        self.html = self.browser.page_source
        self.browser.quit()
        return self.html

    def _parse_url(self, url):
        if not url:
            return url
        url = re.search(r'\((.*?)\)', url).group(1) if url else False
        if not url:
            return url
        raw_url = url.replace('false', '').replace("'seasonid'", '').replace("'", "").rstrip(',').lstrip(',')
        if 'seasonid' in url:
            return {'seasonid': raw_url}
        elif 'false' in url:
            return {'part': raw_url}
        return {}

    def _parse_name(self, elem):
        if elem.find("a"):
            return elem.find("a").getText().strip()
        elif elem.getText():
            return elem.getText().strip()
        return False

    def _get_elem(self, elem):
        url = elem.find("a").attrs.get('href', False) if hasattr(elem.find("a"), 'attrs') else False
        #name = elem.find("a").getText().strip() if url else elem.getText().strip() if elem.getText() else False
        cssclass = elem.find("a").attrs.get('class', False)
        data = {'name': self._parse_name(elem), 'url': self._parse_url(url), 'class': cssclass}
        #print(data)
        return data

    def get_menu(self):
        self.get_page(BASE_URL)
        self.soup = BeautifulSoup(self.html, features="html.parser")

        soccers = self.soup.find('div', "topmenu").find("ul").find("li", "allsports").find("ul").find("li", SOCCER_SPORT_CLASS)
        continents = soccers.find_all("li", "continent")
        for continent in continents:
            self.get_continent(continent)
        # for elem in allsports:
        #     if hasattr(elem, 'attrs') and elem.attrs.get('class') and SOCCER_SPORT_CLASS in elem.attrs.get('class'):

    def get_continent(self, content):
        data = self._get_elem(content)
        #print(data)
        if data.get('name') in CONTINENTS:
            try:
                field_function_name = f"{FUNCTIONS.get(data.get('name'))[0]}"
                field_function = getattr(self, field_function_name, None)
                if field_function and callable(field_function):
                    field_function(content.find("ul"), data)
            except TypeError:
                pass

    def _update_menu(self, continent_obj, country_obj, league_obj):
        #  self.menu[continent_obj['name']][country_obj['name']].append(league_obj)
        url = f"{BASE_URL}{country_obj.get('url', {}).get('part', '')},5_{league_obj.get('url', {}).get('seasonid', '')}"
        self.menu[continent_obj['name']].append({
            'continent': continent_obj['name'],
            'continent_url': continent_obj['url'],
            'country': country_obj['name'],
            'country_url': country_obj['url'],
            'league': league_obj['name'],
            'league_url': league_obj['url'],
            'summary_url': f"{url},9_summary",
            'calendar_url': f"{url},9_fixtures,231_full,23_3",
        })
        #http://stats.betradar.com/s4/gismo.php?&html=1&id=3675&language=pl&clientid=66&child=3&state=2_1%2C3_257%2C22_1%2C5_66665%2C9_summary&childnodeid=3929&callback=902fa95ac71e1765411ff41ecef02ee07873b463
        #http://stats.betradar.com/s4/gismo.php?&html=1&id=3675&language=pl&clientid=66&child=3&state=2_1,3_257,22_1,5_66665,9_summary&childnodeid=3929&callback=902fa95ac71e1765411ff41ecef02ee07873b463
        #http://stats.betradar.com/s4/gismo.php?&html=1&id=3675&language=pl&clientid=66&child=3&state=2_1,3_257,22_1,5_66665,9_summary&childnodeid=3929

    def get_leagues(self, continent_obj, country_obj, leagues):
        continent_name = continent_obj['name']
        country_name = country_obj['name']
        for elem in leagues.find_all("li"):
            league_obj = self._get_elem(elem)
            #print(continent_name, country_name, league_obj)
            self._update_menu(continent_obj, country_obj, league_obj)

    def get_countries(self, continent_obj, countries):
        continent_name = continent_obj['name']
        for elem in countries.find_all("li"):
            country_obj = self._get_elem(elem)
            if elem.find("ul"):
                self.get_leagues(continent_obj, country_obj, elem.find("ul"))

    def get_europe(self, content, continent_obj):
        continent_name = continent_obj['name']
        self.menu[continent_name] = []
        for elem in content.find_all("li", "floater"):
            data = self._get_elem(elem)
            data_class = data.get('class', [''])
            if data_class and 'arrow_right' in data_class:
                if any(word in data['name'] for word in ["A - G", "H - N", "P - W", "Młodzieżowe"]):
                    self.get_countries(continent_obj, elem.find("ul"))
        for team in self.menu['Europa']:
            print(team['league'], team['calendar_url'])
