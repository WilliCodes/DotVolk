from entity_sprite import EntitySprite


class Unit(EntitySprite):

    def __init__(self, pos):
        super(Unit, self).__init__(pos)
        self.target = None
