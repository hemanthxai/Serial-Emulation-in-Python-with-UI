import serial
import random
import time

def main():

    ser = serial.Serial('/dev/pts/7', 9600, timeout=1)
    while True:
        pressure= random.uniform(1000,2000)
            
        ser.write(f"{pressure}\n".encode('utf-8'))
        time.sleep(0.5)
            

if __name__ == "__main__":
    main()
