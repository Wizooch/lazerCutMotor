import RPi.GPIO as GPIO
import time

# GPIO pin assignments
STEP_PIN = 18
DIR_PIN = 23
ENABLE_PIN = 24

# (Optional) If you want to see any warnings about pins in use, etc.
GPIO.setwarnings(True)

# Use BCM numbering
GPIO.setmode(GPIO.BCM)

# Set up pins as outputs
# 'initial=GPIO.LOW' ensures pins start at a known LOW state
GPIO.setup(STEP_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(DIR_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ENABLE_PIN, GPIO.OUT, initial=GPIO.HIGH)

# Debug: Start message
print("========== Motor Test Starting ==========")

# 1) Enable the driver (LOW for A4988 typically means 'enabled')
GPIO.output(ENABLE_PIN, GPIO.LOW)
print("DEBUG: ENABLE_PIN set to LOW (driver enabled).")

# 2) Set direction pin
GPIO.output(DIR_PIN, GPIO.HIGH)  # High = CW (depending on driver orientation)
print("DEBUG: DIR_PIN set to HIGH (clockwise direction).")

# Step delay (adjust speed by changing this value)
step_delay = 0.001  # 1 ms

print("DEBUG: Starting step loop. Press Ctrl+C to exit.")

try:
    step_count = 0
    while True:
        # Toggle the step pin HIGH then LOW
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(step_delay)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(step_delay)

        step_count += 1

        # Print an update every 200 steps (one revolution for many 1.8°/step motors)
        if step_count % 200 == 0:
            print(f"DEBUG: Completed {step_count} steps.")

except KeyboardInterrupt:
    print("\nDEBUG: Motor Test Interrupted by user (Ctrl+C).")

finally:
    print("DEBUG: Cleaning up GPIO pins...")
    GPIO.cleanup()
    print("========== Motor Test Ended ==========")
