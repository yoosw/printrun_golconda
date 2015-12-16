import wiringpi2 as wiringpi
from time import sleep

enable_motor_a = 24
enable_motor_b = 25

enable_led_a = 26
enable_led_b = 21

# power_pin = 15
sensor = 4

class control_gpio:

    def __init__(self):
        wiringpi.wiringPiSetupGpio()

        # Set pin states
        wiringpi.pinMode(enable_led_a, 1)
        wiringpi.pinMode(enable_led_b, 1)
        wiringpi.pinMode(sensor, 0)
        wiringpi.pinMode(enable_motor_a, 1)
        wiringpi.pinMode(enable_motor_b, 1)

        wiringpi.digitalWrite(enable_led_a, 0)
        wiringpi.digitalWrite(enable_led_b, 0)
        wiringpi.digitalWrite(enable_motor_a, 0)
        wiringpi.digitalWrite(enable_motor_b, 0)

    def sensor_detect(self):
        if wiringpi.digitalRead(sensor):
            return True
        else:
            return False

    def led_on(self):
        wiringpi.digitalWrite(enable_led_a, 1)
        wiringpi.digitalWrite(enable_led_b, 1)

    def led_off(self):
        wiringpi.digitalWrite(enable_led_a, 0)
        wiringpi.digitalWrite(enable_led_b, 0)

    def motor_forward(self, x):
        wiringpi.digitalWrite(enable_motor_a, 1)
        sleep(x)
        wiringpi.digitalWrite(enable_motor_a, 0)

    def motor_reverse(self, x):
        wiringpi.digitalWrite(enable_motor_b, 1)
        sleep(x)
        wiringpi.digitalWrite(enable_motor_b, 0)

    def motor_off(self):
        wiringpi.digitalWrite(enable_motor_a, 0)
        wiringpi.digitalWrite(enable_motor_b, 0)
