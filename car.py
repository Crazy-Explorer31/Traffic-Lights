import pygame

class Car:
    def __init__(self, direction, velocity, radius = 20):
        self.is_in_field = True
        # self.color = color
        self.radius = radius
        self.direction = direction
        self.velocity = velocity
        if (direction == "down"): # движение сверху вниз
            self.x = 500
            self.y = radius
            self.motion_vector = [0, velocity]

        elif (direction == "up"): # движение снизу вверх
            self.x = 700
            self.y = 1200 - radius
            self.motion_vector = [0, -velocity]

        elif (direction == "right"): # движение слева направо
            self.x = radius
            self.y = 700
            self.motion_vector = [velocity, 0]

        elif (direction == "left"): # движение справа налево
            self.x = 1200 - radius
            self.y = 500
            self.motion_vector = [-velocity, 0]

        # тут тоже все для отслеживания коллизий
        self.image = pygame.Surface((40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y 

    def do_motion(self):
        self.x += self.motion_vector[0]
        self.y += self.motion_vector[1]
        # следующие 2 строчки нужны для отслеживания коллизий
        self.rect.x = self.x
        self.rect.y = self.y 

    def draw(self, surface) : # просто отрисовка
        pygame.draw.circle(surface, (self.x, self.y), self.radius)

# БЫЛО:
# class Car:
#     def __init__(self, appearance, velocity, radius=20):
#         self.is_in_field = True

#         if appearance == "up":
#             self.x = 500
#             self.y = radius
#             self.motion_vector = [0, velocity]
#         elif appearance == "down":
#             self.x = 700
#             self.y = 1200 - radius
#             self.motion_vector = [0, -velocity]
#         elif appearance == "left":
#             self.x = radius
#             self.y = 700
#             self.motion_vector = [velocity, 0]
#         elif appearance == "right":
#             self.x = 1200 - radius
#             self.y = 500
#             self.motion_vector = [-velocity, 0]

#     def do_motion(self):
#         self.x += self.motion_vector[0]
#         self.y += self.motion_vector[1]

