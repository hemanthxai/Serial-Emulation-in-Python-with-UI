from collections import deque
import random


sensor_queue = deque()


def temp():
    value = random.uniform(15.0, 30.0)
    sensor_queue.appendleft(("Temperature", value))


def pres():
    value = random.uniform(950.0, 1050.0)
    sensor_queue.appendleft(("Pressure", value))


def retrieve_value():

    print(sensor_queue.pop())


print(sensor_queue)

temp()
pres()
temp()
pres()
# temp()


print(sensor_queue)

retrieve_value()
retrieve_value()
# retrieve_value()
# retrieve_value()
# retrieve_value()


print(sensor_queue)
