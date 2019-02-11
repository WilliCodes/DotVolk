from entity_sprite import EntitySprite


class Resource(EntitySprite):

    def __init__(self, pos):
        super(Resource, self).__init__(pos)
        self.workers = {}
        self._amount = 10

    @property
    def amount(self):
        return self._amount

    def harvest(self, amount):
        self._amount -= amount
        if self._amount <= 0:
            for w in self.workers.keys():
                w.task = None
            self.game.remove_entity(self)
