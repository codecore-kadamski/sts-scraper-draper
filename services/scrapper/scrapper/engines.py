import os
import argparse
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import requests
from bs4 import BeautifulSoup

SOCCER_SPORT_CLASS = 'sport-1'
CONTINENTS = ['Europa', 'Ameryka Płn.', 'Ameryka Płd.', 'Afryka', 'Azja', 'Oceania', 'Świat']
FUNCTIONS = {
    'Europa': ('get_europe', ['A-G', 'H-N', 'P-W'],),
    'Ameryka Płn.': ('get_america_n', [],),
}
MENU = dict



class StsStatisticsScrapper(object):

    def __init__(self, args):
        self.url = args.get("url", None)
        self.directory = os.path.dirname(os.path.realpath(__file__))
        self.chromedriver = os.path.join(os.path.dirname(os.path.abspath('../../drivers')), 'drivers', 'chromedriver')
        if not os.path.exists(self.chromedriver):
            print("brak sterownika dla chrome : chromedriver")
        if not self.url:
            print("brak url")

        options = webdriver.ChromeOptions()
        options.add_argument('--no-proxy-server')
        options.add_argument('--start-maximized')
        options.add_argument('--disable-cache')
        self.browser = webdriver.Chrome(self.chromedriver, options=options)
        self.browser.set_page_load_timeout(10)
        self.browser.get(self.url)
        self.html = self.browser.page_source
        self.browser.quit()
        self.soup = BeautifulSoup(self.html, features="html.parser")

        #self.get_sports()
        self.menu = []
        self.get_menu()

    def get_sports(self):
        elements = self.soup.find('table', "sportselect").find_all("td")
        sports = []
        for elem in elements:
            url = elem.find("a").attrs.get('href', False) if hasattr(elem.find("a"), 'attrs') else False
            name = elem.find("span", "name").text.strip() if hasattr(elem.find("span", "name"), 'text') else False
            if url and name:
                data = {'name': name, 'url': url}
                sports.append(data)
        print(sports)

    def _get_elem(self, elem):
        url = elem.find("a").attrs.get('href', False) if hasattr(elem.find("a"), 'attrs') else False
        name = elem.find("a").getText().strip() if url else False
        cssclass = elem.find("a").attrs.get('class', False)
        data = {'name': name, 'url': url, 'class': cssclass}
        #print(data)
        return data

    def get_europe(self, content):
        for elem in content.find_all("li"):
            if 'arrow_right' in elem.find("a").attrs.get('class'):
                print(elem.find("a").getText())
                # import ipdb; ipdb.set_trace()
                # if elem.find("ul"):
                #     for subelem in elem.find("li"):
                #         pass
                    #if subelem.find("a").getText().strip() in FUNCTIONS['Europa'][1]:
                    #data = self._get_elem(elem)
                    
            # if 'arrow_right' in data.get('class'):
            #     import ipdb; ipdb.set_trace()
            #     if elem.getText().strip() in FUNCTIONS['Europa'][1]:
            #         import ipdb; ipdb.set_trace()


    def get_continents(self, content):
        data = self._get_elem(content)
        if data.get('name') in CONTINENTS:
            try:
                field_function_name = f"{FUNCTIONS.get(data.get('name'))[0]}"
                field_function = getattr(self, field_function_name, None)
                if field_function and callable(field_function):
                    try:
                        field_function(content.find("ul"))
                    except Exception:
                        pass
            except TypeError:
                pass

    def _get_loop(self, content):
        self.get_continents(content)
        if content.find("ul"):
            for elem in content.find_all("li"):
                self._get_loop(elem)
        else:
            self._get_elem(content)

    def get_menu(self):
        topmenu = self.soup.find('div', "topmenu").find("ul")
        for elem in topmenu.find_all("li"):
            if hasattr(elem, 'attrs') and elem.attrs.get('class') and SOCCER_SPORT_CLASS in elem.attrs.get('class'):
                self._get_loop(elem)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test szybkosci otwierania wybranej strony')
    parser.add_argument('--url', help='URL do testowania', required=True)
    args = vars(parser.parse_args())
    test = StsStatisticsScrapper(args)

# if __name__ == '__main__':
#     import ipdb; ipdb.set_trace()