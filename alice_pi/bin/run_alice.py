#!/env/bin/python

from w1thermsensor import W1ThermSensor
import os
import time
import argparse
from alice_pi import configurers
from alice_pi import managers

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)

CONFIG_PATHS = [os.curdir, os.path.expanduser('~'),
                os.environ.get('ALICE_PI_CONFIG_DIR', '')]

def load_config():
    conf = configurers.Configurer()

    for dir in CONFIG_PATHS:
        try:
            measurers = conf.configure(os.path.join(dir,
                                                    'alice_pi_config.yml'))
            return measurers
        except IOError:
            pass

def main():
    measurers_and_senders = load_config()

    man = managers.Manager(measurers_and_senders)

    man.run()

if __name__ == "__main__":
    main()
