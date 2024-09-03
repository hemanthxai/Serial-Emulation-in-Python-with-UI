import serial
import random
import time

def main():

    ser = serial.Serial('/dev/pts/9', 9600, timeout=1)
    while True:
        waterlvl = random.uniform(0,5)
        ser.write(f"{waterlvl}\n".encode('utf-8'))


        time.sleep(2)
            

if __name__ == "__main__":
    main()
