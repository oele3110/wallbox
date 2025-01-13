import json

import requests

powermode = 'grid'
solar = 'pv'
solar_plus = 'hybrid'


# url = 'http://host:port/api/e-mobility/config/chargemode'

class ChargeModeConfigurator:
    def __init__(self, host, port, token):
        self.host = host
        self.port = port
        self.token = token
        self.url = 'http://' + host + ':' + str(port) + '/api/e-mobility/config/chargemode'

    def get_header(self):
        return {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }

    def get_charge_mode(self):
        response = requests.get(self.url, headers=self.get_header())
        if response.status_code == 200:
            print('Success:', response.json())
        else:
            print('Error:', response.status_code, response.text)

    # possible charge modes are
    # Power Mode: {mode: "grid", controlledby: 0, mincharginpowerquota: null, minpvpowerquota: 0}
    # Solar Charge: {mode: "pv", controlledby: 0, mincharginpowerquota: null, minpvpowerquota: 100}
    # Solar Charge Plus: {mode: "hybrid", controlledby: 0, mincharginpowerquota: 0, minpvpowerquota: 100}
    def put_charge_mode(self, charge_mode):
        json_data = {
            'mode': charge_mode
        }
        response = requests.put(self.url, headers=self.get_header(), data=json.dumps(json_data))

        if response.status_code == 200:
            print('Success:', response.json())
        elif response.status_code == 204:
            print('Success: charge mode correctly set to ', charge_mode)
        else:
            print('Error:', response.status_code, response.text)
