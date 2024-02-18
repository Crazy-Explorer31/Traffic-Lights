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

        self.light_changes_delay = delay
        self.time_to_next_change = 0

    def update_lights(self, current_time):
        if not self.delaying_mode:
            if self.time_to_next_change == 0:
                self.new_lights = self.light_function(current_time, period=60)
                if self.new_lights != self.current_lights:
                    self.time_to_change = self.delay
                    self.delaying_mode = True
            else:
                self.time_to_next_change -= 1

        else:
            if self.time_to_change == 0:
                self.current_lights = self.new_lights
                self.delaying_mode = False
                self.time_to_next_change = self.light_changes_delay
            else:
                self.time_to_change -= 1
