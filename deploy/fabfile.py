__author__ = 'Jeff'

import os
from fabric.api import run, cd, env, lcd, sudo, put, local, settings


CURDIR = os.path.dirname(os.path.realpath(__file__))

local_app_dir = os.path.join(os.path.dirname(CURDIR))
remote_app_dir = '/usr/bin/alice_pi'
app_name = 'alice_pi'

def prod():

    env.hosts = [os.environ.get('PI_IP', 'localhost')]
    env.user = os.environ.get('PI_USER', 'pi')
    env.password = os.environ.get('PI_PASS', 'raspberry')
    env.keepalive = 20

def deploy():
    with settings(warn_only=True):
        sudo('stop temperature_daemon')
        sudo('stop motion_daemon')
        sudo('rm /etc/init/temperature_daemon.conf')
        sudo('killall python')

    with lcd(local_app_dir):
        sudo('mkdir -p %s' % (remote_app_dir))
        with cd(remote_app_dir):
            put('*', './', use_sudo=True)

            sudo('virtualenv --system-site-packages env')
            sudo('env/bin/pip install -r requirements.txt')


    put('temperature_daemon.conf', '/etc/init', use_sudo=True)

    sudo('service temperature_daemon start')


def setup_server():
    sudo('apt-get update')

    #Dallas 1-Wire
    sudo('echo "dtoverlay=w1-gpio" >> /boot/config.txt')

    # Python
    sudo('apt-get -y install python-dev build-essential')
    sudo('apt-get -y install python-pip')
    sudo('pip install virtualenv')
    sudo('apt-get -y install libatlas-base-dev gfortran')
    sudo('apt-get -y install python-matplotlib')
    sudo('apt-get -y install python-scipy')

    # Source Control
    sudo('apt-get -y install mercurial')
    sudo('apt-get -y install git')

    sudo('apt-get -y --force-yes install upstart')

    # mysql client
    sudo('apt-get -y install libmysqlclient-dev')


    # Deploy app
    # deploy()

    sudo('reboot')


if __name__ == "__main__":

    print(local_app_dir)
