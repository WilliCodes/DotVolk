from building import Building
import pygame
import time
from resource import Resource
import worker


class Field(Resource):

    name = "Field"
    cost = {"food": 0, "wood": 30, "stone": 0, "pop": 0}
    build_time = 10

    initial_hp = 100
    hp_factor = 1
    hp_max = initial_hp * hp_factor

    image_path = './assets/field.png'

    def __init__(self, pos, game):
        super(Field, self).__init__(pos)

        self.game = game

        self.image = pygame.image.load(self.image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.surface = pygame.display.get_surface()

    def draw(self):
        self.surface.blit(self.image, self.rect)

    def update(self):

        # which workers are currently on the resource?
        current_workers = []
        collisions = pygame.sprite.spritecollide(self, self.game.units, False)
        for e in collisions:
            if type(e) == worker.Worker:
                current_workers.append(e)

        # remove workers that are no longer on the building or have a different task
        for w in list(self.workers):
            if w not in current_workers or w.task is not self:
                if w.task is self:
                    w.task = None
                del self.workers[w]

        if len(current_workers) == 0:
            return

        # add workers that just entered the resource to the active workers, with time of entering
        for w in current_workers:
            if w not in self.workers and len(self.workers) < 5 and (w.task is self or w.task is None):
                if w.task is None:
                    w.task = self
                self.workers[w] = time.time()

        # check if worker worked enough, reset time if yes
        for w, t in self.workers.items():
            if time.time() - t >= 1:
                self.harvest(1)
                self.game.food += 1
                self.workers[w] = time.time()
