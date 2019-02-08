from entity import Entity


class Unit(Entity):

    def __init__(self, pos):
        super(Unit, self).__init__(pos)
        self.target = None
