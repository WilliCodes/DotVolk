from building import Building
import pygame
import mercenary
from queueable import Queueable
import worker


class Towncenter(Building):

    initial_hp = 1000
    hp_factor = 1
    hp_max = initial_hp * hp_factor

    name = "Towncenter"
    cost = {"food": 0, "wood": 100, "stone": 50, "pop": 0}

    image_path = './assets/towncenter.png'

    build_time = 20

    queueable = [worker.Worker, mercenary.Mercenary]
    
    def __init__(self, pos, game):
        super(Towncenter, self).__init__(pos)

        self.image = pygame.image.load(self.image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

        self.surface = pygame.display.get_surface()

        self.game = game

        self.hp = Towncenter.initial_hp * Towncenter.hp_factor

        self.queue = []

    def append_to_queue(self, to_queue):
        if to_queue not in self.queueable:
            return
        new_obj = Queueable.try_queue(self, to_queue, self.game)

        if new_obj is not None:
            self.queue.append(new_obj)

    def update(self):
        if len(self.queue) > 0:
            if self.queue[0].progress():
                del self.queue[0]

    def draw(self):
        self.surface.blit(self.image, self.rect)

    def key_pressed(self, key):
        if key == 'w':
            self.append_to_queue(worker.Worker)

    def on_build(self):
        self.game.population_limit += 25

    def on_destroy(self):
        self.game.population_limit -= 25
