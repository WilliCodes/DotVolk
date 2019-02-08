from entity import Entity
import pygame


class ProgressBar(Entity):

    height = 10

    def __init__(self, entity, game):
        super(ProgressBar, self).__init__(entity.rect.topleft)

        self.entity = entity

        self.rect = pygame.Rect((entity.rect.x, entity.rect.y - ProgressBar.height),
                                (0, ProgressBar.height))

        self.game = game
        self.game.drawings.append(self.rect)

    def update_progress_bar(self, progress):
        self.rect.width = progress * self.entity.rect.width
        if progress >= 1:
            self.game.drawings.remove(self.rect)


