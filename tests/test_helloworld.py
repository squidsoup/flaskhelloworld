import unittest

import helloworld


class HelloworldTestCase(unittest.TestCase):

    def setUp(self):
        self.app = helloworld.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to flask-hello-world', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
