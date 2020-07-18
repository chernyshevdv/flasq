import unittest
from hello import app

class BasicTestCase(unittest.TestCase):
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello world')

    def test_other(self):
        tester = app.test_client(self)
        response = tester.get('/other', content_type='text/html')
        self.assertEqual(response.status_code, 404)
        self.assertTrue(b'does not exist' in response.data)


if __name__ == '__main__':
    unittest.main()