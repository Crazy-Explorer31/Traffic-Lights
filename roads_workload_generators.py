from random import randint


def get_random_generator(n=40):
    def random_generator():
        r1 = int(randint(0, n) == 0)
        r2 = int(randint(0, n) == 0)
        r3 = int(randint(0, n) == 0)
        r4 = int(randint(0, n) == 0)
        return [r1, r2, r3, r4]

    return random_generator


def get_weighted_generator(weights):
    def weighted_generator():
        return [randint(0, i) for i in weights]

    return weighted_generator


def get_weighted_generator_single_arrives(weights=[1, 1, 1, 1], intensity=1):
    def weighted_generator_single_arrives():
        result = []

        weights_sum = sum(weights)

        for weight in weights:
            rand_number = randint(1, weights_sum)
            if rand_number <= weight * intensity:
                result.append(1)
            else:
                result.append(0)

        return result

    return weighted_generator_single_arrives
