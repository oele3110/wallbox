import time

# config of the PINs
sensor_pin_1 = 17  # board pin 11
sensor_pin_2 = 18  # board pin 12
sensor_pin_3 = 27  # board pin 13

sensor_rate = 0.2


class TouchInput:
    def __init__(self):
        self.last_input = 0

    def check_touch_input(self, param_dict, callback):
        while True:
            user_input = input("Sensor: ")
            input_value = int(user_input)
            if input_value == sensor_pin_1 or input_value == sensor_pin_2 or input_value == sensor_pin_3:
                print("Touch pin " + str(input_value))
                if self.last_input != input_value:
                    callback(param_dict[input_value])
                    self.last_input = input_value

            # Pause
            time.sleep(sensor_rate)
