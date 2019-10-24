import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
#import chromedriver_binary


class StsProvider(object):
    def __init__(self):
        self.menu = []
        self.get_menu()

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

    def get_menu(self):
        self.get_page("http://stats.betradar.com/s4/?clientid=66")
        self.soup = BeautifulSoup(self.html, features="html.parser")

        allsports = self.soup.find('div', "topmenu").find("ul").find("li", "allsports").find("ul").find_all("li")
        print(allsports)
