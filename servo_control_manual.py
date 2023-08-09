from gpiozero import AngularServo
import time
import keyboard

servo = AngularServo(18, min_angle=0, max_angle=180, min_pulse_width=0.0005, max_pulse_width=0.0025)
servo.angle = 0

while True:
    try:
        if keyboard.is_pressed("1") == True:
            servo.angle = 0
        elif keyboard.is_pressed("2") == True:
            servo.angle = 30
        elif keyboard.is_pressed("3") == True:
            servo.angle = 60
        elif keyboard.is_pressed("4") == True:
            servo.angle = 90
        elif keyboard.is_pressed("5") == True:
            servo.angle = 120
        elif keyboard.is_pressed("6") == True:
            servo.angle = 150
        elif keyboard.is_pressed("7") == True:
            servo.angle = 180
        elif keyboard.is_pressed("q") == True:
            servo.angle = 0
            exit()
    except:
        pass