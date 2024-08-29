import serial
import time
import random

def create_random_water_level():
    return f"{random.randint(0, 20)} meters"

def main():
    with serial.Serial('/dev/ttyS3', baudrate=9600, timeout=1) as ser:  # Adjust port as needed
        while True:
            water_level = create_random_water_level()
            ser.write(water_level.encode())
            time.sleep(1)  # Send data every second

if __name__ == "__main__":
    main()
