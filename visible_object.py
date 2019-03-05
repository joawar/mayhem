import pygame

class Visible_Object(pygame.sprite.Sprite):
    visible_object_group = pygame.sprite.Group()
    def __init__(self, pos, image):
        super().__init__()
        self.pos = pos
        self.visible_object_group.add(self)
        self.image = self.original_image = image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
    
    def update(self):
        raise Exception("update has not been implemented yet")