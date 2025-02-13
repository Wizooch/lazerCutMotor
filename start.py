#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

# GPIO pin assignment for the piezo transducer.
TRANS_PIN = 19

# Setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRANS_PIN, GPIO.OUT)

print("Starting frequency sweep from 20 Hz to 20 kHz on GPIO", TRANS_PIN)

# Initialize PWM with starting frequency of 20 Hz.
pwm = GPIO.PWM(TRANS_PIN, 20)
pwm.start(50)  # 50% duty cycle for a square wave

try:
    while True:
        # Sweep upward from 20 Hz to 20 kHz
        for freq in range(20, 20001, 20):
            pwm.ChangeFrequency(freq)
            time.sleep(0.005)  # Adjust the delay to control sweep speed
        # Sweep downward from 20 kHz back to 20 Hz
        for freq in range(20000, 19, -20):
            pwm.ChangeFrequency(freq)
            time.sleep(0.005)
except KeyboardInterrupt:
    print("\nFrequency sweep interrupted by user.")
finally:
    pwm.stop()
    GPIO.cleanup()
    print("Cleaned up GPIO. Exiting.")
