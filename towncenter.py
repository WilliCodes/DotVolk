from building import Building
import pygame
import time
from worker import Worker
from progress_bar import ProgressBar

class Towncenter(Building):
    
    def __init__(self, pos):
        super(Towncenter, self).__init__(pos)

        self.image = pygame.image.load('./assets/towncenter.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

        self.queue = []

    def queue_worker(self, game):
        worker = WorkerInQueue(game, self)
        if worker.valid:
            self.queue.append(worker)

    def update(self):
        if len(self.queue) > 0:
            if self.queue[0].progress():
                del self.queue[0]


class WorkerInQueue:

    def __init__(self, game, tc):
        self.game = game
        self.valid = self.valid_check()
        if self.valid:
            self.buy()
            self.game = game
            self.tc = tc
            self.start_time = None
            self.end_time = None
            self.pos = self.tc.rect.center
            self.progress_bar = None

    def progress(self):
        if self.start_time is None:
            self.start_time = time.time()
            self.end_time = self.start_time + 5
            self.progress_bar = ProgressBar(self.tc, self.game)

        progress = (time.time() - self.start_time) / (self.end_time - self.start_time)
        self.progress_bar.update_progress_bar(progress)
        if progress >= 1:
            self.game.place_worker(self.pos)
            return True

    def valid_check(self):
        if self.game.food >= 10 and self.game.population + 1 <= self.game.population_limit:
            return True

    def buy(self):
        self.game.food -= 10
        self.game.population += 1

