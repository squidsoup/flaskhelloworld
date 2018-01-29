import unittest

from selenium import webdriver


class HelloworldBrowserTestCase(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(options=options)
        self.baseURL = "http://localhost:5000/"

    def tearDown(self):
        self.driver.quit

    def test_button_text(self):
        self.driver.get(self.baseURL)
        button = self.driver.find_element_by_id('clickMe')
        button.click()
        self.assertIn('You clicked the button.',
                      self.driver.find_element_by_id('result').text)


if __name__ == '__main__':
    unittest.main()
