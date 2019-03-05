from visible_object import Visible_Object

class Obstacle(Visible_Object):
    def __init__(self, screen, pos, width, length, image):
        super().__init__(pos, image)
        self.pos = pos
        self.width = width
        self.length = length
        self.screen = screen