import unittest

import requests as requests
from task import heroku_app_url


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertNotEqual(heroku_app_url, '', msg="Адрес не указан!")
        try:
            heroku_app_url.index('herokuapp.com')
        except ValueError:
            self.assertEqual(True, False, msg="Невалидный адрес Heroku приложения!")
        resp = requests.get(url=heroku_app_url)
        self.assertEqual(resp.status_code, 200, msg="Ваше приложение не доступно по указанному URL!")
