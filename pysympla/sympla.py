import requests


class Sympla(object):

    _URL = "https://api.sympla.com.br/public/v3/"

    def __init__(self, token):
        self.__token = token

    def _get_url(self, path, id=None):
        if id:
            return f"{self._URL}{path}{id}"
        return f"{self._URL}{path}"

    @property
    def token(self):
        return self.__token

    def _request(self, method, path, json, id=None, **kwargs):
        request = requests.request(
            method=method, url=self._get_url(path, id), json=json, **kwargs
        )
        json = request.json()
        return json
