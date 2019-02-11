import time

import pygame

import unit
import building_in_progress


class Worker(unit.Unit):

    build_time = 5
    cost = {"food": 10, "wood": 0, "stone": 0, "pop": 1}

    image_path = './assets/worker.png'
    name = 'Worker'

    initial_hp = 100
    hp_factor = 1
    hp_max = initial_hp * hp_factor

    velocity = 3

    buildable = []

    def __init__(self, pos, game):
        super(Worker, self).__init__(pos)
        self.game = game
        self.hp = Worker.initial_hp * Worker.hp_factor

        self.image = pygame.image.load(Worker.image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

        self.surface = pygame.display.get_surface()

        self.task = None
        self.last_task_time = None

    def update(self):
        self.move()

    def draw(self):
        self.surface.blit(self.image, self.rect)

    def start_building(self, to_build, pos):
        if to_build not in self.buildable:
            return
        new_obj = building_in_progress.BuildingInProgress.try_build(pos, to_build, self.game)

        if new_obj is not None:
            self.target = pos
