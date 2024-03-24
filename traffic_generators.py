from random import randint


def get_uniform_traffic_generator(n=20):
    def uniform_generator():
        r1 = int(randint(0, n) == 0)
        r2 = int(randint(0, n) == 0)
        r3 = int(randint(0, n) == 0)
        r4 = int(randint(0, n) == 0)
        return [r1, r2, r3, r4]

    return uniform_generator


def get_weighted_traffic_generator(weights=[1, 1, 1, 1], intensity=1):
    def weighted_traffic_generator():
        result = []

        weights_sum = sum(weights)

        for weight in weights:
            rand_number = randint(1, weights_sum)
            if rand_number <= weight * intensity:
                result.append(1)
            else:
                result.append(0)

        return result

    return weighted_traffic_generator
