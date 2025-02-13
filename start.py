#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

# GPIO pin assignment for the piezo transducer.
TRANS_PIN = 19

# Setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRANS_PIN, GPIO.OUT)

print("Starting frequency sweep (100 Hz to 1 kHz) for paper vibration on GPIO", TRANS_PIN)

# Initialize PWM starting at 100 Hz with a 50% duty cycle.
pwm = GPIO.PWM(TRANS_PIN, 100)
pwm.start(50)

try:
    while True:
        # Sweep upward from 100 Hz to 1000 Hz
        for freq in range(100, 1001, 10):  # 10 Hz increments
            pwm.ChangeFrequency(freq)
            print(f"Sweeping upward: {freq} Hz")
            time.sleep(0.02)  # Adjust delay to control sweep speed
        # Sweep downward from 1000 Hz to 100 Hz
        for freq in range(1000, 99, -10):
            pwm.ChangeFrequency(freq)
            print(f"Sweeping downward: {freq} Hz")
            time.sleep(0.02)
except KeyboardInterrupt:
    print("\nFrequency sweep interrupted by user.")
finally:
    pwm.stop()
    GPIO.cleanup()
    print("Cleaned up GPIO. Exiting.")
