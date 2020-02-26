# pysympla
A plataforma online de eventos líder no Brasil. Venda de ingressos, promoção e administração de eventos. Simples e segura. Organiza eventos? Sympla!

![Python package](https://github.com/hudsonbrendon/pysympla/workflows/Python%20package/badge.svg?branch=master)
[![Github Issues](http://img.shields.io/github/issues/hudsonbrendon/pysympla.svg?style=flat)](https://github.com/hudsonbrendon/pysympla/issues?sort=updated&state=open)
![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)

![Sympla](https://logodownload.org/wp-content/uploads/2018/10/sympla-logo-3.png)

# Recursos Disponíveis

- [x]  Listar eventos
- [x]  Listar evento por identificador
- [ ]  Listar pedidos por evento
- [ ]  Listar pedidos por identificador
- [ ]  Listar participantes por pedido
- [ ]  Listar participantes por evento
- [ ]  Listar participante por número de ingresso
- [ ]  Listar afiliados por evento

# Instalação

```bash
$ pip install pysympla
```
ou

```bash
$ python setup.py install
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
from pysympla import Sympla
from decouple import config


sympla = Sympla(token=config("TOKEN"))

events = sympla.events()
```

# Listar eventos por identificador

Retorna o evento correspondente ao identificador informado.

Saiba mais em: https://developers.sympla.com.br/api-doc/index.html#operation/getEventId

```python
from pysympla import Sympla
from decouple import config


sympla = Sympla(token=config("TOKEN"))

event = sympla.events(id=config("EVENT_ID"))
```

# Contribua

Clone o projeto repositório:

```bash
$ git clone https://github.com/hudsonbrendon/pysympla.git
```

Certifique-se de que o [Pipenv](https://github.com/kennethreitz/pipenv) está instalado, caso contrário:

```bash
$ pip install -U pipenv
```

Acesse o repositório e instale as dependências:

```bash
$ make install
```

Para executar os testes:

```bash
$ make test
```

# Dependências

- [Python 3.8+](https://www.python.org/downloads/release/python-374/)
- [Pipenv](https://github.com/kennethreitz/pipenv)

# Licença

[MIT](http://en.wikipedia.org/wiki/MIT_License)
