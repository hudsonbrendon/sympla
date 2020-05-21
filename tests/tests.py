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
            self.sympla._get_url("test/12345"), f"{self.sympla._URL}test/12345"
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

        event = self.sympla.events(event_id=133207)
        self.assertEqual(event, json)

    @requests_mock.Mocker()
    def test_event_orders(self, requests_mock):
        url = "https://api.sympla.com.br/public/v3/events/856842/orders"
        json = {
            "data": [
                {
                    "id": "Q080KEE",
                    "event_id": 10203040,
                    "order_date": "2018-10-21 10:12:23",
                    "order_status": "A",
                    "updated_date": "2018-10-10 23:34:21",
                    "discount_code": "10,00% - desconto10",
                    "transaction_type": "CREDIT_CARD",
                    "order_total_sale_price": 23.34,
                    "buyer_first_name": "Joaquim",
                    "buyer_last_name": "Lopes",
                    "buyer_email": "meuemail@sympla.com.br",
                    "invoice_info": {
                        "doc_type": "CPF",
                        "doc_number": "142.536.789-55",
                        "client_name": "Joaquim",
                        "address_zip_code": "31112-000",
                        "address_street": "Rua Fernandes Tourinho",
                        "address_street_number": "147",
                        "address_street2": "10º Andar",
                        "address_neighborhood": "Funcionários",
                        "address_city": "Belo Horizonte",
                        "address_state": "MG",
                        "mei": False
                    }
                }
            ],
            "sort": {
                "field_sort": "id",
                "sort": "ASC"
            },
            "pagination": {
                "has_next": True,
                "has_prev": False,
                "quantity": 10,
                "offset": 1,
                "page": 1,
                "page_size": 100,
                "total_page": 2
            }
        }
        requests_mock.get(url=url, json=json)

        orders = self.sympla.orders_by_event(event_id=856842)
        self.assertEqual(orders, json)

    @requests_mock.Mocker()
    def test_event_order_by_identifier(self, requests_mock):
        url = "https://api.sympla.com.br/public/v3/events/856842/orders/Q080KEE"
        json = {
            "data": {
                "id": "Q080KEE",
                "event_id": 10203040,
                "order_date": "2018-10-21 10:12:23",
                "order_status": "A",
                "updated_date": "2018-10-10 23:34:21",
                "discount_code": "10,00% - desconto10",
                "transaction_type": "CREDIT_CARD",
                "order_total_sale_price": 23.34,
                "buyer_first_name": "Joaquim",
                "buyer_last_name": "Lopes",
                "buyer_email": "meuemail@sympla.com.br",
                "invoice_info": {
                    "doc_type": "CPF",
                    "doc_number": "142.536.789-55",
                    "client_name": "Joaquim",
                    "address_zip_code": "31112-000",
                    "address_street": "Rua Fernandes Tourinho",
                    "address_street_number": "147",
                    "address_street2": "10º Andar",
                    "address_neighborhood": "Funcionários",
                    "address_city": "Belo Horizonte",
                    "address_state": "MG",
                    "mei": False
                }
            }
        }
        requests_mock.get(url=url, json=json)

        order = self.sympla.order_by_identifier(event_id=856842, order_id="Q080KEE")
        self.assertEqual(order, json)

    @requests_mock.Mocker()
    def test_participants_by_order(self, requests_mock):
        url = "https://api.sympla.com.br/public/v3/events/856842/orders/Q080KEE/participants"
        json = {
            "data": [
                {
                    "id": 102345,
                    "order_id": "BC1BA1",
                    "first_name": "Joaquim",
                    "last_name": "Lopes",
                    "email": "meuemail@sympla.com.br",
                    "ticket_number": "QHWA-1Q-3G0J",
                    "ticket_num_qr_code": "QHWA1Q3G0J",
                    "ticket_name": "VIP",
                    "pdv_user": "meuemail@sympla.com.br",
                    "ticket_sale_price": 123.5,
                    "checkin": {
                        "id": 1,
                        "check_in": True,
                        "check_in_date": "2018-09-10T10:21:10-03:00"
                    },
                    "custom_form": {
                        "id": 1,
                        "name": "CPF",
                        "value": "142.536.789-55"
                    }
                }
            ],
            "sort": {
                "field_sort": "id",
                "sort": "ASC"
            },
            "pagination": {
                "has_next": True,
                "has_prev": False,
                "quantity": 10,
                "offset": 1,
                "page": 1,
                "page_size": 100,
                "total_page": 2
            }
        }
        requests_mock.get(url=url, json=json)

        participants = self.sympla.participants_by_order(event_id=856842, order_id="Q080KEE")
        self.assertEqual(participants, json)

    @requests_mock.Mocker()
    def test_populated_affiliates_event(self, request_mock):
        url = "https://api.sympla.com.br/public/v3/events/133207/affiliates"
        json = {
            "data": [
                {
                    "name": "Programa de afiliados",
                    "comission_type": "PERCENTUAL",
                    "comission_value": 20.5,
                    "has_limit": True,
                    "limit": 100,
                    "affiliates": [
                        {
                            "email": "email@email.com.br",
                            "discount_code": "AFILIADO1",
                            "sold_tickets": 50,
                            "sales": 500,
                        }
                    ],
                }
            ]
        }

        request_mock.get(url=url, json=json)

        affiliates = self.sympla.affiliates(133207)
        self.assertEqual(affiliates, json)

    @requests_mock.Mocker()
    def test_empty_affiliates_event(self, request_mock):
        url = "https://api.sympla.com.br/public/v3/events/133207/affiliates"
        json = {"error": True, "message": "Event dont have affiliate program."}

        request_mock.get(url=url, json=json)

        affiliates = self.sympla.affiliates(133207)
        self.assertEqual(affiliates, json)

    @requests_mock.Mocker()
    def test_unauthorized_affiliates_event(self, request_mock):
        url = "https://api.sympla.com.br/public/v3/events/555555/affiliates"
        json = {
            "error": True,
            "code": 10,
            "message": "Token is not authorized access this event.",
        }

        request_mock.get(url=url, json=json)

        affiliates = self.sympla.affiliates(555555)
        self.assertEqual(affiliates, json)


if __name__ == "__main__":
    unittest.main()
