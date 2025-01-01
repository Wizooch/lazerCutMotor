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

# Enable driver (LOW on many drivers means "enabled")
GPIO.output(ENABLE_PIN, GPIO.LOW)

# Set direction (HIGH = CW, LOW = CCW depending on your driver)
GPIO.output(DIR_PIN, GPIO.HIGH)

# Define a step delay (tune this for your desired speed)
step_delay = 0.001

try:
    # Run motor continuously
    while True:
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(step_delay)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(step_delay)

except KeyboardInterrupt:
    # If you press Ctrl+C, exit gracefully
    pass

finally:
    # OPTIONAL: If you actually want to leave it enabled,
    # you can comment out the line below or set it to LOW
    # so it stays enabled. But typically it's good practice
    # to disable and clean up for safety.

    # Disable driver
    # GPIO.output(ENABLE_PIN, GPIO.HIGH)

    GPIO.cleanup()
