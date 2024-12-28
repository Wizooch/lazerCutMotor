import serial
import serial.tools.list_ports
import time

# -----------------------------
# 1) Enumerate all serial ports
# -----------------------------
print("Available serial ports:")
ports = serial.tools.list_ports.comports()
for p in ports:
    print(f"  {p.device} - {p.description}")

# ----------------------------------------------------------
# 2) Set the target port name and desired baud rate
#    On Windows, it might be "COM3"
#    On Raspberry Pi/Linux, try "/dev/ttyACM0" or "/dev/ttyUSB0"
# ----------------------------------------------------------
TARGET_PORT = "COM3"          # Example for Windows
# TARGET_PORT = "/dev/ttyACM0"  # Example for Raspberry Pi

BAUD_RATE = 115200

# ---------------------
# 3) Your G-code lines
# ---------------------
gcode_commands = [
    "M3 S0",
    "S0",
    "G0X6.004Y0.533",
    "S1000",
    "G1X95.596F800",
    "G3X100.965Y5.902I0J5.369",
    "G1Y146.293",
    "G3X95.596Y151.663I-5.369J0",
    "G1X6.004",
    "G3X0.635Y146.293I0J-5.369",
    "G1Y5.902",
    "G3X6.004Y0.533I5.369J0",
    "G1",
    "S0",
    "M5 S0"
]

def main():
    print(f"\nAttempting to connect to {TARGET_PORT} at {BAUD_RATE} baud...")

    try:
        # ----------------------------------
        # Open the serial port
        # ----------------------------------
        ser = serial.Serial(TARGET_PORT, BAUD_RATE, timeout=1)

        # Give the laser controller time to initialize
        time.sleep(2)

        print(f"Connected to {TARGET_PORT}.\nSending G-code...")

        # ----------------------------------
        # Send each G-code line
        # ----------------------------------
        for cmd in gcode_commands:
            full_cmd = cmd + "\n"
            ser.write(full_cmd.encode('utf-8'))
            # Read any response; some controllers echo or respond with 'ok', etc.
            response = ser.readline().decode('utf-8').strip()
            print(f"Sent: {cmd}, Received: {response}")

        # ----------------------------------
        # Close the port
        # ----------------------------------
        ser.close()
        print("\nDone sending G-code. Port closed.")

    except serial.SerialException as e:
        print(f"Error opening port {TARGET_PORT}: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
