from vector import copy_Vector2
from pygame import Vector2
from config import *
from visible_object import Visible_Object

class Moving_Object(Visible_Object):
    moving_object_group = pygame.sprite.Group()
    def __init__(self, pos, velocity, color, image, acceleration = Vector2(0,0)):
        super().__init__(pos, image)
        self.color = color
        self.velocity = velocity
        self.direction = velocity.normalize()
        self.acceleration = copy_Vector2(GRAVITY)
        self.alive = True
        self.moving_object_group.add(self)
        
    def update(self):
        self.border_hit_detection()
        self.accelerate()
        self.move()
    
    def border_hit_detection(self):
        x = self.pos.x
        y = self.pos.y
        if x <= 0:
            self.kill()
        if x >= SCREEN_WIDTH:
            self.kill()
        if y <= 0:
            self.kill()
        if y >= SCREEN_HEIGHT:
            self.kill()
    
    def accelerate(self):
        self.velocity += self.acceleration
        if self.velocity.length() > MAX_SPEED:
            self.velocity = self.velocity.normalize() * MAX_SPEED

    def move(self):
        self.pos += self.velocity
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

    def rotate(self, angle = 0):
        self.direction = self.direction.rotate(angle)
        new_angle = self.direction.angle_to(Vector2(0,-1))
        self.image = pygame.transform.rotate(self.original_image, new_angle)

    def burn_fuel(self):
        raise Exception("burn_fuel has not been implemented")