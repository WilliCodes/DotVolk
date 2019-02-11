from entity_sprite import EntitySprite
import pygame


class ProgressBar(EntitySprite):

    height = 10

    def __init__(self, entity, game):
        super(ProgressBar, self).__init__(entity.rect.topleft)

        self.entity = entity

        self.surface = pygame.display.get_surface()

        self.rect = pygame.Rect((entity.rect.x, entity.rect.y - ProgressBar.height),
                                (1, ProgressBar.height))

        self.game = game
        self.game.drawings.add(self)

    def update_progress_bar(self, progress):

        width = progress * self.entity.rect.width
        if width < 1:
            self.rect.width = 1
        else:
            self.rect.width = width

        if progress >= 1:
            self.kill()

    def draw(self):
        pygame.draw.rect(self.surface, (0, 255, 0), self.rect)
