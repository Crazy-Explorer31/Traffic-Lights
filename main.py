from emulator import Emulator
from traffic_light import TrafficLight
import roads_workload_generators
import light_functions

set_delay = 70
set_light_function = light_functions.classic_traffic_light_function

set_traffic_generator_intensity = 0.15
set_traffic_generator_intensity_weights = [100, 100, 100, 100]

set_traffic_generator = roads_workload_generators.get_weighted_generator_single_arrives(
    set_traffic_generator_intensity_weights,
    set_traffic_generator_intensity
)

set_finish_time = 10_000


def main():

    roads_workload = [0, 0, 0, 0]

    light_function = light_functions.load_nn_light_function(
        model_path="model/model.pkl",
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
        set_visualization_enabled=True
    )

    simple_emulator.emulate()


if __name__ == "__main__":
    main()
