from scrapper import config
from selenium import webdriver


def get_page(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--no-proxy-server")
    options.add_argument("--start-minimized")
    options.add_argument("--disable-cache")
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    browser = webdriver.Chrome(chrome_options=options)
    browser.implicitly_wait(15)
    browser.set_page_load_timeout(10)
    browser.get(url)
    html = browser.page_source
    browser.quit()
    return html


def get_page_chromedriver(url):
    options = webdriver.ChromeOptions()
    options.add_argument("--no-proxy-server")
    options.add_argument("--start-minimized")
    options.add_argument("--disable-cache")
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    browser = webdriver.Remote(command_executor=f"http://{config.get('CHROMEDRIVER_HOST')}:4444", options=options)
    browser.implicitly_wait(15)
    browser.set_page_load_timeout(10)
    browser.get(url)
    html = browser.page_source
    browser.quit()
    return html
