import pygame

class MyCar():
    def init(self, direction, color, velocity, radius = 20):
        self.is_in_field = True
        self.color = color
        self.radius = radius
        self.direction = direction
        self.velocity = velocity
        if (direction == "down"):
            self.x = 500
            self.y = radius
            self.motion_vector = [0, velocity]
        elif (direction == "up"):
            self.x = 700
            self.y = 1200 - radius
            self.motion_vector = [0, -velocity] 
        elif (direction == "right"):
            self.x = radius
            self.y = 700
            self.motion_vector = [velocity, 0]
        elif (direction == "left"):
            self.x = 1200 - radius
            self.y = 500
            self.motion_vector = [-velocity, 0]
        self.image = pygame.Surface((40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y 
    def do_motion(self):
        self.x += self.motion_vector[0]
        self.y += self.motion_vector[1]
        # self.x = (self.x + self.motion_vector[0])%1200
        # self.y = (self.y + self.motion_vector[1])%1200
        self.rect.x = self.x
        self.rect.y = self.y 

    def draw(self, surface) :
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)


class TrafficLights:
    def init (self, x, y, w, h, color):
        self.color = color
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def change_color(self):
        if (self.color == 'Red'):
            self.color = 'Green'
        else:
            self.color = 'Red'
    def draw(self, surface) :
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.w, self.h))

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1200,1200))
pygame.display.set_caption("Traffic lights")
running = True
background = pygame.image.load('images/road.jpeg')

my_car_1 = MyCar("up", 'Blue', 15)
my_car_2 = MyCar("down", 'Blue', 25)
my_car_3 = MyCar("right", 'Blue', 35)
my_car_4 = MyCar("left", 'Blue', 25)

x = 0
time = 0
upper_light = TrafficLights(401,380,200,20, 'Green')
lower_light = TrafficLights(601,800,200,20, 'Green')
left_light = TrafficLights(380,600,20,200, 'Red')
right_light = TrafficLights(800,400,20,200, 'Red')
lights = [upper_light, right_light, lower_light, left_light]
cars = [
    my_car_1,
    my_car_2, 
    my_car_3,
    my_car_4
    ]
while running:
    screen.blit(background, (0,0))
    for light in lights:
        light.draw(screen)
        if time == 40:
            light.change_color()

    for car in cars:
        car.draw(screen)
        if  (car.direction == "down" and (lights[0].color == 'Green' or car.y < 360 or car.y > 380)) or \
            (car.direction == "left" and (lights[1].color == 'Green' or car.x < 802 or car.x > 840)) or \
            (car.direction == "up" and (lights[2].color == 'Green' or car.y < 802 or car.y > 850)) or \
            (car.direction == "right" and (lights[3].color == 'Green' or car.x < 360 or car.x > 380)):
            
            car.do_motion()

        for car in cars:
            for caaaar in cars:
                if car!= caaaar and car.rect.colliderect(caaaar):
                    car.motion_vector[1] = 0
                    caaaar.motion_vector[0] = 0
                    
    time = (time + 1) % 80

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    pygame.display.update()
    
    clock.tick(20)