from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
from scraper.scraper_page import PageAutomation

class Setup:
    def __init__(self):
        options = Options()
        options.headless = False
        self.driver = webdriver.Chrome(options=options, executable_path=r'/Users/carljavier/Downloads/chromedriver')

    def first_page(self):
        try:
            scraper = PageAutomation(driver=self.driver)
            scraper.login_page_bot()
            scraper.book_list_bot()
        finally:
            self.driver.quit()