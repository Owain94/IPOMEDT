if __name__ == '__main__':
    from sys import path

    path.append("..")

from util.GPIOFuckUp import GPIOFuckUp
import RPi.GPIO as GPIO
from time import sleep, time


class LineDetection:
    """
    Klasse om de line detection sensoren uit te lezen
    """

    def __init__(self, input_pin: int) -> None:
        """
        Code die wordt uitgevoerd bij het instantiëren van de klasse

        :param input_pin: De GPIO pin waar de sensor op is aan gesloten
                          als lijst
        """
        self.pin = input_pin

        GPIO.setup(self.pin, GPIO.IN)

    def color(self) -> bool:
        """
        Lees de waarde van de sensor uit

        :return: boolean
        """
        if GPIO.input(self.pin) == 0:
            return True
        else:
            return False


def main() -> None:
    """
    Code om de klasse te testen, deze code wordt niet uitgevoerd als de
    klasse in een ander bestand wordt geimporteerd!
    """
    GPIOFuckUp()

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    line_detection = LineDetection(25)

    while True:
        if line_detection.color():
            print('Zwart')
        else:
            print('Wit')


# Zorg ervoor dat de main functie niet wordt uitgevoerd als de klasse
# wordt geimporteerd
if __name__ == '__main__':
    main()
