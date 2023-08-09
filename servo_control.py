from gpiozero import AngularServo
import time

servo = AngularServo(18, min_angle=0, max_angle=180, min_pulse_width=0.0005, max_pulse_width=0.0025)

while True:
    servo.angle = 0
    time.sleep(2)
    servo.angle = 180
    time.sleep(2)
    servo.angle = 90
    time.sleep(2)
    servo.angle = 0
    print("Finished Cycle!")
    time.sleep(2)