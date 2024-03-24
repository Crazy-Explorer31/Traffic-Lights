import pygame


class Painter:
    def __init__(self, visualization_enabled):
        self.visualization_enabled = visualization_enabled
        if visualization_enabled:
            pygame.init()
            self.clock = pygame.time.Clock()
            self.screen = pygame.display.set_mode((1200, 1200))
            self.background = pygame.image.load("../inc/road.jpeg")
            pygame.display.set_caption("Traffic lights")

    def draw_traffic_light(self, location, color):
        if location == 0:
            (x, y, width, height) = (380, 598, 20, 200)

        elif location == 1:
            (x, y, width, height) = (400, 380, 200, 20)

        elif location == 2:
            (x, y, width, height) = (800, 401, 20, 200)

        elif location == 3:
            (x, y, width, height) = (600, 798, 200, 20)

        pygame.draw.rect(self.screen, color, (x, y, width, height))

    def update_screen(self):
        self.screen.blit(self.background, (0, 0))

    def draw_car(self, location):
        location.draw(self.screen)

    def check_for_quit(self):
        for event in pygame.event.get():  # to exit the program correctly
            if event.type == pygame.QUIT:
                pygame.quit()

    def refresh_screen(self):
        pygame.display.update()
        self.clock.tick(100)  # screen refresh rate
