from entity_sprite import EntitySprite


class Building(EntitySprite):

    queueable = []

    def __init__(self, pos):
        super(Building, self).__init__(pos)

        self.queue = []

    def on_build(self):
        pass

    def on_destroy(self):
        pass
