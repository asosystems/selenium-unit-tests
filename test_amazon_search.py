import unittest

from selenium import webdriver

from amazon_helper import AmazonHelper


class Test_AmazonSearch(unittest.TestCase):
    def test_can_search_amazon(self):
        driver = webdriver.Chrome()

        amazon_searcher = AmazonHelper(driver)
        links = amazon_searcher.search("python book")

        self.assertIsNotNone(links)


if __name__ == "__main__":
    unittest.main()
