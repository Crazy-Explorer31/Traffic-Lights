from car import Car
import time


class Emulator:
    def __init__(
        self,
        roads_workload,
        traffic_light,
        traffic_generator,
        finish_time=120,
        seconds_for_sleep=0,
    ):
        self.roads_workload = roads_workload
        self.traffic_light = traffic_light
        self.traffic_generator = traffic_generator
        self.finish_time = finish_time
        self.current_time = 0
        self.seconds_for_sleep = seconds_for_sleep
        self.cars_coordinates = {"left": [], "up": [], "right": [], "down": []}
        self.car_radius = 20
        self.car_velocity = 5

    def show_state(self):
        print(f"current time: {self.current_time}")
        print(f"roads_workload: {self.roads_workload}")
        print(f"lights: {self.traffic_light.current_lights}")
        print()

    def update_cars_coordinates(self, new_cars):
        for car_index in range(len(self.cars_coordinates)):
            car = self.cars_coordinates[car_index]
            if car.x > 1200 or car.y > 1200:
                del self.cars_coordinates[car_index]

        if new_cars[0] == 1 and self.cars_coordinates["left"][-1].x != self.car_radius:
            self.cars_coordinates["left"].append(
                Car("left", self.car_velocity, self.car_radius)
            )
        if new_cars[1] == 1 and self.cars_coordinates["up"][-1].y != self.car_radius:
            self.cars_coordinates["up"].append(
                Car("up", self.car_velocity, self.car_radius)
            )
        if (
            new_cars[2] == 1
            and self.cars_coordinates["right"][-1].x != 1200 - self.car_radius
        ):
            self.cars_coordinates["right"].append(
                Car("right", self.car_velocity, self.car_radius)
            )
        if (
            new_cars[3] == 1
            and self.cars_coordinates["down"][-1].y != 1200 - self.car_radius
        ):
            self.cars_coordinates["down"].append(
                Car("down", self.car_velocity, self.car_radius)
            )

    def move_car_simple(self, direction, car_index):
        car = self.cars_coordinates[direction][car_index]
        if car_index == 0:
            if direction == "left":
                if self.traffic_light.current_lights[0] and not (
                    self.traffic_light.delaying_mode
                ):
                    self.cars_coordinates["left"][car_index].do_motion()
                elif car.x != 400 - self.car_radius:
                    self.cars_coordinates["left"][car_index].do_motion()

            elif direction == "up":
                if self.traffic_light.current_lights[1] and not (
                    self.traffic_light.delaying_mode
                ):
                    self.cars_coordinates["up"][car_index].do_motion()
                elif car.y != 400 - self.car_radius:
                    self.cars_coordinates["up"][car_index].do_motion()

            elif direction == "right":
                if self.traffic_light.current_lights[2] and not (
                    self.traffic_light.delaying_mode
                ):
                    self.cars_coordinates["right"][car_index].do_motion()
                elif car.x != 800 + self.car_radius:
                    self.cars_coordinates["right"][car_index].do_motion()

            elif direction == "down":
                if self.traffic_light.current_lights[3] and not (
                    self.traffic_light.delaying_mode
                ):
                    self.cars_coordinates["down"][car_index].do_motion()
                elif car.y != 800 + self.car_radius:
                    self.cars_coordinates["down"][car_index].do_motion()

    def move_car(self, direction, car_index):
        car = self.cars_coordinates[direction][car_index]
        if car_index == 0:
            self.move_car_simple(self, direction, car_index)
        else:
            if (
                car.x + car.motion_vector[0]
                != self.cars_coordinates[direction][car_index - 1].x
                and car.y + car.motion_vector[1]
                != self.cars_coordinates[direction][car_index - 1].y
            ):
                self.move_car_simple(self, direction, car_index)

    def do_global_move(self):
        for cars, direction in zip(
            self.cars_coordinates.values(), ["left", "up", "right", "down"]
        ):
            for car_index in range(len(cars)):
                self.move_car(self, direction, car_index)

    def emulate(self):
        while self.current_time < self.finish_time:
            new_cars = self.traffic_generator()
            self.update_cars_coordinates(new_cars)

            for r in range(4):
                self.roads_workload[r] += new_cars[r]

            self.traffic_light.update_lights(self.current_time)

            # for i in range(4):
            #     if self.traffic_light.current_lights[i] == 1:
            #         if self.roads_workload[i] > 0:
            #             self.roads_workload[i] -= 1

            self.do_global_move()

            self.show_state()

            self.current_time += 1

            time.sleep(self.seconds_for_sleep)
