import os.path
import neat
from emulator import Emulator
from traffic_light import TrafficLight
import traffic_generators
import pickle


set_traffic_generator_intensity = 0.15
set_traffic_generator_intensity_weights = [100, 100, 100, 100]

traffic_generator = traffic_generators.get_weighted_traffic_generator(
    set_traffic_generator_intensity_weights, set_traffic_generator_intensity
)


def eval_genomes(genomes, config):
    nets = []
    emulators = []
    genomes_list = []
    roads_to_emulators = []

    set_delay = 70
    set_finish_time = 10000

    part_time = set_finish_time / 100

    for genome_id, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)

        roads_to_emulators.append([0, 0, 0, 0])

        def light_function(roads_workload):
            output = net.activate(roads_workload)
            if output[0] > 0:
                return [1, 0, 1, 0]
            else:
                return [0, 1, 0, 1]

        traffic_light_sample = TrafficLight(
            roads_workload=roads_to_emulators[-1],
            delay=set_delay,
            light_function=light_function,
        )

        emulator_sample = Emulator(
            roads_workload=roads_to_emulators[-1],
            traffic_light=traffic_light_sample,
            traffic_generator=traffic_generator,
            finish_time=part_time,
            set_visualization_enabled=False,
        )

        emulators.append(emulator_sample)
        genomes_list.append(genome)

    for index, emulator in enumerate(emulators):
        for t in range(100):
            emulator.current_time = 0
            emulator.emulate()
            result = sum(roads_to_emulators[index])
            genomes_list[index].fitness += (
                30 - result
            ) / 30  # best_fitness, max = 1, min = -1


def run(config_file):

    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_file,
    )

    population = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    # population.add_reporter(neat.StdOutReporter(True))
    # stats = neat.StatisticsReporter()
    # population.add_reporter(stats)

    # Run for up to 100 generations.
    winner = population.run(eval_genomes, 1000)

    # show final stats
    # print('\nBest genome:\n{!s}'.format(winner))
    return winner


if __name__ == "__main__":
    directory = os.path.dirname(__file__)
    config_path = os.path.join(directory, "model-config")

    for t in range(100):
        winner = run(config_path)

        config = neat.config.Config(
            neat.DefaultGenome,
            neat.DefaultReproduction,
            neat.DefaultSpeciesSet,
            neat.DefaultStagnation,
            config_path,
        )

        network = neat.nn.FeedForwardNetwork.create(winner, config)
        roads = [0, 0, 0, 0]

        set_delay = 70
        set_finish_time = 1000

        def light_function(roads_workload):
            output = network.activate(roads_workload)
            # print(roads_workload, output)
            if output[0] > 0:
                return [1, 0, 1, 0]
            else:
                return [0, 1, 0, 1]

        traffic_light_sample = TrafficLight(
            roads_workload=roads,
            delay=set_delay,
            light_function=light_function,
        )

        emulator = Emulator(
            roads_workload=roads,
            traffic_light=traffic_light_sample,
            traffic_generator=traffic_generator,
            finish_time=set_finish_time,
            set_visualization_enabled=False,
        )
        emulator.emulate()
        print(sum(roads))

        if sum(roads) < 30:
            print(roads, sum(roads))
            with open("model.pkl", "wb") as f:
                pickle.dump(winner, f)
                f.close()
            break
