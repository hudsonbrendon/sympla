import requests


class Sympla(object):

    _URL = "https://api.sympla.com.br/public/v3/"

    def __init__(self, token):
        self.__token = token

    def _get_url(self, path):
        return f"{self._URL}{self.__token}"

    def _request(self, method, path, json, **kwargs):
        request = requests.request(
            method=method, url=self._get_url(path), json=json, **kwargs,
        )
        json = request.json()
        return json
