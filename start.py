#!/usr/bin/env python3

import serial
import serial.tools.list_ports
import time

BAUD_RATE = 115200

GCODE_COMMANDS = [
    "G90",             # Ensure absolute mode
    "G21",             # Ensure mm
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
    """ Find the first /dev/ttyUSB* or /dev/ttyACM* port. """
    ports = serial.tools.list_ports.comports()
    for p in ports:
        if 'ttyUSB' in p.device or 'ttyACM' in p.device:
            return p.device
    return None

def send_gcode(port_name):
    """ Send GCODE_COMMANDS to the specified port_name. """
    try:
        ser = serial.Serial(port_name, BAUD_RATE, timeout=1)
        
        # Give controller time to reset
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        time.sleep(3)  
        
        print(f"Connected to {port_name} at {BAUD_RATE}. Sending G-code...")

        # Optionally send homing or coordinate reset
        # ser.write(b"$H\n")
        # wait for homing response, or just sleep a bit
        # time.sleep(3)
        
        for cmd in GCODE_COMMANDS:
            line = cmd.strip() + "\n"
            ser.write(line.encode('utf-8'))
            ser.flush()
            
            # Wait for controller's response (like 'ok' or error message)
            response = ser.readline().decode('utf-8', errors='ignore').strip()
            print(f"Sent: {cmd} | Received: {response}")
            
            # short delay so we don't overwhelm the controller
            time.sleep(0.1)
        
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
