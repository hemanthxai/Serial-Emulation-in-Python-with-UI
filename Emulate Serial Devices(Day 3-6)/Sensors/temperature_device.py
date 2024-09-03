import serial
import time
import random

def main():

    ser = serial.Serial('/dev/pts/5', 9600, timeout=1)
    while True:
        temperature = random.uniform(20,55)         
        ser.write(f"{temperature}\n".encode('utf-8'))
        time.sleep(0.5)
            

if __name__ == "__main__":
    main()
