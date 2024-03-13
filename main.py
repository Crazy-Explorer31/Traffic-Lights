from emulator import Emulator
from traffic_light import TrafficLight
import roads_workload_generators
import light_functions

set_delay = 70
set_light_function = light_functions.classic_traffic_light_function

set_traffic_generator_n = 40
set_traffic_generator_intensity = 0.5
set_traffic_generator_intensity_weights = [1, 1, 1, 1]
# set_traffic_generator = roads_workload_generators.get_weighted_generator_single_arrives(
#     set_traffic_generator_intensity_weights,
#     set_traffic_generator_intensity
# )
set_traffic_generator = roads_workload_generators.get_random_generator(
    set_traffic_generator_n
)

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
    while True:
        simple_emulator.emulate()


main()
