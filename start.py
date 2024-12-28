import serial
import time

# Update the serial port and baud rate according to your laser cutter.
# Common baud rates: 115200, 230400. 
# Common device names: /dev/ttyACM0 or /dev/ttyUSB0
SERIAL_PORT = "/dev/ttyACM0"  
BAUD_RATE = 115200

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
    try:
        # Open serial port
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        
        # Give the connection a second to wake up
        time.sleep(2)

        # Send each G-code line
        for cmd in gcode_commands:
            full_cmd = cmd + "\n"
            ser.write(full_cmd.encode('utf-8'))
            response = ser.readline().decode('utf-8').strip()
            print(f"Sent: {cmd}, Received: {response}")

        # Close the serial connection
        ser.close()

    except serial.SerialException as e:
        print(f"Could not open serial port {SERIAL_PORT}: {e}")

if __name__ == "__main__":
    main()
