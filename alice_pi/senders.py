import sys
import inspect
import requests

class DataNotSentException(Exception):
    pass

class Sender(object):
    """
    A Sender's responsibility is to send a measurement to a particular platform.
    """


class RestSender(Sender):

    def __init__(self, base_url, method='get', headers=None,
                 measurement_name=None, extra_params=None):

        send_callables = {'get': self.get,
                          'post': self.post}

        self.base_url = base_url
        self.method = send_callables[method]
        self.headers = headers

        if self.headers is None:
            self.headers = {}

        self.measurement_name = measurement_name
        self.extra_params = extra_params

    def __handle_response(self, response):
        status = response.status_code

        if status not in [200, 201]:
            raise DataNotSentException('Received {} from {}'.format(status,
                                                                    self.base_url))

    def send(self, measurement):
        meas_dict = {self.measurement_name: measurement}

        if self.extra_params is not None:
            meas_dict.update(self.extra_params)


        self.method(meas_dict, self.headers)

    def get(self, params, headers):
        response = requests.get(self.base_url,
                                params=params,
                                headers=headers)

        self.__handle_response(response)

    def post(self, params, headers):
        response = requests.post(self.base_url,
                                 json=params,
                                 headers=headers)
        self.__handle_response(response)

classes = inspect.getmembers(sys.modules[__name__],
                             inspect.isclass)

SENDERS = dict([tuple(item) for item in classes
                if item[1].__module__ == __name__ and
                'Exception' not in item[0]])
