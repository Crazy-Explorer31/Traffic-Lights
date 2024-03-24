from emulator import Emulator
from traffic_light import TrafficLight
import traffic_generators
import light_functions

set_delay = 70

# set_light_function = light_functions.get_periodic_light_function()

set_light_function = light_functions.get_nn_light_function(
    model_path="model/model.pkl", config_path="model/model-config"
)

# set_traffic_generator = roads_workload_generators.get_uniform_traffic_generator()

set_traffic_generator_weights = [400, 100, 400, 100]

set_traffic_generator_intensity = 0.15

set_traffic_generator = traffic_generators.get_weighted_traffic_generator(
    set_traffic_generator_weights, set_traffic_generator_intensity
)

set_finish_time = 10_000


def main():
    traffic_light = TrafficLight(
        delay=set_delay,
        light_function=set_light_function,
    )

    emulator = Emulator(
        traffic_light=traffic_light,
        traffic_generator=set_traffic_generator,
        finish_time=set_finish_time,
        set_visualization_enabled=True,
    )

    emulator.emulate(show_states=True)


if __name__ == "__main__":
    main()
