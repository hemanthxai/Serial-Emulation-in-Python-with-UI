import threading
import time


def task1():
    print("task one started", end=" ")
    time.sleep(2)
    print("task one completed", end=" ")


def task2():
    print("task two started..", end=" ")
    time.sleep(2)
    print("task two completed", end=" ")


def task3():
    print("task three started..", end=" ")
    time.sleep(2)
    print("task three completed", end=" ")


thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)


thread1.start()
thread2.start()

thread1.join()
thread2.join()


task3()
