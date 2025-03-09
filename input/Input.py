import json
import threading

from chargemode.ChargeModeConfigurator import powermode, solar, solar_plus, ChargeModeConfigurator
from input.TouchInput import sensor_pin_1, sensor_pin_2, sensor_pin_3, TouchInput


class Input:
    def __init__(self):
        self.token = None
        self.port = None
        self.host = None
        self.read_wallbox_config()
        self.touch_input = TouchInput()

        print("Initialize touch inputs")
        self.param_dict = {sensor_pin_1: powermode, sensor_pin_2: solar, sensor_pin_3: solar_plus}
        self.charge_mode_configurator = ChargeModeConfigurator(self.host, self.port, self.token)

    def start(self):
        print("Start touch input evaluation")
        touch_input_thread = threading.Thread(target=self.touch_input.check_touch_input, args=(self.param_dict, self.charge_mode_configurator.put_charge_mode))
        touch_input_thread.start()

    def read_wallbox_config(self):
        with open('smartMeterConfig.json', 'r') as file:
            data = json.load(file)

        self.host = data.get('host')
        self.port = data.get('httpPort')
        self.token = data.get('httpToken')
