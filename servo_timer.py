from gpiozero import AngularServo
import time

servo = AngularServo(18, min_angle=0, max_angle=180, min_pulse_width=0.0005, max_pulse_width=0.0025)
servoang = 0

while servoang<180:
    servo.angle = servoang
    servoang += 3
    time.sleep(1)
servo.angle = 0
stop()