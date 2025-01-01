import RPi.GPIO as GPIO
import time

# GPIO setup
STEP_PIN = 18
DIR_PIN = 23
ENABLE_PIN = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(ENABLE_PIN, GPIO.OUT)

# Enable driver
GPIO.output(ENABLE_PIN, GPIO.LOW)

# Set direction
GPIO.output(DIR_PIN, GPIO.HIGH)  # High = CW, Low = CCW

# Step motor
for _ in range(200):  # 200 steps for one revolution (assuming 1.8° per step)
    GPIO.output(STEP_PIN, GPIO.HIGH)
    time.sleep(0.001)  # Step delay (adjust for speed)
    GPIO.output(STEP_PIN, GPIO.LOW)
    time.sleep(0.001)

# ENABLE driver
GPIO.output(ENABLE_PIN, GPIO.LOW)

GPIO.cleanup()
