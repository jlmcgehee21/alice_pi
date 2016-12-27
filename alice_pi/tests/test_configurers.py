import unittest2 as unittest
import os
from alice_pi import configurers
from alice_pi import senders
from alice_pi import measurers
from alice_pi.tests import TEST_DIR


class TestConfigurer(unittest.TestCase):
    config_path = os.path.join(TEST_DIR, 'test_config.yml')

    def test_configure(self):
        conf = configurers.Configurer()
        measurers_and_senders = conf.configure(self.config_path)

        extracted_senders = [item['senders'] for item in measurers_and_senders]
        is_sender = [isinstance(item, senders.Sender)
                     for sublist in extracted_senders for item in sublist]

        self.assertTrue(all(is_sender))

        is_measurer = [isinstance(item['measurer'], measurers.Measurer)
                       for item in measurers_and_senders]

        self.assertTrue(all(is_measurer))
