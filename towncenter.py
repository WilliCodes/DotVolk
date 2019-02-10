from building import Building
import pygame
import worker
from queueable import Queueable


class Towncenter(Building):
    
    def __init__(self, pos, game):
        super(Towncenter, self).__init__(pos)

        self.image = pygame.image.load('./assets/towncenter.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

        self.surface = pygame.display.get_surface()

        self.game = game

        self.queue = []

        self.queueable = [worker.Worker]

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
