import RPi.GPIO as GPIO
import time


class Wheel(object):

    def __init__(self, inputA, inputB, enable):
        """Input ints are BCM GPIO pin numbers connecting to
        the stepper motor.
        """
        self.a = inputA
        self.b = inputB
        self.enable = enable

        # Establish direction of GPIO pints
        GPIO.setup(self.a, GPIO.OUT)
        GPIO.setup(self.b, GPIO.OUT)
        GPIO.setup(self.enable, GPIO.OUT)

    def forward(self):
        GPIO.output(self.enable, 1)
        GPIO.output(self.a, 1)

    def reverse(self):
        GPIO.output(self.enable, 1)
        GPIO.output(self.b, 1)

    def stop(self):
        GPIO.output(self.enable, 0)
        GPIO.output(self.a, 0)
        GPIO.output(self.b, 0)


class Car():

    def __init__(self, frontleft, frontright):
        """Requires two Wheel objects."""
        self.fl = frontleft
        self.fr = frontright

    def forward(self, length):
        """Drives forward for the length in seconds."""
        self.fl.forward()
        self.fr.forward()
        time.sleep(length)
        self.fl.stop()
        self.fr.stop()

    def reverse(self, length):
        """Drives in reverse for the length in seconds."""
        self.fl.reverse()
        self.fr.reverse()
        time.sleep(length)
        self.fl.stop()
        self.fr.stop()

    def turn_right(self, length):
        """Runs wheels in opposite directions for length in seconds."""
        self.fr.reverse()
        self.fl.forward()
        time.sleep(length)
        self.fr.stop()
        self.fl.stop()

    def turn_left(self, length):
        """Runs wheels in opposite directions for length in seconds."""
        self.fl.reverse()
        self.fr.forward()
        time.sleep(length)
        self.fl.stop()
        self.fr.stop()


def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    frontleft = Wheel(14, 15, 18)
    frontright = Wheel(17, 27, 22)

    car = Car(frontleft, frontright)

    car.forward(3)
    car.reverse(3)


if __name__ == "__main__":
    main()
