import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
#import chromedriver_binary

SOCCER_SPORT_CLASS = 'sport-1'
CONTINENTS = ['Europa', 'Ameryka Płn.', 'Ameryka Płd.', 'Afryka', 'Azja', 'Oceania', 'Świat']
FUNCTIONS = {
    'Europa': ('get_europe', ['A-G', 'H-N', 'P-W'],),
    'Ameryka Płn.': ('get_america_n', [],),
}


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

    def _get_elem(self, elem):
        url = elem.find("a").attrs.get('href', False) if hasattr(elem.find("a"), 'attrs') else False
        name = elem.find("a").getText().strip() if url else False
        cssclass = elem.find("a").attrs.get('class', False)
        data = {'name': name, 'url': url, 'class': cssclass}
        #print(data)
        return data

    def get_menu(self):
        self.get_page("http://stats.betradar.com/s4/?clientid=66")
        self.soup = BeautifulSoup(self.html, features="html.parser")

        soccers = self.soup.find('div', "topmenu").find("ul").find("li", "allsports").find("ul").find("li", SOCCER_SPORT_CLASS)
        continents = soccers.find_all("li", "continent")
        for continent in continents:
            self.get_continent(continent)
        # for elem in allsports:
        #     if hasattr(elem, 'attrs') and elem.attrs.get('class') and SOCCER_SPORT_CLASS in elem.attrs.get('class'):

    def get_continent(self, content):
        data = self._get_elem(content)
        print(data)
        if data.get('name') in CONTINENTS:
            try:
                field_function_name = f"{FUNCTIONS.get(data.get('name'))[0]}"
                field_function = getattr(self, field_function_name, None)
                if field_function and callable(field_function):
                    try:
                        field_function(content.find_all("ul"), data['name'])
                    except Exception:
                        pass
            except TypeError:
                pass


    def get_europe(self, content, continent_name):
        #print(continent_name)
        self.menu[continent_name] = {}
        for elem in content.find_all("li"):
            data = self._get_elem(elem)
            print(data)
            if 'arrow_right' in data['class']:
                self.menu[continent_name] = data
                self.menu[continent_name]['sessionid'] = []
            else:
                self.menu[continent_name]['sessionid'].append(data)
        #print(self.menu)
