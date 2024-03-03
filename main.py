from emulator import Emulator
from traffic_light import TrafficLight
import roads_workload_generators
import light_functions


set_delay = 5
set_light_function = light_functions.choose_max_light_function
set_traffic_generator = roads_workload_generators.low_intensity_random_generator
set_finish_time = 1000


def main():

    roads_workload = [0, 0, 0, 0]

    light_function = light_functions.load_nn_light_function(
        model_path="model/model2.pkl",
        config_path="model/model-config"
    )

    classic_traffic_light = TrafficLight(
        roads_workload=roads_workload,
        delay=set_delay,
        light_function=light_function,
    )

    simple_emulator = Emulator(
        roads_workload=roads_workload,
        traffic_light=classic_traffic_light,
        traffic_generator=set_traffic_generator,
        finish_time=set_finish_time,
    )

    simple_emulator.emulate(show_stats=True)
    print(roads_workload, sum(roads_workload))


if __name__ == "__main__":
    main()
