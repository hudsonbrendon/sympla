import requests


class Sympla(object):

    _URL = "https://api.sympla.com.br/public/v3/"

    def __init__(self, token):
        self.__token = token

    def _get_url(self, path, id=None):
        if id:
            return f"{self._URL}{path}/{id}"
        return f"{self._URL}{path}"

    @property
    def headers(self):
        return {"S_TOKEN": self.__token}

    def _request(self, method, path, params, id=None, **kwargs):
        request = requests.request(
            method=method,
            url=self._get_url(path, id),
            headers=self.headers,
            params=params,
            **kwargs,
        )
        json = request.json()
        return json

    def events(
        self,
        id=None,
        _from=None,
        published=True,
        page_size=100,
        page=1,
        field_sort=None,
        sort="ASC",
        fields=None,
    ):
        """
        Esta API fornece acesso às informações de eventos criados na plataforma Sympla, exclusivamente aqueles vinculados ao usuário proprietário do token.

        A API também permite a personalização dos resultados, possibilitando filtrar eventos dentro de uma janela de data ou restringir quais campos são relevantes e devem ser exibidos no retorno, como apenas nome do evento e descrição.

        Para saber mais, acesse: https://developers.sympla.com.br/api-doc/index.html#tag/Eventos
        """
        path = "events"

        params = {
            "from": _from,
            "published": published,
            "page_size": page_size,
            "page": page,
            "field_sort": field_sort,
            "sort": sort,
            "fields": fields,
        }

        request = self._request(method="get", path=path, params=params, id=id)
        return request
