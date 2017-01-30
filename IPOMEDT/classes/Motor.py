if __name__ == '__main__':
    from sys import path

    path.append("..")

from util.GPIOFuckUp import GPIOFuckUp
import RPi.GPIO as GPIO
from time import sleep


class Motor:
    """
    Klasse om een motor aan te sturen
    """

    def __init__(self, input_pins: list) -> None:
        """
        Code die wordt uitgevoerd bij het instantiëren van de klasse

        :param input_pins: De GPIO pins waar de motor op is aan gesloten
                           als lijst
        """
        # De sequentie die wordt gebruikt om de motor te laten draaien
        # (gedefinieerd als constante)
        self.coil_a_1_pin = input_pins[0]
        self.coil_a_2_pin = input_pins[1]
        self.coil_b_1_pin = input_pins[2]
        self.coil_b_2_pin = input_pins[3]

        GPIO.setup(self.coil_a_1_pin, GPIO.OUT)
        GPIO.setup(self.coil_a_2_pin, GPIO.OUT)
        GPIO.setup(self.coil_b_1_pin, GPIO.OUT)
        GPIO.setup(self.coil_b_2_pin, GPIO.OUT)

        self.count = 0

    def set_step(self, step: list) -> None:
        """
        Als bijvoorbeeld de step variabele '0100' bevat wordt er alleen op de
        tweede pin stroom gezet. Zo draait het motorje elke keer (reeks
        die meegegeven wordt is: 1000, 0100, 0010, 0001) een stapje verder

        :param step: Het aantal stappen als string
                     (0100 = false, true, false, false)
        """

        GPIO.output(self.coil_a_1_pin, step[0])
        GPIO.output(self.coil_a_2_pin, step[1])
        GPIO.output(self.coil_b_1_pin, step[2])
        GPIO.output(self.coil_b_2_pin, step[3])

    def forward(self) -> None:
        """
        Laat de motor vooruit draaien
        """
        self.set_step([True, False, True, False])

    def backward(self) -> None:
        """
        Laat de motor achteruit draaien
        """
        self.set_step([False, True, False, True])

    def right(self) -> None:
        """
        Laat de linker motor draaien
        """
        self.set_step([False, False, True, False])

    def left(self) -> None:
        """
        Laat de rechter motor draaien
        """
        self.set_step([True, False, False, False])

    def stop(self) -> None:
        """
        Haal de stroom van alle GPIO pinnen die worden gebruikt
        """
        GPIO.output(self.coil_a_1_pin, False)
        GPIO.output(self.coil_a_2_pin, False)
        GPIO.output(self.coil_b_1_pin, False)
        GPIO.output(self.coil_b_2_pin, False)


def main() -> None:
    """
    Code om de klasse te testen, deze code wordt niet uitgevoerd als de
    klasse in een ander bestand wordt geimporteerd!
    """
    GPIOFuckUp()

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    motor = Motor([10, 9, 8, 7])

    motor.forward()
    sleep(1)
    motor.stop()
    sleep(1)

    motor.backward()
    sleep(1)
    motor.stop()
    sleep(1)

    motor.left()
    sleep(1)
    motor.stop()
    sleep(1)

    motor.right()
    sleep(1)
    motor.stop()
    sleep(1)

    GPIO.cleanup()


# Zorg ervoor dat de main functie niet wordt uitgevoerd als de klasse
# wordt geimporteerd
if __name__ == '__main__':
    main()
