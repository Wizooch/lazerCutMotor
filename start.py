#!/usr/bin/env python3

import serial
import serial.tools.list_ports
import time

BAUD_RATE = 115200

# Updated G-code lines to match your .nc file exactly
GCODE_COMMANDS = [
    "M3 S0",
    "S0 ",
    "G0X6.004Y0.533",
    "S1000 ",
    "G1X95.596F800",
    "G3X100.965Y5.902I0J5.369",
    "G1Y146.293",
    "G3X95.596Y151.663I-5.369J0",
    "G1X6.004",
    "G3X0.635Y146.293I0J-5.369",
    "G1Y5.902",
    "G3X6.004Y0.533I5.369J0",
    "G1",
    "S0 ",
    "M5 S0"
]

def find_laser_port():
    """
    Scan through all serial ports and return the first one
    that looks like a USB or ACM port (typical on Raspberry Pi for laser cutters/3D printers).
    Returns None if none are found or opened successfully.
    """
    ports = serial.tools.list_ports.comports()
    candidates = []

    # Gather candidate ports (common on Raspberry Pi for USB/ACM devices)
    for p in ports:
        # Typical Pi device names: /dev/ttyUSB0, /dev/ttyACM0
        if 'ttyUSB' in p.device or 'ttyACM' in p.device:
            candidates.append(p.device)

    # Try each candidate in turn
    for port_name in candidates:
        print(f"Trying port: {port_name}")
        try:
            ser = serial.Serial(port_name, BAUD_RATE, timeout=1)
            ser.close()
            print(f"Success opening {port_name} at {BAUD_RATE} baud.")
            return port_name
        except Exception as e:
            print(f"Failed to open {port_name}: {e}")

    return None

def send_gcode(port_name):
    """
    Send GCODE_COMMANDS to the specified port_name.
    """
    try:
        ser = serial.Serial(port_name, BAUD_RATE, timeout=1)
        time.sleep(2)  # wait for controller to initialize

        print(f"\nConnected to {port_name}. Sending G-code...")
        
        for cmd in GCODE_COMMANDS:
            full_cmd = cmd + "\n"
            ser.write(full_cmd.encode('utf-8'))
            response = ser.readline().decode('utf-8').strip()
            print(f"Sent: {cmd} | Received: {response}")
        
        ser.close()
        print("Done sending G-code. Port closed.\n")
    except serial.SerialException as e:
        print(f"Could not open serial port {port_name}: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    print("Searching for laser cutter serial port...")
    port = find_laser_port()
    if port:
        send_gcode(port)
    else:
        print("No suitable laser port found. Please check connections.")

if __name__ == "__main__":
    main()
