def classic_traffic_light_function(t, period):
    if t % period > period / 2:
        return [1, 0, 1, 0]

    else:
        return [0, 1, 0, 1]
