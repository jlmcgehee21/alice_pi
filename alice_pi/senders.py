import requests

class DataNotSentException(Exception):
    pass

class Sender(object):
    """
    A Sender's responsibility is to send a measurement to a particular platform.
    """


class RestSender(Sender):
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers

    def __handle_response(self, response):
        status = response.status_code

        if status not in [200, 201]:
            raise DataNotSentException('Received {} from {}'.format(status,
                                                                    self.base_url))

    def get(self, **params):
        response = requests.get(self.base_url, params=params)
        self.__handle_response(response)

    def post(self, **params):
        response = requests.post(self.base_url, json=params)
        self.__handle_response(response)

class HomeAssistantSender(RestSender):
    pass
