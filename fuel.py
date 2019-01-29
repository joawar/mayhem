from visible_object import Visible_Object

class Fuel(Visible_Object):
    def __init__(self, pos, color, size):
        super().__init__(pos)
        self.color = color
        self.size = size
    
    def draw(self):
        pass