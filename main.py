from emulator import Emulator, TrafficLight
from random_generator import random_generator
from classic_traffic_light_function import classic_traffic_light_function

roads = [0, 0, 0, 0]

classic_traffic_light = TrafficLight(
    roads_workload=roads,
    delay=5,
    light_function=classic_traffic_light_function
)

simple_emulator = Emulator(
    roads=roads,
    traffic_light=classic_traffic_light,
    traffic_generator=random_generator,
    finish_time=120
)

simple_emulator.start()
