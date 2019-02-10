from building import Building
import pygame
import time
from resource import Resource


class Field(Resource):

    def __init__(self, pos, game):
        super(Field, self).__init__(pos)

        self.game = game

        self.image = pygame.image.load('./assets/field.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.surface = pygame.display.get_surface()

    def draw(self):
        self.surface.blit(self.image, self.rect)
