from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test= '@web/search/searchButton']")
    def search_product(self, product):
        self.input_text(product, SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6) #wait for search results page to load
