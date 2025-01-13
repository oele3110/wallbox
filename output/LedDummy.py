# config of the PINs
led_pin_1 = 22  # board pin 15
led_pin_2 = 23  # board pin 16
led_pin_3 = 24  # board pin 18


def led_on(led):
    print("LED " + str(led) + ": ON")


def led_off(led):
    print("LED " + str(led) + ": OFF")


class Led:
    def __init__(self, led_param_dict):
        self.led_param_dict = led_param_dict

    def update_leds(self, wallbox_charge_mode):
        for mode, led in self.led_param_dict.items():
            if mode == wallbox_charge_mode:
                led_on(led)
            else:
                led_off(led)
