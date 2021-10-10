import time


class TrafficLight:
    def __init__(self):
        self.__color = (('Red', 7), ('Yellow', 2), ('Green', 10))

    def running(self):
        for color, time_traffic_light in self.__color:
            print(f'{color}! wait ... {time_traffic_light} seconds')
            time.sleep(int(time_traffic_light))


traffic_light = TrafficLight()
while True:
    traffic_light.running()