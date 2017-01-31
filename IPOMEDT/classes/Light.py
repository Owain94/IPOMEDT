if __name__ == '__main__':
    from sys import path

    path.append("..")

import RPi.GPIO as GPIO
import time
from threading import Thread


class Light:
    def __init__(self, pins: list):
        left_light = pins[0]
        right_light = pins[1]

        GPIO.setup(left_light, GPIO.OUT)
        GPIO.setup(right_light, GPIO.OUT)

        self.left_pin = GPIO.PWM(left_light, 1000)
        self.right_pin = GPIO.PWM(right_light, 1000)

        self.left_pin.start(0)
        self.right_pin.start(0)

        self.thread = None

    def turn_on_left(self):
        self.dim_left(100)

    def turn_on_right(self):
        self.dim_right(100)

    def turn_on(self):
        self.dim_left(100)
        self.dim_right(100)

    def turn_off_left(self):
        self.dim_left(0)

    def turn_off_right(self):
        self.dim_right(0)

    def turn_off(self):
        self.dim_left(0)
        self.dim_right(0)

    def dim(self, percentage):
        self.dim_left(percentage)
        self.dim_right(percentage)

    def dim_left(self, percentage):
        self.left_pin.ChangeDutyCycle(percentage)

    def dim_right(self, percentage):
        self.right_pin.ChangeDutyCycle(percentage)

    def siren_loop(self):
        while True:
            self.dim_left(100)
            self.dim_right(100)
            time.sleep(0.05)

            self.turn_off_left()
            self.turn_off_right()
            time.sleep(0.05)

            self.dim_right(100)
            time.sleep(0.05)

            self.turn_on_right()
            time.sleep(0.05)

            self.dim_left(100)
            time.sleep(0.05)

            self.dim_left(0)
            time.sleep(0.05)

    def start_sirene(self):
        self.thread = Thread(target=self.siren_loop)
        self.thread.setDaemon(True)
        self.thread.start()

    def stop_sirene(self):
        self.thread.do_run = False


def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    light = Light([21, 20])

    light.start_sirene()
    time.sleep(1)
    light.stop_sirene()

if __name__ == '__main__':
    main()
