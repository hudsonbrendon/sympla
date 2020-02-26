import unittest
import requests_mock

from pysympla import Sympla
from decouple import config


class TestSympla(unittest.TestCase):
    def setUp(self):
        self.sympla = Sympla(token=config("TOKEN"))

    def test_get_url(self):
        self.assertEqual(self.sympla._get_url("test/"), f"{self.sympla._URL}test/")

    def test_get_url_with_id(self):
        self.assertEqual(
            self.sympla._get_url("test/", 12345), f"{self.sympla._URL}test/12345"
        )

    @requests_mock.Mocker()
    def test_events_with_from(self, request_mock):
        url = "https://api.sympla.com.br/public/v3/events?from=2020-01-01&published=True&page_size=100&page=1&sort=ASC"
        json = {
            "data": [],
            "pagination": {
                "has_next": False,
                "has_prev": False,
                "quantity": 0,
                "offset": 0,
                "page": 1,
                "page_size": 100,
                "total_page": 1,
            },
            "sort": {"field_sort": "start_date", "sort": "ASC"},
        }
        request_mock.get(url=url, json=json)

        events = self.sympla.events(_from="2020-01-01")
        self.assertEqual(events, json)


if __name__ == "__main__":
    unittest.main()
