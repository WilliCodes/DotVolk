from entity_sprite import EntitySprite
import math


class Unit(EntitySprite):

    def __init__(self, pos):
        super(Unit, self).__init__(pos)
        self.target = None

    def move(self):
        # target should be a Sprite, to walk towards moving Units
        if self.target is not None:
            vector = (self.target[0] - self.rect.center[0], self.target[1] - self.rect.center[1])
            v_len = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
            if v_len == 0:
                self.target = None
            elif v_len <= self.velocity:
                self.target = None
            else:
                vector = (self.velocity * vector[0] / v_len, self.velocity * vector[1] / v_len)

                self.rect.x += round(vector[0])
                self.rect.y += round(vector[1])

                if self.rect.center[0] == self.target[0] and self.rect.center[1] == self.target[1]:
                    self.target = None
