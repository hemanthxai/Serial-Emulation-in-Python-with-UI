import serial
import time
import random

def create_random_temperature():
    return f"{random.randint(20, 40)}°C"

def main():
    with serial.Serial('/dev/ttyS1', baudrate=9600, timeout=1) as ser:  # Adjust port as needed
        while True:
            temperature = create_random_temperature()
            ser.write(temperature.encode())
            time.sleep(1)  # Send data every second

if __name__ == "__main__":
    main()
