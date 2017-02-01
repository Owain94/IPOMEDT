if __name__ == '__main__':
    from sys import path

    path.append("..")

from util.GPIOFuckUp import GPIOFuckUp
import RPi.GPIO as GPIO
from time import sleep


class MotorPwm:
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
        GPIO.setup(input_pins[0], GPIO.OUT)
        GPIO.setup(input_pins[1], GPIO.OUT)
        GPIO.setup(input_pins[2], GPIO.OUT)
        GPIO.setup(input_pins[3], GPIO.OUT)

        self.coil_a_1_pin = GPIO.PWM(input_pins[0], 30)
        self.coil_a_2_pin = GPIO.PWM(input_pins[1], 30)
        self.coil_b_1_pin = GPIO.PWM(input_pins[2], 30)
        self.coil_b_2_pin = GPIO.PWM(input_pins[3], 30)

        self.coil_a_1_pin.start(0)
        self.coil_a_2_pin.start(0)
        self.coil_b_1_pin.start(0)
        self.coil_b_2_pin.start(0)

    def set_step(self, step: list, speed: int = 100) -> None:
        """
        Als bijvoorbeeld de step variabele '0100' bevat wordt er alleen op de
        tweede pin stroom gezet. Zo draait het motorje elke keer (reeks
        die meegegeven wordt is: 1000, 0100, 0010, 0001) een stapje verder

        :param speed: Snelheid
        :param step: Het aantal stappen als string
                     (0100 = false, true, false, false)
        """
        self.coil_a_1_pin.ChangeDutyCycle((0, speed)[step[0]])
        self.coil_a_2_pin.ChangeDutyCycle((0, speed)[step[1]])
        self.coil_b_1_pin.ChangeDutyCycle((0, speed)[step[2]])
        self.coil_b_2_pin.ChangeDutyCycle((0, speed)[step[3]])

    def forward(self, speed: int = 100) -> None:
        """
        Laat de motor vooruit draaien
        """
        self.set_step([True, False, True, False], speed)

    def backward(self, speed: int = 100) -> None:
        """
        Laat de motor achteruit draaien
        """
        self.set_step([False, True, False, True], speed)

    def left_forward(self, speed: int = 100) -> None:
        """
        Laat de linker motor draaien
        """
        self.set_step([False, False, True, False], speed)

    def right_forward(self, speed: int = 100) -> None:
        """
        Laat de rechter motor draaien
        """
        self.set_step([True, False, False, False], speed)

    def left_backward(self, speed: int = 100) -> None:
        """
        Laat de linker motor draaien
        """
        self.set_step([False, False, False, True], speed)

    def right_backward(self, speed: int = 100) -> None:
        """
        Laat de rechter motor draaien
        """
        self.set_step([False, True, False, False], speed)

    def right_backward_left_forward(self, speed: int = 100) -> None:
        self.set_step([False, True, True, False], speed)

    def left_backward_right_forward(self, speed: int = 100) -> None:
        self.set_step([True, False, False, True], speed)

    def stop(self) -> None:
        """
        Haal de stroom van alle GPIO pinnen die worden gebruikt
        """
        self.set_step([False, False, False, False])


def main() -> None:
    """
    Code om de klasse te testen, deze code wordt niet uitgevoerd als de
    klasse in een ander bestand wordt geimporteerd!
    """
    GPIOFuckUp()

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    motor = MotorPwm([10, 9, 8, 7])

    motor.right_forward(10)
    sleep(1)
    motor.stop()

    GPIO.cleanup()


# Zorg ervoor dat de main functie niet wordt uitgevoerd als de klasse
# wordt geimporteerd
if __name__ == '__main__':
    main()
