from moving_object import Moving_Object
from vector import Vector2
from config import *
import pygame

class Bullet(Moving_Object):
    def __init__(self, pos, velocity):
        super().__init__(pos, velocity, BULLET_IMAGE)
        self.bullet_group.add(self)
    
    def update(self):
        angle = self.find_rotation_angle()
        self.rotate(angle)
        super().update()
    
    def find_rotation_angle(self):
        angle = self.direction.angle_to(self.velocity)
        return angle

if __name__ == '__main__':
    a = Vector2(0,-1)
    b = Vector2(-1,0)
    angle = a.angle_to(b)
    print(angle)
        