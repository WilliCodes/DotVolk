from control_sprite import ControlSprite
import pygame.freetype
import building
import unit


class InfoDisplay(ControlSprite):

    BTN_BUILD = "build"
    BTN_QUEUE = "queue"

    def __init__(self, game):
        super(InfoDisplay, self).__init__()

        self.game = game
        self.entities = None
        self.buttons = []

        self.font = pygame.freetype.SysFont('Consolas', 15)
        self.surface = pygame.display.get_surface()

        self.height = 200
        self.width = self.surface.get_width()
        self.x = 0
        self.y = self.surface.get_height() - self.height - 20  # 20: StatusBar height

        self.rect = pygame.Rect((self.x, self.y), (self.width, self.height))

        self.placing_building = None

    def left_click(self, pos, entities):

        if self.placing_building is not None:
            self.placing_building[0](self.placing_building[1], pos)
            self.placing_building = None

        if self.rect.collidepoint(pos):
            for rect, func, obj, btn_type in self.buttons:
                if rect.collidepoint(pos):
                    if btn_type == self.BTN_QUEUE:
                        func(obj)
                    if btn_type == self.BTN_BUILD:
                        self.placing_building = (func, obj)
        else:
            if entities is None or len(entities) == 0:
                self.entities = None
            self.entities = entities

        self.buttons = []

    def label(self, text, x, y):
        rect = self.font.get_rect(text)
        rect.x = x
        rect.y = y
        self.font.render_to(self.surface, (x, y), text)
        return rect

    def draw(self):
        # Don't draw if nothing selected
        if self.entities is None:
            return

        # single entity selected
        if len(self.entities) == 1:
            entity = self.entities[0]

            # Building selected
            if isinstance(entity, building.Building):
                self.draw_building(entity)

            # Unit selected
            if isinstance(entity, unit.Unit):
                self.draw_unit(entity)

    def draw_building(self, entity):

        pygame.draw.rect(self.surface, (150, 150, 150), self.rect)

        x = self.x + 20
        y = self.y + 20
        y_inc = self.font.get_sized_ascender() + 5

        self.buttons = []
        for q in entity.queueable:
            btn = self.label(q.name, x, y)
            self.buttons.append((btn, entity.append_to_queue, q, self.BTN_QUEUE))
            y += y_inc

        size = self.font.get_rect(entity.name)
        y = self.y + 50
        x = (self.width / 2) - (size.width / 2)
        self.label(entity.name, x, y)

        size = self.font.get_rect(str(entity.hp) + ' / ' + str(entity.hp_max))
        x = (self.width / 2) - (size.width / 2)
        y += 20
        self.label(str(entity.hp) + ' / ' + str(entity.hp_max), x, y)

        x = self.width * 0.75
        y = self.y + 20
        for q in entity.queue:
            self.label(q.to_queue.name, x, y)
            y += y_inc

    def draw_unit(self, entity):

        pygame.draw.rect(self.surface, (150, 150, 150), self.rect)

        x = self.x + 20
        y = self.y + 20
        y_inc = self.font.get_sized_ascender() + 5

        self.buttons = []
        for q in entity.buildable:
            btn = self.label(q.name, x, y)
            self.buttons.append((btn, entity.start_building, q, self.BTN_BUILD))
            y += y_inc

        size = self.font.get_rect(entity.name)
        y = self.y + 50
        x = (self.width / 2) - (size.width / 2)
        self.label(entity.name, x, y)

        size = self.font.get_rect(str(entity.hp) + ' / ' + str(entity.hp_max))
        x = (self.width / 2) - (size.width / 2)
        y += 20
        self.label(str(entity.hp) + ' / ' + str(entity.hp_max), x, y)
