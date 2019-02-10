from control_sprite import ControlSprite
import pygame.freetype
import building


class InfoDisplay(ControlSprite):

    def __init__(self, game):
        super(InfoDisplay, self).__init__()
        self.game = game
        self.entity = None
        self.buttons = {}
        self.font = pygame.freetype.SysFont('Consolas', 15)

        self.surface = pygame.display.get_surface()

        self.height = 200
        self.width = self.surface.get_width()

        self.x = 0
        self.y = self.surface.get_height() - self.height - 10 # 10: StatusBar height

    def focus(self, entity):
        self.entity = entity

    def hide(self):
        self.entity = None

    def button(self, text, x, y):
        surf, rect = self.font.render(text, color=(0, 0, 0))
        rect.x = x
        rect.y = y
        return (surf, rect)

    def draw(self):
        # Don't draw if nothing selected
        if self.entity is None:
            return

        # Skip non-buildings for now
        if not isinstance(self.entity, building.Building):
            return

        # Building selected
        if isinstance(self.entity, building.Building):
            self.draw_building()

    def draw_building(self,):
        rect = pygame.Rect((self.width, self.height), (self.x, self.y))
        pygame.draw.rect(self.surface, (100, 100, 100), rect)

        x = self.x
        y = self.y
        y_inc = self.font.get_sized_ascender()

        for q in self.entity.queueable:
            btn = self.button(q.name, x, y)
            self.buttons[q] = self.entity.append_to_queue
