import pygame
from pygame import Vector2

class Visible_Object(pygame.sprite.Sprite):
    visible_object_group = pygame.sprite.Group()
    moving_object_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    spaceship_group = pygame.sprite.Group()
    obstacle_group = pygame.sprite.Group()
    def __init__(self, pos, image):
        super().__init__()
        self.pos = pos
        self.visible_object_group.add(self)
        self.image = self.original_image = image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        center_x = self.rect.x + self.rect.width/2
        center_y = self.rect.y + self.rect.height/2
        self.center = Vector2(center_x, center_y)

    
    def update(self):
        raise Exception("update has not been implemented yet")