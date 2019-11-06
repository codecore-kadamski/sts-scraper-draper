import json
import logging
from dynaconf import settings
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import re
from app.tasks import get_menu_soccer_from_betradar
#import chromedriver_binary


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# CHROMEDRIVER_FILE = 'chromedriver78'
# PATH_DRIVER_DOCKER = PATH_DRIVER = '/drivers/'
# if os.path.isdir(PATH_DRIVER_DOCKER) is False:
#     PATH_DRIVER = os.path.dirname(os.path.abspath('../../drivers')) + PATH_DRIVER_DOCKER
#     if os.path.isdir(PATH_DRIVER) is False:
#         raise ValueError("Brak path do chromedriver")
# PATH_DRIVER = f"{PATH_DRIVER}{CHROMEDRIVER_FILE}"

#self.chromedriver = os.path.join(os.path.dirname(os.path.abspath('../../drivers')), 'drivers', 'chromedriver')
#self.chromedriver = os.path.join(os.path.dirname(__file__), 'chromedriver')
#chrome_bin = os.environ.get('CHROMEDRIVER_PATH', None)
#options.binary_location = os.environ.get('CHROMEDRIVER_PATH', None)
#browser = webdriver.Chrome(executable_path='chromedriver78', chrome_options=options)
#  browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)


def get_page(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--no-proxy-server')
    options.add_argument('--start-minimized')
    options.add_argument('--disable-cache')
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(chrome_options=options)
    browser.implicitly_wait(25)
    browser.set_page_load_timeout(10)
    browser.get(url)
    html = browser.page_source
    browser.quit()
    return html


class BetRadarMenuProvider(object):
    menu = {}
    soup = None

    def __init__(self):
        self.parse_menu()

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
        cssclass = elem.find("a").attrs.get('class', False)
        data = {'name': self._parse_name(elem), 'url': self._parse_url(url), 'class': cssclass}
        return data

    def fetch_menu_soccer(self):
        for continent_name in settings.CONTINENTS:
            for part_menu_data in self.menu[continent_name]:
                if part_menu_data is not None:
                    result = get_menu_soccer_from_betradar.delay(part_menu_data)
                    #  result = get_menu_soccer_from_betradar(part_menu_data)
                    print(f'Task result: {result.id}', )

    def parse_menu(self):
        html = get_page(settings.BETRADAR_URL)
        self.soup = BeautifulSoup(html, features="html.parser")
        try:
            soccers = self.soup.find('div', "topmenu").find("ul").find("li", "allsports").find("ul").find("li", settings.SOCCER_SPORT_CLASS)
        except AttributeError:
            raise
        else:
            continents = soccers.find_all("li", "continent")
            for continent in continents:
                self.get_continent(continent)

    def get_continent(self, content):
        data = self._get_elem(content)
        if data.get('name') in settings.CONTINENTS:
            try:
                field_function_name = f"{settings.SOCCER.get(data.get('name'))[0]}"
                field_function = getattr(self, field_function_name, None)
                if field_function and callable(field_function):
                    field_function(content.find("ul"), data, settings.SOCCER.get(data.get('name'))[1])
            except TypeError:
                pass

    def _update_menu(self, continent_obj, country_obj, league_obj):
        """
        league_obj: {'name': 'Tercera Division, Playoffs', 'url': {'seasonid': '66615'}, 'class': False}
        """
        url = f"{settings.BETRADAR_URL}{country_obj.get('url', {}).get('part', '')},5_{league_obj.get('url', {}).get('seasonid', '')}"
        url_continent = f"{settings.BETRADAR_URL}{continent_obj.get('url', {}).get('part', {})}"
        url_country = f"{settings.BETRADAR_URL}{country_obj.get('url', {}).get('part', {})}"
        url_league = f"{settings.BETRADAR_URL}{league_obj.get('url', {}).get('seasonid', {})}"
        self.menu[continent_obj['name']].append({
            'continent': continent_obj['name'],
            'continent_url': url_continent,
            'country': country_obj['name'],
            'country_url': url_country,
            'league': league_obj['name'],
            'league_url': url_league,
            'summary_url': f"{url},9_summary",
            'calendar_url': f"{url},9_fixtures,231_full,23_3",
        })

    def get_leagues(self, continent_obj, country_obj, leagues):
        continent_name = continent_obj['name']
        country_name = country_obj['name']
        for elem in leagues.find_all("li"):
            league_obj = self._get_elem(elem)
            self._update_menu(continent_obj, country_obj, league_obj)

    def get_countries(self, continent_obj, countries):
        continent_name = continent_obj['name']
        for elem in countries.find_all("li"):
            country_obj = self._get_elem(elem)
            if elem.find("ul"):
                self.get_leagues(continent_obj, country_obj, elem.find("ul"))

    def _parse_continent(self, content, continent_obj, selectors):
        continent_name = continent_obj['name']
        self.menu[continent_name] = []
        for elem in content.find_all("li", "floater"):
            data = self._get_elem(elem)
            data_class = data.get('class', [''])
            if data_class and 'arrow_right' in data_class:
                if any(word in data['name'] for word in selectors):
                    self.get_countries(continent_obj, elem.find("ul"))
        # for team in self.menu[continent_name]:
        #     print(team['league'], team['calendar_url'])

    def get_europe(self, content, continent_obj, selectors):
        self._parse_continent(content, continent_obj, selectors)

    def get_america_n(self, content, continent_obj, selectors):
        self._parse_continent(content, continent_obj, selectors)

    def get_america_s(self, content, continent_obj, selectors):
        self._parse_continent(content, continent_obj, selectors)

    def get_africa(self, content, continent_obj, selectors):
        self._parse_continent(content, continent_obj, selectors)

    def get_asia(self, content, continent_obj, selectors):
        self._parse_continent(content, continent_obj, selectors)

    def get_oceania(self, content, continent_obj, selectors):
        self._parse_continent(content, continent_obj, selectors)

    def get_glob(self, content, continent_obj, selectors):
        self._parse_continent(content, continent_obj, selectors)
