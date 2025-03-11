import json
import threading

from modbusReader.ModbusConfig import modbus_wallbox_config, modbus_wallbox_status_codes
from modbusReader.ModbusReader import ModbusReader

from output.Led import led_pin_1, led_pin_2, led_pin_3, Led
from output.drivers.i2c_dev import Lcd

timer_increment = 0.5
timer_maximum = 1000


def fill_string_with_spaces(display_string, chars):
    diff = chars - len(display_string)
    if diff > 0:
        display_string += diff * " "
    return display_string


class Output:
    def __init__(self):
        self.current_time = 0
        self.host = None
        self.read_smartmeter_config()

        print("Initialize Modbus Reader")
        self.modbusReader = ModbusReader(self.host)

        print("Initialize Display")
        self.lcd = Lcd()

        print("Initialize LEDs")
        self.led_param_dict = {
            2: led_pin_1,
            3: led_pin_2,
            4: led_pin_3
        }
        self.led = Led(self.led_param_dict)

    def start(self):
        print("Start input evaluation timer")
        timer = threading.Timer(timer_increment, self.timer_step)
        timer.daemon = True
        timer.start()

    def timer_step(self):
        # increment current_timer by timer_increment
        self.current_time += timer_increment
        for modbus_key, modbus_config in modbus_wallbox_config.items():
            if modbus_config["update_frequency"] % timer_increment == 0:
                modbus_result = self.modbusReader.read_modbus(modbus_config)
                if modbus_config["display_line"] > 0:
                    if "division" in modbus_config and modbus_config["division"] is not None:
                        modbus_result = modbus_result / modbus_config["division"]
                        if "division_round" in modbus_config and modbus_config["division_round"] is not None:
                            modbus_result = round(modbus_result, modbus_config["division_round"])
                            if modbus_config["division_round"] == 0:
                                modbus_result = int(modbus_result)
                    unit = modbus_config["unit"] if modbus_config["unit"] is not None else ""
                    if modbus_key == "wallbox_status_code":
                        modbus_result = modbus_wallbox_status_codes[modbus_result]
                    display_string = modbus_config["display_string"] + ": " + str(modbus_result) + " " + unit
                    display_string = fill_string_with_spaces(display_string, 20)
                    self.lcd.lcd_display_string(display_string, modbus_config["display_line"])
                elif modbus_config["display_line"] == 0:
                    # update leds
                    self.led.update_leds(modbus_result)

        # reset current_time if timer_maximum is reached
        if self.current_time > timer_maximum:
            self.current_time = 0
        timer = threading.Timer(timer_increment, self.timer_step)
        timer.daemon = True
        timer.start()

    def stop(self):
        self.modbusReader.__shutdown__()
        # TODO: dispose lcd

    def read_smartmeter_config(self):
        with open('smartMeterConfig.json', 'r') as file:
            data = json.load(file)
        self.host = data.get('host')
