import requests
import json
import subprocess


def send_to_ha(sensor_name, sensor_value, attributes=None):
    headers = {'x-ha-access': 'brotato',
               'content-type': 'application/json'}

    url = 'http://192.168.1.55:8123/api/states/' + sensor_name

    data = json.dumps({'state': sensor_value,
                       'attributes': attributes})

    response = requests.post(url,
                             headers=headers,
                             data=data)
    return response


def restart():
    command = "/usr/bin/sudo /sbin/shutdown -r now"

    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print output

if __name__ == "__main__":
    pass
