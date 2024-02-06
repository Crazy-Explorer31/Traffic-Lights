def classic_traffic_light_function(t, period):
    if t % period > period / 2:
        return [1, 0, 1, 0]

    else:
        return [0, 1, 0, 1]


def choose_max_light_function(roads_workload):
    if roads_workload[0] + roads_workload[2] > roads_workload[1] + roads_workload[3]:
        return [1, 0, 1, 0]
    else:
        return [0, 1, 0, 1]
