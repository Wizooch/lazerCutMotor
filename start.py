#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

# GPIO pin assignment for the piezo transducer.
# Using GPIO19 to avoid pins 18, 23, and 24.
TRANS_PIN = 19

# PWM parameters
FREQUENCY = 32000      # 32 kHz
DUTY_CYCLE = 50        # 50% duty cycle

# Setup GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRANS_PIN, GPIO.OUT, initial=GPIO.LOW)

print("========== Piezo Transducer Continuous Test ==========")
print(f"DEBUG: Setting up PWM on GPIO {TRANS_PIN} at {FREQUENCY} Hz with a {DUTY_CYCLE}% duty cycle.")

# Initialize and start PWM on the transducer pin
pwm = GPIO.PWM(TRANS_PIN, FREQUENCY)
pwm.start(DUTY_CYCLE)
print("DEBUG: PWM started. Playing 32 kHz tone continuously...")

try:
    # Run indefinitely until interrupted by the user.
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nDEBUG: Test Interrupted by user (Ctrl+C).")
finally:
    print("DEBUG: Stopping PWM and cleaning up GPIO pins...")
    pwm.stop()
    GPIO.cleanup()
    print("========== Piezo Transducer Test Ended ==========")
