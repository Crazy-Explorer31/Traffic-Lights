class Car:
    def __init__(self, appearance, velocity, radius=20):
        self.is_in_field = True

        if appearance == "up":
            self.x = 500
            self.y = radius
            self.motion_vector = [0, velocity]
        elif appearance == "down":
            self.x = 700
            self.y = 1200 - radius
            self.motion_vector = [0, -velocity]
        elif appearance == "left":
            self.x = radius
            self.y = 700
            self.motion_vector = [velocity, 0]
        elif appearance == "right":
            self.x = 1200 - radius
            self.y = 500
            self.motion_vector = [-velocity, 0]

    def do_motion(self):
        self.x += self.motion_vector[0]
        self.y += self.motion_vector[1]
