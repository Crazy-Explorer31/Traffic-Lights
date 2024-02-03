from traffic_light import TrafficLight


class Emulator:
    roads_workload: list[int]
    current_time: int
    finish_time: int
    traffic_light: TrafficLight

    def __init__(self, traffic_light, traffic_generator, roads, finish_time):
        self.roads = roads
        self.traffic_light = traffic_light
        self.traffic_generator = traffic_generator
        self.finish_time = finish_time
        self.current_time = 0

    def show_state(self):
        print(f"current time: {self.current_time}")
        print(f"roads: {self.roads}")
        print(f"lights: {self.traffic_light.lights}")
        print()

    def start(self):
        while self.current_time < self.finish_time:
            new_cars = self.traffic_generator()
            for r in range(4):
                self.roads[r] += new_cars[r]

            self.traffic_light.choose_lights(self.current_time)

            for i in range(4):
                if self.traffic_light.lights[i] == 1:
                    if self.roads[i] > 0:
                        self.roads[i] -= 1

            self.show_state()

            self.current_time += 1
