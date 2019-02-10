from control_sprite import ControlSprite
import pygame
import pygame.freetype


class StatusBar(ControlSprite):

    height = 10

    def __init__(self, height, game):
        super(StatusBar, self).__init__()

        self.surface = pygame.display.get_surface()
        self.rect = pygame.Rect((0, self.surface.get_height() - height),
                                (self.surface.get_width(), height))

        self.game = game

    def draw(self):
        pygame.draw.rect(self.surface, (125, 125, 125), self.rect)

        font = pygame.freetype.SysFont('Consolas', 15)

        text = "Food: " + str(self.game.food) + "   Wood: " + str(self.game.wood) + "   Stone: " + str(self.game.stone)
        text += "      Population: " + str(self.game.population) + "/" + str(self.game.population_limit)

        font.render_to(self.surface, (10, self.rect.y + 5), text, (0, 0, 0))

