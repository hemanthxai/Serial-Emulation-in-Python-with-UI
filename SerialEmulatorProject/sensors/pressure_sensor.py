import serial
import time
import random

def create_random_pressure():
    return f"{random.randint(1000, 1040)} hPa"

def main():
    with serial.Serial('/dev/ttyS2', baudrate=9600, timeout=1) as ser:  # Adjust port as needed
        while True:
            pressure = create_random_pressure()
            ser.write(pressure.encode())
            time.sleep(1)  # Send data every second

if __name__ == "__main__":
    main()
