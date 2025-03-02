import time

import RPi.GPIO as GPIO

# config of the PINs
sensor_pin_1 = 17  # board pin 11
sensor_pin_2 = 18  # board pin 12
sensor_pin_3 = 27  # board pin 13

sensor_rate = 0.2


def check_current_input():
    if GPIO.input(sensor_pin_1):
        return sensor_pin_1
    elif GPIO.input(sensor_pin_2):
        return sensor_pin_2
    elif GPIO.input(sensor_pin_3):
        return sensor_pin_3


class TouchInput:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(sensor_pin_1, GPIO.IN)
        GPIO.setup(sensor_pin_2, GPIO.IN)
        GPIO.setup(sensor_pin_3, GPIO.IN)

    def check_touch_input(self, param_dict, callback):
        while True:
            current_input = check_current_input()
            if current_input == sensor_pin_1 or current_input == sensor_pin_2 or current_input == sensor_pin_3:
                print("Touch pin " + str(current_input))
                callback(param_dict[current_input])
            # Pause
            time.sleep(sensor_rate)
