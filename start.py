#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

# GPIO pin assignment for the piezo transducer.
TRANS_PIN = 19

# PWM parameters
FREQUENCY = 2000      # 2 kHz tone, audible and typical for piezo buzzers
DUTY_CYCLE = 50       # 50% duty cycle for a square wave

# Setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRANS_PIN, GPIO.OUT)

print("Generating a 2 kHz tone on GPIO", TRANS_PIN)

# Initialize and start PWM on the transducer pin
pwm = GPIO.PWM(TRANS_PIN, FREQUENCY)
pwm.start(DUTY_CYCLE)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopping tone and cleaning up GPIO...")
finally:
    pwm.stop()
    GPIO.cleanup()
