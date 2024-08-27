class TemperatureError(Exception):

    pass


try:
    Temp = int(input())
    if Temp > 1000 or Temp < -1000:
        raise TemperatureError
except TemperatureError:
    print("Temperature must be between -1000°C and 1000°C")
else:
    print("Good Temperature")
