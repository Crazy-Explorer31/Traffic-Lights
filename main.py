from emulator import Emulator
from traffic_light import TrafficLight
import roads_workload_generators
import light_functions

set_delay = 5
set_light_function = light_functions.classic_traffic_light_function
set_traffic_generator = roads_workload_generators.random_generator
set_finish_time = 120


def main():
    roads_workload = [0, 0, 0, 0]

    classic_traffic_light = TrafficLight(
        roads_workload=roads_workload,
        delay=set_delay,
        light_function=set_light_function,
    )

    simple_emulator = Emulator(
        roads_workload=roads_workload,
        traffic_light=classic_traffic_light,
        traffic_generator=set_traffic_generator,
        finish_time=set_finish_time,
    )

    simple_emulator.emulate()


main()
