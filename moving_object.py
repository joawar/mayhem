from vector import copy_Vector2
from pygame import Vector2
from config import *
from visible_object import Visible_Object

class Moving_Object(Visible_Object):
    def __init__(self, pos, velocity, image):
        super().__init__(pos, image)
        self.velocity = velocity
        self.direction = velocity.normalize()
        self.acceleration = copy_Vector2(GRAVITY)
        self.alive = True
        self.moving_object_group.add(self)
        self.rotate()
        
    def update(self):
        self.detect_border_hit()
        self.accelerate()
        self.move()

    def detect_border_hit(self):
        if self.pos.x <= 0:
            self.kill()
        if self.pos.x >= SCREEN_WIDTH:
            self.kill()
        if self.pos.y <= 0:
            self.kill()
        if self.pos.y >= SCREEN_HEIGHT:
            self.kill()
    
    def accelerate(self):
        self.velocity += self.acceleration
        if self.velocity.length() > MAX_SPEED:
            self.velocity = self.velocity.normalize() * MAX_SPEED

    def move(self):
        self.pos += self.velocity
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        self.center.x = self.rect.x + self.rect.width/2
        self.center.y = self.rect.y + self.rect.height/2

    def rotate(self, angle = 0):
        self.direction = self.direction.rotate(angle)
        new_angle = self.direction.angle_to(Vector2(0,-1))
        self.image = pygame.transform.rotate(self.original_image, new_angle)

    def burn_fuel(self):
        raise Exception("burn_fuel has not been implemented")