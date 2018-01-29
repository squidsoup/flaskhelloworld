import threading
import time
import unittest

from selenium import webdriver

import helloworld


class HelloworldBrowserTestCase(unittest.TestCase):
    client = None

    @classmethod
    def setUpClass(cls):
        # start Chrome
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        try:
            cls.client = webdriver.Chrome(options=options)
        except:
            pass

        if cls.client:
            cls.app = helloworld.create_app('testing')
            threading.Thread(target=cls.app.run).start()
            time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        if cls.client:
            cls.client.get('http://localhost:5000/shutdown')
            cls.client.close()

    def setUp(self):
        if not self.client:
            self.skipTest('Web browser not available')

    def test_button_text(self):
        self.client.get('http://localhost:5000')
        button = self.client.find_element_by_id('clickMe')
        button.click()
        self.assertIn('You clicked the button.',
                      self.client.find_element_by_id('result').text)


if __name__ == '__main__':
    unittest.main()
