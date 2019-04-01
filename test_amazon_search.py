import unittest

from selenium import webdriver

from amazon_helper import AmazonHelper


class Test_AmazonSearch(unittest.TestCase):
    def test_can_search_amazon(self):
        driver = webdriver.Chrome()

        amazon_searcher = AmazonHelper(driver)
        links = amazon_searcher.search("python book")

        self.assertIsNotNone(links)

    def test_can_search_amazon_and_get_bestsellers(self):
        driver = webdriver.Chrome()

        amazon_searcher = AmazonHelper(driver)
        items = amazon_searcher.search_and_list_bestsellers("python book")

        print([item.text for item in items])

        self.assertIsNotNone(items)


if __name__ == "__main__":
    unittest.main()
