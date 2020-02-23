import unittest
import requests_mock

from pysympla import Sympla
from decouple import config


class TestSympla(unittest.TestCase):
    def setUp(self):
        self.sympla = Sympla(token=config("TOKEN"),)

    def test_get_url(self):
        self.assertEqual(self.sympla._get_url("test/"), f"{self.sympla._URL}test/")


if __name__ == "__main__":
    unittest.main()
