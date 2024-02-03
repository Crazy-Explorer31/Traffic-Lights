class TrafficLight:
    roads_workload: list[int]  # 4 numbers - left, up, right, down amount of cars
    delay: int
    last_time_change: int

    def __init__(self, roads_workload, delay, light_function):
        self.roads_workload = roads_workload
        self.delay = delay
        self.light_function = light_function
        self.last_time_change = 0
        self.lights = [0, 0, 0, 0]

    def choose_lights(self, current_time):
        if current_time - self.delay > self.last_time_change:
            self.lights = self.light_function(current_time, period=60)
            self.last_time_change = current_time

