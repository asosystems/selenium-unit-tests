from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from utils import set_text_and_submit


class AmazonHelper():
    search_box_selector = (By.NAME, "field-keywords")
    search_results_selector = (
        By.CSS_SELECTOR, ".s-result-list .s-result-item")

    links_selector = (By.CSS_SELECTOR, "h5 a.a-link-normal.a-text-normal")
    badges_selector = (
        By.CSS_SELECTOR, ".a-badge-text")

    def __init__(self, driver):
        self.driver = driver

    def search(self, query):
        self.driver.get("https://amazon.com")

        search_text_box = self.driver.find_element(*self.search_box_selector)
        set_text_and_submit(search_text_box, query)

        links = self.driver.find_elements(*self.links_selector)

        return links

    def search_and_list_bestsellers(self, query):
        self.driver.get("https://amazon.com")

        search_text_box = self.driver.find_element(*self.search_box_selector)
        set_text_and_submit(search_text_box, query)

        # get search results
        results = self.driver.find_elements(*self.search_results_selector)

        # now filter search results by their badges ("Best Seller")
        best_sellers = []

        for result in results:
            try:
                # if the search result container has a badge, then we add it to the list
                result.find_element(*self.badges_selector)
                best_sellers.append(result)
            except NoSuchElementException:
                pass

        return best_sellers
