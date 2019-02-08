from entity import Entity
import pygame


class StatusBar(Entity):

    height = 10

    def __init__(self, height, game):
        super(StatusBar, self).__init__(height)

        surface = pygame.display.get_surface()
        self.rect = pygame.Rect((0, surface.get_height() - height),
                                (surface.get_width(), height))

        self.game = game
        self.game.control.append(self)

    def draw(self, surface):
        pygame.draw.rect(surface, (125, 125, 125), self.rect)
