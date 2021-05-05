import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
servo = GPIO.PWM(8, 1000)
servo.start(50)
sleep(3)
servo.stop()


