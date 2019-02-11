from building import Building
import pygame
import time
from resource import Resource


class Field(Resource):

    name = "Field"
    cost = {"food": 0, "wood": 30, "stone": 0, "pop": 0}
    build_time = 10

    initial_hp = 100
    hp_factor = 1
    hp_max = initial_hp * hp_factor

    image_path = './assets/field.png'

    def __init__(self, pos, game):
        super(Field, self).__init__(pos)

        self.game = game

        self.image = pygame.image.load(self.image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.surface = pygame.display.get_surface()

    def draw(self):
        self.surface.blit(self.image, self.rect)
