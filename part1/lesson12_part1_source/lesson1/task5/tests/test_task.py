import unittest

import requests as requests
from task import username, repository_name


class TestCase(unittest.TestCase):
    def test_requirements_file(self):
        url = f"https://github.com/{username}/{repository_name}"
        resp = requests.get(url=url)
        # здесь лучше чтобы код не равнялся 200, мало ли GitHub изменят код с 404 на другой
        self.assertNotEqual(resp.status_code, 200, msg="Репозиторий не найден")
