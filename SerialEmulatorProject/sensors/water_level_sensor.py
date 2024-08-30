import serial
import random
import time

def generate_water_level_data():
    return f"{random.randint(1, 5)} meters"

def main():
    try:
        # Open the serial port
        ser = serial.Serial('/dev/pts/12', 9600, timeout=1)  # Update the path if necessary

        while True:
            # Generate and send data
            data = generate_water_level_data()
            ser.write(data.encode())
            print(f"Sent data: {data}")  # Log data being sent
            time.sleep(2)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
