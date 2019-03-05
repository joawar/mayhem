from moving_object import Moving_Object
from vector import Vector2
from config import *

class Bullet(Moving_Object):
    bullet_list = []
    def __init__(self, pos, direction):
        super().__init__(pos, direction * BULLET_SPEED)
        self.radius = BULLET_RADIUS
        self.bullet_list.append(self)