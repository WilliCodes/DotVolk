from unit import Unit
import pygame
import time


class Mercenary(Unit):

    build_time = 10
    cost = {"food": 20, "wood": 10, "stone": 0, "pop": 1}

    image_path = './assets/mercenary.png'
    name = 'Mercenary'

    initial_hp = 150
    hp_factor = 1
    hp_max = initial_hp * hp_factor

    velocity = 5

    def __init__(self, pos, game):
        super(Mercenary, self).__init__(pos)
        self.game = game
        self.hp = Mercenary.initial_hp * Mercenary.hp_factor

        self.image = pygame.image.load(Mercenary.image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

        self.surface = pygame.display.get_surface()

        self.task = None
        self.last_task_time = None

    def update(self):
        self.move()

    def draw(self):
        self.surface.blit(self.image, self.rect)

    def right_click(self, pos):
        self.target = pos
