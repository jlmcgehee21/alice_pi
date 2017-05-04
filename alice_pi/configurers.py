from alice_pi.senders import SENDERS
from alice_pi.measurers import MEASURERS
import yaml


class Configurer(object):
    def configure(self, config_path):

        config_dict = self.__load_config_dict(config_path)

        measurers = []
        for meas_group in config_dict.values():
            measurer = meas_group['measurer'][0]
            measurer_name = next(iter(measurer))
            measurer_params = measurer.get(measurer_name)

            if measurer_params is None:
                measurer_params = {}

            measurer = MEASURERS[measurer_name](**measurer_params)

            senders = []
            for sender in meas_group['senders']:
                sender_name = next(iter(sender))
                sender_params = sender.get(sender_name)

                if sender_params is None:
                    sender_params = {}

                sender_obj = SENDERS[sender_name](**sender_params)
                senders.append(sender_obj)

            measurers.append(dict(measurer=measurer,
                                  senders=senders))
        return measurers

    def __load_config_dict(self, config_path):
        with open(config_path) as conf_file:
            config_dict = yaml.load(conf_file)

        return config_dict

