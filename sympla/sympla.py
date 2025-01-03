import requests

from sympla.enums import Ordering


class Sympla:

    __URL = "https://api.sympla.com.br/public/v3/"

    def __init__(self, token) -> None:
        self.__token = token

    @property
    def url(self) -> str:
        return self.__URL

    @property
    def token(self) -> str:
        return self.__token

    def full_url(self, path: str) -> str:
        return f"{self.url}{path}"

    @property
    def headers(self) -> dict:
        return {"S_TOKEN": self.token}

    def _request(
        self, method: str, path: str, params: dict = None, **kwargs
    ) -> dict:
        request = requests.request(
            method=method,
            url=self.full_url(path),
            headers=self.headers,
            params=params,
            **kwargs,
        )
        json = request.json()
        return json

    def events(
        self,
        event_id: int = None,
        _from: str = None,
        published: bool = True,
        page_size: int = 100,
        page: int = 1,
        field_sort: str = None,
        sort: Ordering = Ordering.ASC.value,
        fields: str = None,
    ) -> dict:
        """
        Esta API fornece acesso às informações de eventos criados na plataforma Sympla, exclusivamente aqueles vinculados ao usuário proprietário do token.

        A API também permite a personalização dos resultados, possibilitando filtrar eventos dentro de uma janela de data ou restringir quais campos são relevantes e devem ser exibidos no retorno, como apenas nome do evento e descrição.

        Para saber mais, acesse: https://developers.sympla.com.br/api-doc/index.html#tag/Eventos
        """
        if sort not in Ordering._value2member_map_:
            raise ValueError(
                f"O valor de 'sort' deve ser 'ASC' ou 'DESC', não '{sort}'"
            )

        path = "events"
        if event_id is not None:
            path = f"events/{event_id}"

        params = {
            "from": _from,
            "published": published,
            "page_size": page_size,
            "page": page,
            "field_sort": field_sort,
            "sort": sort,
            "fields": fields,
        }

        request = self._request(method="get", path=path, params=params)
        return request

    def orders_by_event(
        self,
        event_id: int,
        status: bool = False,
        page_size: int = 100,
        page: int = 1,
        field_sort: str = None,
        sort: Ordering = Ordering.ASC.value,
        fields: str = None,
    ) -> dict:
        """
        Retorna os pedidos de um determinado evento.

        Para saber mais, acesse: https://developers.sympla.com.br/api-doc/index.html#operation/getListOrders

        :param event_id: Identificador único do evento

        :param status: Retorna todos os pedidos com qualquer status.
                        True: Retorna os pedidos de todos os status;
                        False: Retorna apenas os pedidos com status "A".

        :param page_size: Especifica quantos registros por página o usuário deseja. Mínimo 1 e maxímo 200.
        :param page: Número da página dos resultados.
        :param field_sort: Permite que os resultados sejam ordenados.
        :param sort: Ordena por 'ASC' ou 'DESC'
        :param fields: Deve ser utilizado para retornar apenas os atributos indicados do objeto.
                        Os atributos indicados devem ser separados por ",".
        """
        if sort not in Ordering._value2member_map_:
            raise ValueError(
                f"O valor de 'sort' deve ser 'ASC' ou 'DESC', não '{sort}'"
            )

        path: str = f"events/{event_id}/orders"

        params = {
            "status": status,
            "page_size": page_size,
            "page": page,
            "field_sort": field_sort,
            "sort": sort,
            "fields": fields,
        }

        request = self._request(method="get", path=path, params=params)

        return request

    def order_by_identifier(
        self, event_id: int, order_id: str, fields: str = None
    ) -> dict:
        """
        Retorna o pedido correspondente ao identificador informado.

        Para saber mais, acesse: https://developers.sympla.com.br/api-doc/index.html#operation/getOneOrder

        :param event_id: Identificador único do evento
        :param order_id: id do pedido

        :param fields: Deve ser utilizado para retornar apenas os atributos indicados do objeto.
                        Os atributos indicados devem ser separados por ",".
        """

        path: str = f"events/{event_id}/orders/{order_id}"

        params = {"fields": fields}

        request = self._request(method="get", path=path, params=params)

        return request

    def participants_by_order(
        self,
        event_id: int,
        order_id: str,
        page_size: int = 100,
        page: int = 1,
        field_sort: str = None,
        sort: Ordering = Ordering.ASC.value,
        fields: str = None,
    ) -> dict:
        """
        Retorna o(s) participante(s) contido(s) em um determinado pedido.

        Para saber mais, acesse: https://developers.sympla.com.br/api-doc/index.html#operation/getAllParticipantsForOrder

        :param event_id: Identificador único do evento
        :param order_id: Identificador único do pedido

        :param page_size: Especifica quantos registros por página o usuário deseja. Mínimo 1 e maxímo 200.
        :param page: Número da página dos resultados.
        :param field_sort: Permite que os resultados sejam ordenados.
        :param sort: Ordena por 'ASC' ou 'DESC'
        :param fields: Deve ser utilizado para retornar apenas os atributos indicados do objeto.
                        Os atributos indicados devem ser separados por ",".
        """
        if sort not in Ordering._value2member_map_:
            raise ValueError(
                f"O valor de 'sort' deve ser 'ASC' ou 'DESC', não '{sort}'"
            )

        path: str = f"events/{event_id}/orders/{order_id}/participants"

        params = {
            "page_size": page_size,
            "page": page,
            "field_sort": field_sort,
            "sort": sort,
            "fields": fields,
        }

        request = self._request(method="get", path=path, params=params)

        return request

    def participants_by_event(
        self,
        event_id: int,
        ticket_number: str = None,
        page_size: int = 100,
        page: int = 1,
        field_sort: str = None,
        sort: Ordering = Ordering.ASC.value,
        fields: str = None,
    ) -> dict:
        """
        Retorna os participantes de um determinado evento.

        Para saber mais, acesse: https://developers.sympla.com.br/api-doc/index.html#operation/getAllParticipants

        :param event_id: Identificador único do evento

        :param ticket_number: Código escrito no ingresso.
        :param page_size: Especifica quantos registros por página o usuário deseja. Mínimo 1 e maxímo 200.
        :param page: Número da página dos resultados.
        :param field_sort: Permite que os resultados sejam ordenados.
        :param sort: Ordena por 'ASC' ou 'DESC'
        :param fields: Deve ser utilizado para retornar apenas os atributos indicados do objeto.
                        Os atributos indicados devem ser separados por ",".
        """
        if sort not in Ordering._value2member_map_:
            raise ValueError(
                f"O valor de 'sort' deve ser 'ASC' ou 'DESC', não '{sort}'"
            )

        path: str = f"events/{event_id}/participants"

        params = {
            "ticket_number": ticket_number,
            "page_size": page_size,
            "page": page,
            "field_sort": field_sort,
            "sort": sort,
            "fields": fields,
        }

        request = self._request(method="get", path=path, params=params)

        return request

    def participant_by_ticket_id(
        self, event_id: int, participant_id: int, fields: str = None
    ) -> dict:
        """
        Retorna o participante correspondente ao ingresso informado.

        Para saber mais, acesse: https://developers.sympla.com.br/api-doc/index.html#operation/getOneParticipant

        :param event_id: Identificador único do evento
        :param participant_id: Identificador único do ingresso

        :param fields: Deve ser utilizado para retornar apenas os atributos indicados do objeto.
                        Os atributos indicados devem ser separados por ",".
        """

        path: str = f"events/{event_id}/participants/{participant_id}"

        params = {"fields": fields}

        request = self._request(method="get", path=path, params=params)

        return request

    def participant_by_ticket_number(
        self, event_id: int, ticket_number: str, fields: str = None
    ) -> dict:
        """
        Retorna o participante correspondente ao ingresso informado.

        Para saber mais, acesse: https://developers.sympla.com.br/api-doc/index.html#operation/getOneParticipantByTicketNumber

        :param event_id: Identificador único do evento
        :param ticket_number: Número do ingresso

        :param fields: Deve ser utilizado para retornar apenas os atributos indicados do objeto.
                        Os atributos indicados devem ser separados por ",".
        """

        path: str = (
            f"events/{event_id}/participants/ticketNumber/{ticket_number}"
        )

        params = {"fields": fields}

        request = self._request(method="get", path=path, params=params)

        return request

    def checkin_by_ticket_id(self, event_id: int, participant_id: int) -> dict:
        """
        Realiza o check-in de um participante por id do ingresso.

        Para saber mais, acesse: https://developers.sympla.com.br/api-doc/index.html#operation/checkInByParticipantId

        :param event_id: Identificador único do evento
        :param participant_id: Identificador único do ingresso
        """

        path: str = f"events/{event_id}/participants/{participant_id}/checkIn"

        request = self._request(method="post", path=path)

        return request

    def checkin_by_ticket_number(
        self, event_id: int, ticket_number: str
    ) -> dict:
        """
        Realiza o check-in de um participante por número do ingresso.

        Para saber mais, acesse: https://developers.sympla.com.br/api-doc/index.html#operation/checkInByTicketNumber

        :param event_id: Identificador único do evento
        :param ticket_number: Número do ingresso
        """

        path: str = f"events/{event_id}/participants/ticketNumber/{ticket_number}/checkIn"

        request = self._request(method="post", path=path)

        return request

    def affiliates(self, event_id: int) -> dict:
        """
        Esta API fornece acesso às informações relativas ao programa de afiliados e seus respectivos afiliados.

        Para saber mais, acesse: https://developers.sympla.com.br/api-doc/index.html#tag/Afiliados

        :param event_id: Identificador único do evento
        """

        path: str = f"events/{event_id}/affiliates"
        request = self._request(method="get", path=path)

        return request
