from control_sprite import ControlSprite
import pygame.freetype

class InfoDisplay(ControlSprite):

    def __init__(self, game):
        super(InfoDisplay, self).__init__()
        self.game = game
        self.entity = None
        self.buttons = []

    def focus(self, entity):
        self.entity = entity

    def hide(self):
        self.entity = None

    def button(self, text, x, y, width, height):
        font = pygame.freetype.SysFont('Consolas', 15)
        