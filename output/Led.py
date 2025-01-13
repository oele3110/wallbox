import RPi.GPIO as GPIO

# config of the PINs
led_pin_1 = 22  # board pin 15
led_pin_2 = 23  # board pin 16
led_pin_3 = 24  # board pin 18


def led_on(led):
    GPIO.output(led, GPIO.HIGH)


def led_off(led):
    GPIO.output(led, GPIO.LOW)


class Led:
    def __init__(self, led_param_dict):
        self.led_param_dict = led_param_dict

        GPIO.setwarnings(False)  # Ignore warning for now
        GPIO.setup(led_pin_1, GPIO.OUT, initial=GPIO.LOW)  # Set pin 22 to be an output pin and set initial value to low (off)
        GPIO.setup(led_pin_2, GPIO.OUT, initial=GPIO.LOW)  # Set pin 23 to be an output pin and set initial value to low (off)
        GPIO.setup(led_pin_3, GPIO.OUT, initial=GPIO.LOW)  # Set pin 24 to be an output pin and set initial value to low (off)

    def update_leds(self, wallbox_charge_mode):
        for mode, led in self.led_param_dict.items():
            if mode == wallbox_charge_mode:
                led_on(led)
            else:
                led_off(led)
