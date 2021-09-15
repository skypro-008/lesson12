import unittest

import requests as requests
from task import username, repository_name


class TestCase(unittest.TestCase):
    def test_requirements_file(self):
        url = f"https://raw.githubusercontent.com/{username}/{repository_name}/main/app.py"
        resp = requests.get(url=url)
        self.assertEqual(resp.status_code, 200, msg="Не найден файл app.py в корне проекта указанного репозитория")
