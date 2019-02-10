from unit import Unit
import pygame
import math
from resource import Resource
from field import Field
import time


class Worker(Unit):

    build_time = 5
    cost = {"food": 10, "wood": 0, "stone": 0, "pop": 1}

    image_path = './assets/worker.png'
    name = 'Worker'

    initial_hp = 100
    hp_factor = 1

    def __init__(self, pos, game):
        super(Worker, self).__init__(pos)
        self.game = game
        self.hp = Worker.initial_hp * Worker.hp_factor
        self.hp_max = Worker.initial_hp * Worker.hp_factor

        self.image = pygame.image.load(Worker.image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

        self.surface = pygame.display.get_surface()

        self.task = None
        self.last_task_time = None

        self.velocity = 3

    def update(self):
        self.move()
        self.work()

    def draw(self):
        self.surface.blit(self.image, self.rect)

    def work(self):
        col = pygame.sprite.spritecollide(self, self.game.entities, False)
        on_resource = False
        for e in col:
            if isinstance(e, Resource):
                on_resource = True
                if self in e.workers:
                    if self.last_task_time + 1 <= time.time():
                        self.last_task_time = time.time()
                        e.amount = 1
                        if isinstance(e, Field):
                            self.game.food += 1
                elif len(e.workers) < 5:
                    e.workers.add(self)
                    self.task = e
                    self.last_task_time = time.time()
        if self.task is not None and not on_resource:
            self.task.workers.remove(self)
            self.task = None
            self.last_task_time = None

    def move(self):
        # target should be a Sprite, to walk towards moving Units
        if self.target is not None:
            vector = (self.target[0] - self.rect.center[0], self.target[1] - self.rect.center[1])
            v_len = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
            if v_len == 0:
                self.target = None
            elif v_len <= self.velocity:
                self.target = None
            else:
                vector = (self.velocity * vector[0] / v_len, self.velocity * vector[1] / v_len)

                self.rect.x += vector[0]
                self.rect.y += vector[1]

                if self.rect.center[0] == self.target[0] and self.rect.center[1] == self.target[1]:
                    self.target = None

    def right_click(self, pos):
        self.target = pos
