from traffic_light import TrafficLight


class Emulator:
    def __init__(self, traffic_light, traffic_generator, roads_workload, finish_time):
        self.roads_workload = roads_workload
        self.traffic_light = traffic_light
        self.traffic_generator = traffic_generator
        self.finish_time = finish_time
        self.current_time = 0

    def show_state(self):
        print(f"current time: {self.current_time}")
        print(f"roads_workload: {self.roads_workload}")
        print(f"lights: {self.traffic_light.current_lights}")
        print()

    def emulate(self):
        while self.current_time < self.finish_time:
            new_cars = self.traffic_generator()
            for r in range(4):
                self.roads_workload[r] += new_cars[r]

            self.traffic_light.update_lights(self.current_time)

            for i in range(4):
                if self.traffic_light.current_lights[i] == 1:
                    if self.roads_workload[i] > 0:
                        self.roads_workload[i] -= 1

            self.show_state()

            self.current_time += 1
