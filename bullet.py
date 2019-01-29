from moving_object import Moving_Object
from precode2 import *
from config import *

class Bullet(Moving_Object):
    """Initialize bullet object
    
    Arguments:
        screen -- Surface
        pos -- position
        direction -- normalized direction vector
    """
    bullet_list = []
    def __init__(self, screen, pos, direction, radius):
        super().__init__(screen, pos, direction * BULLET_SPEED, BULLET_COLOR)
        self.radius = BULLET_RADIUS
        self.bullet_list.append(self)

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius)