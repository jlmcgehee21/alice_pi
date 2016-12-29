import unittest2 as unittest
from alice_pi import senders
import mock


class TestRestSender(unittest.TestCase):
    @mock.patch('requests.get',
                return_value=mock.MagicMock(status_code=404))
    def test_get_breaks_for_non_200(self, mock_get):
        sender = senders.RestSender('http://blah')

        with self.assertRaises(senders.DataNotSentException):
            sender.get(dict(test='a', test2='b'), {})

    @mock.patch('requests.post',
                return_value=mock.MagicMock(status_code=404))
    def test_post_breaks_for_non_200(self, mock_post):
        sender = senders.RestSender('http://blah')

        with self.assertRaises(senders.DataNotSentException):
            sender.post(dict(test='a', test2='b'), {})

    @mock.patch('requests.get',
                return_value=mock.MagicMock(status_code=200))
    def test_get_passes_200(self, mock_get):
        senders.RestSender('http://blah')

    @mock.patch('requests.post',
                return_value=mock.MagicMock(status_code=200))
    def test_post_passes_200(self, mock_post):
        senders.RestSender('http://blah')


if __name__ == '__main__':
    unittest.main()
