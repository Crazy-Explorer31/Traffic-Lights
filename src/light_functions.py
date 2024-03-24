import pickle
import os
import neat


def get_periodic_light_function(period=120):
    def periodic_light_function(t):
        if t % period > period / 2:
            return [1, 0, 1, 0]

        else:
            return [0, 1, 0, 1]

    return periodic_light_function


def get_choose_max_light_function():
    def choose_max_light_function(roads_workload):
        if (
            roads_workload[0] + roads_workload[2]
            > roads_workload[1] + roads_workload[3]
        ):
            return [1, 0, 1, 0]
        else:
            return [0, 1, 0, 1]

    return choose_max_light_function


def get_nn_light_function(model_path, config_path):
    with open(model_path, "rb") as f:
        genome = pickle.load(f)

    directory = os.path.dirname(__file__)
    config_path = os.path.join(directory, config_path)
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path,
    )
    net = neat.nn.FeedForwardNetwork.create(genome, config)

    def nn_light_function(roads_workload):
        output = net.activate(roads_workload)
        if output[0] > 0:
            return [1, 0, 1, 0]
        else:
            return [0, 1, 0, 1]

    return nn_light_function
