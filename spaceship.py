from config import *
from precode2 import *
from moving_object import Moving_Object
from bullet import Bullet

class Spaceship(Moving_Object):
    def __init__(self, screen, pos, velocity, fuel, color):
        super().__init__(screen, pos, velocity, color)
        self.fuel = fuel
        self.time_spent_dead = 0
    
    def burn_fuel(self):
        if self.alive:
            self.fuel -= FUEL_CONSUMPTION

    def draw(self):
        self.point1 = self.pos
        self.point2 = self.pos + self.direction.rotate(180 + SPACESHIP_ANGLE)*SPACESHIP_SIZE
        self.point3 = self.pos + self.direction.rotate(180 - SPACESHIP_ANGLE)*SPACESHIP_SIZE
        pygame.draw.polygon(self.screen, self.color, [[self.point1.x, self.point1.y], 
                                                      [self.point2.x, self.point2.y], 
                                                      [self.point3.x, self.point3.y]])
    
    def fire(self):
        if self.alive:
            bullet = Bullet(self.screen, self.pos, self.direction)
    
    def respawn(self):
        self.alive = True
        self.fuel = START_FUEL
        self.moving_object_list.append(self)
