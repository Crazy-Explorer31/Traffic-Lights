from emulator import Emulator
from traffic_light import TrafficLight
import roads_workload_generators
import light_functions
import pickle
import neat
import os.path

set_delay = 5
set_light_function = light_functions.choose_max_light_function
set_traffic_generator = roads_workload_generators.low_intensity_random_generator
set_finish_time = 1000


def main():

    with open("model/model.pkl", "rb") as f:
        genome = pickle.load(f)

    directory = os.path.dirname(__file__)
    config_path = os.path.join(directory, "model/model-config")
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)

    net = neat.nn.FeedForwardNetwork.create(genome, config)

    def light_function(roads_workload):
        output = net.activate(roads_workload)
        if output[0] > 0:
            return [1, 0, 1, 0]
        else:
            return [0, 1, 0, 1]

    roads_workload = [0, 0, 0, 0]

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
