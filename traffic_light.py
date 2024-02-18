class TrafficLight:  # TF below
    def __init__(self, roads_workload, delay, light_function):
        self.roads_workload = (
            roads_workload  # 4 numbers - left, up, right, down amount of cars
        )
        self.delay = delay  # time, during for that TF will be being switched
        self.light_function = light_function  # rule, by that switching will be executed
        self.current_lights = [0, 1, 0, 1]  # current condition of TF
        self.delaying_mode = False
        self.time_to_change = 0  # time to switching TF
        self.new_lights = [0, 0, 0, 0]

    def update_lights(self):
        if not self.delaying_mode:
            self.new_lights = self.light_function(self.roads_workload)
            if self.new_lights != self.current_lights:
                self.current_lights = [0, 0, 0, 0]
                self.time_to_change = self.delay
                self.delaying_mode = True

        else:
            if self.time_to_change == 0:
                self.current_lights = self.new_lights
                self.delaying_mode = False
            else:
                self.time_to_change -= 1
