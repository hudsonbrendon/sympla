import unittest
import requests_mock

from pysympla import Sympla
from decouple import config


class TestSympla(unittest.TestCase):
    def setUp(self):
        self.sympla = Sympla(token=config("TOKEN"),)

    def test_get_url(self):
        self.assertEqual(self.sympla._get_url("test/"), f"{self.sympla._URL}test/")

    def test_get_url_with_id(self):
        self.assertEqual(
            self.sympla._get_url("test/", 12345), f"{self.sympla._URL}test/12345"
        )


if __name__ == "__main__":
    unittest.main()
