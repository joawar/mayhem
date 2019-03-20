from visible_object import Visible_Object

class Obstacle(Visible_Object):
    def __init__(self, pos, image):
        super().__init__(pos, image)
        self.obstacle_group.add(self)