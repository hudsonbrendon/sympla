import unittest
import requests_mock

from pysympla import Sympla
from decouple import config


class TestSympla(unittest.TestCase):
    def setUp(self):
        self.sympla = Sympla(token=config("TOKEN"))

    def test_get_url(self):
        self.assertEqual(self.sympla._get_url("test"), f"{self.sympla._URL}test")

    def test_get_url_with_id(self):
        self.assertEqual(
            self.sympla._get_url("test", 12345), f"{self.sympla._URL}test/12345"
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

    @requests_mock.Mocker()
    def test_events_with_id(self, requests_mock):
        url = "https://api.sympla.com.br/public/v3/events/133207?published=True&page_size=100&page=1&sort=ASC"
        json = {
            "data": {
                "id": 133207,
                "start_date": "2017-04-20 19:00:00",
                "end_date": "2017-04-20 22:00:00",
                "name": "Event Test",
                "detail": '<font color="#555555" face="Open Sans, Arial"><span style="font-size: 13px;">Test</span></font>',
                "private_event": 0,
                "published": 1,
                "cancelled": 0,
                "image": "https://images.sympla.com.br/58e6d1d0b872c.png",
                "address": {
                    "name": "IFRN Natal Central",
                    "address": "Av. Sen. Salgado Filho,",
                    "address_num": "1559",
                    "address_alt": "",
                    "neighborhood": "Tirol",
                    "city": "Natal",
                    "state": "RN",
                    "zip_code": "59015-000",
                    "country": "BRASIL",
                },
                "host": {"name": "Grupy-RN", "description": ""},
                "category_prim": {"name": "encontro-networking"},
                "category_sec": {"name": "None"},
                "url": "https://www.sympla.com.br/event-test__133207",
            }
        }
        requests_mock.get(url=url, json=json)

        event = self.sympla.events(id=133207)


if __name__ == "__main__":
    unittest.main()
