# Sympla
A plataforma online de eventos líder no Brasil. Venda de ingressos, promoção e administração de eventos. Simples e segura. Organiza eventos? Sympla!

[![Python package](https://github.com/hudsonbrendon/sympla/actions/workflows/pythonpackage.yml/badge.svg)](https://github.com/hudsonbrendon/sympla/actions/workflows/pythonpackage.yml)
[![Upload Python Package](https://github.com/hudsonbrendon/sympla/actions/workflows/python-publish.yml/badge.svg)](https://github.com/hudsonbrendon/sympla/actions/workflows/python-publish.yml)
[![Github Issues](http://img.shields.io/github/issues/hudsonbrendon/sympla.svg?style=flat)](https://github.com/hudsonbrendon/sympla/issues?sort=updated&state=open)
![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)

![Sympla](https://logodownload.org/wp-content/uploads/2018/10/sympla-logo-3.png)

# Recursos Disponíveis

- [x]  Listar eventos
- [x]  Listar evento por identificador
- [x]  Listar pedidos por evento
- [x]  Listar pedidos por identificador
- [x]  Listar participantes por pedido
- [x]  Listar participantes por evento
- [x]  Listar participante por id do ingresso
- [x]  Listar participante por número de ingresso
- [x]  Check-in por id do ingresso
- [x]  Check-in por número do ingresso
- [x]  Listar afiliados por evento

# Instalação

```bash
$ pip install sympla
```
# Modo de usar

A API da Sympla é a interface pública de acesso a dados da plataforma Sympla. Através dela é possível obter informações relacionadas aos eventos criados por você, como ingressos, pedidos e participantes.

A API fornece endpoints com resultados representados em formato JSON, e os dados são disponibilizados em conformidade com o princípio REST de maneira segura, eficiente e de fácil integração. Para garantir a segurança de acesso somente a dados relacionados aos seus eventos, a API exige autenticação prévia.

Neste documento você encontrará a referência técnica de como acessar todos os serviços disponíveis da API.
Saiba mais em: https://developers.sympla.com.br/api-doc/index.html#section/Introducao

# Autenticação

Para executar requisições válidas à Sympla API é necessário uma chave de acesso (token) associada ao seu usuário na plataforma. Este token deverá assinar todas as requisições enviadas à API.

Para gerar a chave de acesso é preciso logar na plataforma Sympla, acessar o menu "Minha Conta" (a partir do nome do seu usuário) e navegar até a aba "Integrações".

Saiba mais em: https://developers.sympla.com.br/api-doc/index.html#section/Autenticacao

# Listar eventos

Esta API fornece acesso às informações de eventos criados na plataforma Sympla, exclusivamente aqueles vinculados ao usuário proprietário do token.

A API também permite a personalização dos resultados, possibilitando filtrar eventos dentro de uma janela de data ou restringir quais campos são relevantes e devem ser exibidos no retorno, como apenas nome do evento e descrição.

Saiba mais em: https://developers.sympla.com.br/api-doc/index.html#tag/Eventos

```python
from sympla import Sympla
from decouple import config


sympla = Sympla(token=config("TOKEN"))

events = sympla.events()
```

# Listar eventos por identificador

Retorna o evento correspondente ao identificador informado.

Saiba mais em: https://developers.sympla.com.br/api-doc/index.html#operation/getEventId

```python
from sympla import Sympla
from decouple import config


sympla = Sympla(token=config("TOKEN"))

event = sympla.events(event_id=config("EVENT_ID"))
```

# Listar pedidos por evento

Retorna os pedidos de um determinado evento.

Saiba mais em: https://developers.sympla.com.br/api-doc/index.html#operation/getListOrders

```python
from sympla import Sympla
from decouple import config


sympla = Sympla(token=config("TOKEN"))

orders = sympla.orders_by_event(event_id=config("EVENT_ID"))
```

# Listar pedido por identificador

Retorna o pedido correspondente ao identificador informado.

Saiba mais em: https://developers.sympla.com.br/api-doc/index.html#operation/getOneOrder

```python
from sympla import Sympla
from decouple import config


sympla = Sympla(token=config("TOKEN"))

order = sympla.order_by_identifier(event_id=config("EVENT_ID"), order_id=config("ORDER_ID"))
```

# Listar participantes por pedido

Retorna o(s) participante(s) contido(s) em um determinado pedido.

Saiba mais em: https://developers.sympla.com.br/api-doc/index.html#operation/getAllParticipantsForOrder

```python
from sympla import Sympla
from decouple import config


sympla = Sympla(token=config("TOKEN"))

participants = sympla.participants_by_order(event_id=config("EVENT_ID"), order_id=config("ORDER_ID"))
```

# Listar participantes por evento

Retorna os participantes de um determinado evento.

Saiba mais em: https://developers.sympla.com.br/api-doc/index.html#tag/Participantes

```python
from sympla import Sympla
from decouple import config


sympla = Sympla(token=config("TOKEN"))

participants = sympla.participants_by_event(event_id=config("EVENT_ID"))
```

# Listar participante por id do ingresso

Retorna o participante correspondente ao ingresso informado.

Saiba mais em: https://developers.sympla.com.br/api-doc/index.html#operation/getOneParticipant

```python
from sympla import Sympla
from decouple import config


sympla = Sympla(token=config("TOKEN"))

participants = sympla.participant_by_ticket_id(event_id=config("EVENT_ID"), participant_id=config("PARTICIPANT_ID"))
```

# Listar participante por número de ingresso

Retorna o participante correspondente ao ingresso informado.

Saiba mais em: https://developers.sympla.com.br/api-doc/index.html#operation/getOneParticipantByTicketNumber

```python
from sympla import Sympla
from decouple import config


sympla = Sympla(token=config("TOKEN"))

participants = sympla.participant_by_ticket_number(event_id=config("EVENT_ID"), ticket_number=config("TICKET_NUMBER"))
```

# Check-in por id do ingresso

Realiza o check-in de um participante por id do ingresso.

Saiba mais em: https://developers.sympla.com.br/api-doc/index.html#operation/checkInByParticipantId

```python
from sympla import Sympla
from decouple import config


sympla = Sympla(token=config("TOKEN"))

participant = sympla.checkin_by_ticket_id(event_id=config("EVENT_ID"), participant_id=config("PARTICIPANT_ID"))
```

# Check-in por número do ingresso

Realiza o check-in de um participante por número do ingresso.

Saiba mais em: https://developers.sympla.com.br/api-doc/index.html#operation/checkInByTicketNumber

```python
from sympla import Sympla
from decouple import config


sympla = Sympla(token=config("TOKEN"))

participant = sympla.checkin_by_ticket_number(event_id=config("EVENT_ID"), ticket_number=config("TICKET_NUMBER"))
```

# Listar afiliados por evento

Retorna os afiliados do evento correspondente ao identificador informado.

Saiba mais em: https://developers.sympla.com.br/api-doc/index.html#tag/Afiliados

```python
from sympla import Sympla
from decouple import config


sympla = Sympla(token=config("TOKEN"))

affiliates = sympla.affiliates(event_id=config("EVENT_ID"))
```

# Contribua

Clone o projeto repositório:

```bash
$ git clone https://github.com/hudsonbrendon/sympla.git
```

Certifique-se de que o [Poetry](https://python-poetry.org/) está instalado, caso contrário:

```bash
$ pip install -U poetry
```

Acesse o repositório e instale as dependências:

```bash
$ poetry install
```
e
```bash
$ poetry shell
```

Para executar os testes:

```bash
$ pytest
```

# Dependências

- [Python >= 3.8](https://www.python.org/downloads/release/python-380/)

# Licença

[MIT](http://en.wikipedia.org/wiki/MIT_License)
