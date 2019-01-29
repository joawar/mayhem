from precode2 import *
from config import *
from visible_object import Visible_Object

class Moving_Object(Visible_Object):
    moving_object_list = []
    def __init__(self, screen, pos, velocity, color, acceleration = GRAVITY):
        super().__init__(pos)
        self.color = color
        self.velocity = velocity
        self.direction = velocity.normalized()
        self.acceleration = acceleration
        self.screen = screen
        self.moving_object_list.append(self)
        
    
    def border_hit_detection(self):
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()
        x = self.pos.x
        y = self.pos.y
        if x <= 0:
            self.die()
        if x >= screen_width:
            self.die()
        if y <= 0:
            self.die()
        if y >= screen_height:
            self.die()
    
    
    def jerk(self, jerk_power):
        self.acceleration += self.direction*jerk_power
        self.burn_fuel()
    
    def accelerate(self):
        self.velocity += self.acceleration
        if abs(self.velocity) > MAX_SPEED:
            self.velocity = self.velocity.normalized() * MAX_SPEED

    def move(self):
        self.pos += self.velocity
        print(abs(self.velocity))
        
    def draw(self):
        raise Exception("Not implemented yet")

    def rotate(self, angle):
        self.direction = self.direction.rotate(angle)
    
    def brake(self):
        self.acceleration -= self.velocity.normalized()*BRAKEFORCE
    
    def die(self):
        self.moving_object_list.remove(self)

    def burn_fuel(self):
        pass


