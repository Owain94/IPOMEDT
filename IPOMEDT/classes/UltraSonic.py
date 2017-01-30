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
        self.how_near = 15.0
        self.reverse_time = 0.5
        self.turn_time = 0.75

        self.pin_trigger = input_pins[0]
        self.pin_echo = input_pins[1]

        GPIO.setup(self.pin_trigger, GPIO.OUT)
        GPIO.setup(self.pin_echo, GPIO.IN)

    def is_near_obstacle(self, local_how_near: float) -> bool:
        """
        Kijk of er een object dicht bij is

        :param local_how_near: afstand tot object
        :return: boolean
        """
        distance = self.measure()

        if distance < local_how_near:
            return True
        else:
            return False

    def measure(self) -> float:
        """
        Meet de afstand tot een object

        :return: float afstand tot object
        """
        GPIO.output(self.pin_trigger, True)

        sleep(0.00001)

        GPIO.output(self.pin_trigger, False)

        start_time = time()
        stop_time = start_time

        while GPIO.input(self.pin_echo) == 0:
            start_time = time()
            stop_time = start_time

        while GPIO.input(self.pin_echo) == 1:
            stop_time = time()

            if stop_time - start_time >= 0.04:
                stop_time = start_time
                break

        distance = ((stop_time - start_time) * 34326) / 2

        return distance


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
        sleep(0.1)
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
