from car import Car
import time
import pygame
from traffic_light import TrafficLight

# actions for rendering

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1200, 1200))
pygame.display.set_caption("Traffic lights")
running = True
background = pygame.image.load("road.jpeg")

# end

direcion_to_int = {"left": 0, "up": 1, "right": 2, "down": 3}


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
        self.car_radius = 10
        self.car_velocity = 10

    def update_cars_coordinates(self, new_cars):
        for direction in self.cars_coordinates.keys():  # try to delete the heading car
            if len(self.cars_coordinates[direction]) > 0:
                car = self.cars_coordinates[direction][0]
                if (
                    car.x > 1200 or car.y > 1200 or car.x < 0 or car.y < 0
                ):  # TODO: 1200 -> FIELD_SIZE
                    del self.cars_coordinates[direction][0]

                    self.roads_workload[direcion_to_int[direction]] -= 1

        if new_cars[0] == 1 and (
            len(self.cars_coordinates["left"]) == 0
            or self.cars_coordinates["left"][-1].x > self.car_radius
        ):
            self.cars_coordinates["left"].append(
                Car("left", self.car_velocity, self.car_radius)
            )

        if new_cars[1] == 1 and (
            len(self.cars_coordinates["up"]) == 0
            or self.cars_coordinates["up"][-1].y > self.car_radius
        ):
            self.cars_coordinates["up"].append(
                Car("up", self.car_velocity, self.car_radius)
            )

        if new_cars[2] == 1 and (
            len(self.cars_coordinates["right"]) == 0
            or self.cars_coordinates["right"][-1].x < 1200 - self.car_radius
        ):
            self.cars_coordinates["right"].append(
                Car("right", self.car_velocity, self.car_radius)
            )

        if new_cars[3] == 1 and (
            len(self.cars_coordinates["down"]) == 0
            or self.cars_coordinates["down"][-1].y < 1200 - self.car_radius
        ):
            self.cars_coordinates["down"].append(
                Car("down", self.car_velocity, self.car_radius)
            )

    def move_car_simple(self, direction, car_index):
        car = self.cars_coordinates[direction][car_index]

        if direction == "left":
            if self.traffic_light.current_lights[0] and not (
                self.traffic_light.delaying_mode
            ):  # try not to check delaying mode
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
            self.move_car_simple(direction, car_index)
        else:
            next_car_coordinates = [
                self.cars_coordinates[direction][car_index - 1].x,
                self.cars_coordinates[direction][car_index - 1].y,
            ]
            new_current_car_coordinates = [
                car.x + car.motion_vector[0],
                car.y + car.motion_vector[1],
            ]
            if (
                abs(new_current_car_coordinates[0] - next_car_coordinates[0])
                + abs(new_current_car_coordinates[1] - next_car_coordinates[1])
                > 2 * self.car_radius
            ):
                self.move_car_simple(direction, car_index)

    def do_global_move(self):
        for cars, direction in zip(
            self.cars_coordinates.values(), self.cars_coordinates.keys()
        ):
            for car_index in range(len(cars)):
                self.move_car(direction, car_index)

    def draw_traffic_light(self, surface, location, color_int):
        if location == 0:
            (x, y, width, height) = (380, 598, 20, 200)

        elif location == 1:
            (x, y, width, height) = (400, 380, 200, 20)

        elif location == 2:
            (x, y, width, height) = (800, 401, 20, 200)

        elif location == 3:
            (x, y, width, height) = (600, 798, 200, 20)

        color = "Green" if color_int == 1 else "Red"

        if self.traffic_light.delaying_mode and color_int:
            color = "Yellow"

        pygame.draw.rect(surface, color, (x, y, width, height))

    def show_state(self):
        print(f"current time: {self.current_time}")
        print(f"road workload: {self.roads_workload}")
        print(f"lights: {self.traffic_light.current_lights}")
        print()

    def emulate(self):
        # Update of cars' condition

        new_cars = self.traffic_generator()
        self.update_cars_coordinates(new_cars)
        for r in range(4):
            self.roads_workload[r] += new_cars[r]

        self.do_global_move()  # move all cars

        self.traffic_light.update_lights(self.current_time)

        # Visualization

        screen.blit(background, (0, 0))  # updating screen

        for i in range(0, 4):  # drawing of traffic lights
            self.draw_traffic_light(screen, i, self.traffic_light.current_lights[i])

        for k in self.cars_coordinates.keys():  # drawing of cars
            for car in self.cars_coordinates[k]:
                car.draw(screen)

        # for k in self.cars_coordinates.keys(): # checking collisions (unlucky)
        #     for car in self.cars_coordinates[k]:
        #         for k in self.cars_coordinates.keys():
        #             for caar in self.cars_coordinates[k]:
        #                 if car!= caar and car.rect.colliderect(caar):
        #                     car.motion_vector[1] = 0
        #                     car.motion_vector[0] = 0
        #                     caar.motion_vector[0] = 0
        #                     caar.motion_vector[1] = 0

        # self.show_state()

        self.current_time += 1

        time.sleep(self.seconds_for_sleep)

        # time = (time + 1) % 80

        for event in pygame.event.get():  # to exit the program correctly
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        pygame.display.update()

        clock.tick(100)  # screen refresh rate
