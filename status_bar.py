from entity import Entity
import pygame
import pygame.freetype


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

        font = pygame.freetype.SysFont('Consolas', 15)

        text = "Food: " + str(self.game.food) + "   Wood: " + str(self.game.wood) + "   Stone: " + str(self.game.stone)
        text += "      Population: " + str(self.game.population) + "/" + str(self.game.population_limit)

        font.render_to(surface, (10, self.rect.y + 5), text, (0, 0, 0))

