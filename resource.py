from entity_sprite import EntitySprite


class Resource(EntitySprite):

    def __init__(self, pos):
        super(Resource, self).__init__(pos)
        self.workers = set()
        self._amount = 1000

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, change):
        self._amount -= change
        if self._amount <= 0:
            self.kill()
