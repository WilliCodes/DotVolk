import time
from progress_bar import ProgressBar
from unit import Unit
from research import Research


class Queueable:

    def __init__(self, origin, to_queue, game):
        self.origin = origin
        self.to_queue = to_queue
        self.game = game

        self.start_time = None
        self.end_time = None
        self.build_time = to_queue.build_time
        self.pos = self.origin.rect.bottomright
        self.progress_bar = None

    def check_resources(self):
        cost = self.to_queue.cost
        if cost["food"] > self.game.food or cost["wood"] > self.game.wood or cost["stone"] > self.game.stone or self.game.population + cost["pop"] > self.game.population_limit:
            return False

        return True

    def buy(self):
        cost = self.to_queue.cost
        self.game.food -= cost["food"]
        self.game.wood -= cost["wood"]
        self.game.stone -= cost["stone"]
        self.game.population += cost["pop"]

    def progress(self):
        if self.start_time is None:
            self.start_time = time.time()
            self.end_time = self.start_time + self.build_time
            self.progress_bar = ProgressBar(self.origin, self.game)
        progress = (time.time() - self.start_time) / self.build_time
        self.progress_bar.update_progress_bar(progress)
        if progress >= 1:
            if issubclass(self.to_queue, Unit):
                self.game.place_entity(self.to_queue, self.pos)
            elif issubclass(self.to_queue, Research):
                self.game.apply_research(self.to_queue)
            return True

    @staticmethod
    def try_queue(origin, to_queue, game):
        obj = Queueable(origin, to_queue, game)
        if not obj.check_resources():
            return None
        obj.buy()
        return obj
