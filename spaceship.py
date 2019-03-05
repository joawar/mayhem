from config import *
from vector import copy_Vector2
from pygame import Vector2
from moving_object import Moving_Object
from bullet import Bullet

class Spaceship(Moving_Object):
    def __init__(self,  pos, velocity, fuel, controls, image, name):
        super().__init__(pos, velocity, image)
        self.fuel = fuel
        self.time_spent_dead = 0
        self.controls = controls
        self.name = name
        self.time_since_last_shot = 0
    
    def update(self):
        self.acceleration = copy_Vector2(GRAVITY)
        self.handle_inputs()
        super().update()

    def handle_inputs(self):
        inputs = pygame.key.get_pressed()
        rotate_clockwise = inputs[self.controls[0]]
        rotate_counterclockwise = inputs[self.controls[1]]
        thrust = inputs[self.controls[2]]
        reverse = inputs[self.controls[3]]
        if rotate_clockwise:
            self.rotate(ANGULAR_SPEED)
        if rotate_counterclockwise:
            self.rotate(-ANGULAR_SPEED)
        if thrust:
            self.thrust()
        if reverse:
            self.reverse()

    def thrust(self):
        self.acceleration += self.direction*THRUST_STRENGTH
        self.burn_fuel()

    def burn_fuel(self):
        if self.alive:
            self.fuel -= FUEL_CONSUMPTION

    def reverse(self):
        self.acceleration -= self.direction*REVERSE_STRENGTH
    
    def shoot(self):
        if self.alive:
            bullet = Bullet(self.pos, self.direction)
    
    def respawn(self):
        self.alive = True
        self.fuel = START_FUEL
        self.moving_object_list.append(self)
