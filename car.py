import pygame

class Car:
    def __init__(self, direction, velocity, radius = 20):
        self.is_in_field = True
        # self.color = color
        self.radius = radius
        self.direction = direction
        self.velocity = velocity
        if (direction == "up"): # movement from top to bottom
            self.x = 500
            self.y = radius
            self.motion_vector = [0, velocity]

        elif (direction == "down"): # movement from bottom to top
            self.x = 700
            self.y = 1200 - radius
            self.motion_vector = [0, -velocity]

        elif (direction == "left"): # movement from left to right
            self.x = radius
            self.y = 700
            self.motion_vector = [velocity, 0]

        elif (direction == "right"): # movement from right to left
            self.x = 1200 - radius
            self.y = 500
            self.motion_vector = [-velocity, 0]

        # everything for collision tracking
        self.image = pygame.Surface((40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y 

    def do_motion(self):
        self.x += self.motion_vector[0]
        self.y += self.motion_vector[1]
        # for collision tracking
        self.rect.x = self.x
        self.rect.y = self.y 

    def draw(self, surface) : # just for rendering
        pygame.draw.circle(surface, (0, 200, 64),[self.x, self.y], self.radius)
