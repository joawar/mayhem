import pygame

class Visible_Object(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos