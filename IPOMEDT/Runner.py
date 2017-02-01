from util.GPIOFuckUp import GPIOFuckUp
from util.Logger import Logger

from classes.LineDetection import LineDetection
from classes.MotorPwm import MotorPwm
from classes.UltraSonic import UltraSonic
from classes.Light import Light

import RPi.GPIO as GPIO

from time import sleep
from threading import Thread


class Runner:
    @staticmethod
    def measure(ultrasonic: UltraSonic) -> float:
        val = ultrasonic.measure()
        if val > 1000 or val < 0:
            return -1
        else:
            return val

    def runner(self) -> None:
        GPIOFuckUp()

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        line_detection = LineDetection(25)
        ultrasonic = UltraSonic([17, 18])
        motor = MotorPwm([10, 9, 8, 7])
        light = Light([21, 20])
        logger = Logger()

        previous = "left"

        try:
            light.turn_on()
            while not line_detection.color():
                ultra_measure = self.measure(ultrasonic)
                logger.append("Ultrasonic measurement: {}".format(ultra_measure))
                if ultra_measure <= 15:
                    if previous is "left":
                        motor.left_backward_right_forward(25)
                        logger.append(
                            "Turning the left wheel backwards and right wheel forwards with a PWM value of 25%")
                    else:
                        motor.right_backward_left_forward(25)
                        logger.append(
                            "Turning the right wheel backwards and left wheel forwards with a PWM value of 25%")
                    sleep(0.54)
                    motor.stop()
                    logger.append("Motor stopped")

                    ultra_measure = self.measure(ultrasonic)
                    logger.append("Ultrasonic measurement: {}".format(ultra_measure))
                    if ultra_measure is -1 or ultra_measure > 15:
                        motor.forward(100)
                        logger.append("moving forwards for 0.175 seconds with a PWM value of 25%")
                        sleep(0.175)
                        motor.stop()
                        logger.append("Motor stopped for 0.15 seconds")
                        sleep(0.15)

                    ultra_measure = self.measure(ultrasonic)
                    logger.append("Ultrasonic measurement: {}".format(ultra_measure))
                    if ultra_measure is -1 or ultra_measure > 15:
                        if previous is "left":
                            motor.left_backward_right_forward(25)
                            logger.append(
                                "Turning the left wheel backwards and right wheel forwards with a PWM value of 25")
                        else:
                            motor.right_backward_left_forward(25)
                            logger.append(
                                "Turning the right wheel backwards and left wheel forwards with a PWM value of 25")
                        sleep(0.5)
                        motor.stop()
                        logger.append("Motor stopped")

                        if previous is "left":
                            previous = "right"
                        else:
                            previous = "left"
                        logger.append("Saving the previous turning direction")

                else:
                    motor.forward(25)
                    sleep(0.5)
                    motor.stop()

            logger.append("FOUND THE DOT!")
            motor.stop()
            logger.append("Motor stopped")
        except KeyboardInterrupt:
            motor.stop()
            GPIO.cleanup()

    def start_runner(self):
        thread = Thread(target=self.runner)
        thread.setDaemon(True)
        thread.start()


# Zorg ervoor dat de main functie niet wordt uitgevoerd als de klasse
# wordt geimporteerd
if __name__ == '__main__':
    runner = Runner()
    runner.runner()
