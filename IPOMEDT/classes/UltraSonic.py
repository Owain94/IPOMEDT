if __name__ == '__main__':
    from sys import path

    path.append("..")

from util.GPIOFuckUp import GPIOFuckUp
import RPi.GPIO as GPIO
from time import sleep, time


class UltraSonic:
    """
    Klasse om de ultrasonische sensoren uit te lezen
    """

    def __init__(self, input_pins: list) -> None:
        """
        Code die wordt uitgevoerd bij het instantiëren van de klasse

        :param input_pins: De GPIO pins waar de ultra sonische sensor op is aan gesloten
                           als lijst
        """
        self.speedSound = 33100 + (0.6 * 20)
        self.how_near = 15.0

        self.pin_trigger = input_pins[0]
        self.pin_echo = input_pins[1]

        GPIO.setup(self.pin_trigger, GPIO.OUT)
        GPIO.setup(self.pin_echo, GPIO.IN)

        GPIO.output(self.pin_trigger, False)

        sleep(0.1)

    def is_near_obstacle(self, local_how_near: float) -> bool:
        """
        Kijk of er een object dicht bij is

        :param local_how_near: afstand tot object
        :return: boolean
        """
        distance = self.measure()

        return bool(distance < local_how_near)

    def measure(self) -> float:
        """
        Meet de afstand tot een object

        :return: float afstand tot object
        """

        GPIO.output(self.pin_trigger, True)
        sleep(0.00001)
        GPIO.output(self.pin_trigger, False)
        start = time()
        stop = 0

        while GPIO.input(self.pin_echo) == 0:
            start = time()

        while GPIO.input(self.pin_echo) == 1:
            stop = time()

        elapsed = stop - start

        return round((elapsed * self.speedSound) / 2)


def main() -> None:
    """
    Code om de klasse te testen, deze code wordt niet uitgevoerd als de
    klasse in een ander bestand wordt geimporteerd!
    """
    GPIOFuckUp()

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    ultrasonic = UltraSonic([17, 18])

    try:
        GPIO.output(ultrasonic.pin_trigger, False)
        while True:
            sleep(0.1)
            if ultrasonic.is_near_obstacle(ultrasonic.how_near):
                print("STOP")
            else:
                print("GO")

    except KeyboardInterrupt:
        GPIO.cleanup()


# Zorg ervoor dat de main functie niet wordt uitgevoerd als de klasse
# wordt geimporteerd
if __name__ == '__main__':
    main()
