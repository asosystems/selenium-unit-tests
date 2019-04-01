from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from utils import set_text_and_submit


class AmazonHelper():
    search_box_selector = (By.NAME, "field-keywords")
    links_selector = (By.CSS_SELECTOR, "h5 a.a-link-normal.a-text-normal")

    def __init__(self, driver):
        self.driver = driver

    def search(self, query):
        self.driver.get("https://amazon.com")

        search_text_box = self.driver.find_element(*self.search_box_selector)
        set_text_and_submit(search_text_box, query)

        links = self.driver.find_elements(*self.links_selector)

        return links
