from precode2 import *

class Obstacle():
    def __init__(self, screen, pos, color, width, length):
        self.pos = pos
        self.color = color
        self.width = width
        self.length = length
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.pos.x, self.pos.y, self.width, self.height))