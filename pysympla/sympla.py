import requests


class Sympla(object):

    _URL = "https://api.sympla.com.br/public/v3/"

    def __init__(self, token):
        self.__token = token
