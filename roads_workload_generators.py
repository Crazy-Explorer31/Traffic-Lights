from random import randint


def random_generator():
    r1 = randint(0, 1)
    r2 = randint(0, 1)
    r3 = randint(0, 1)
    r4 = randint(0, 1)
    return [r1, r2, r3, r4]


def low_intensity_random_generator():
    r1 = randint(0, 4)
    r2 = randint(0, 4)
    r3 = randint(0, 4)
    r4 = randint(0, 4)
    return [r1 > 3, r2 > 3, r3 > 3, r4 > 3]


def weighted_generator(weights):
    return [randint(0, i) for i in weights]


def weighted_generator_single_arrives(weights, intensity=1):
    result = []

    weights_sum = sum(weights)

    for weight in weights:
        rand_number = randint(1, weights_sum)
        if rand_number <= weight * intensity:
            result.append(1)
        else:
            result.append(0)

    return result
