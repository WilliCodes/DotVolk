from building import Building
import pygame
import time
import progress_bar
import worker


class BuildingInProgress(Building):

    def __init__(self, pos, building, game):
        super(BuildingInProgress, self).__init__(pos)

        self.building = building

        self.name = building.name
        self.cost = building.cost
        self.build_time = building.build_time

        self.hp = 0
        self.hp_max = building.hp_max

        self.image = pygame.image.load(building.image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

        self.surface = pygame.display.get_surface()

        self.game = game

        self.progress_bar = progress_bar.ProgressBar(self, self.game)

        self.workers = {}
        self.progress_seconds = 0

    def draw(self):
        pygame.draw.rect(self.surface, (125, 125, 125), self.rect)

    def update(self):

        # which workers are currently on the building?
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

        # add workers that just entered the building to the active workers, with time of entering
        for w in current_workers:
            if w not in self.workers and len(self.workers) < 5 and (w.task is self or w.task is None):
                if w.task is None:
                    w.task = self
                self.workers[w] = time.time()

        # add worked time to progress and reset time
        for w, t in self.workers.items():
            self.progress_seconds += time.time() - t
            self.workers[w] = time.time()

        progress = self.progress_seconds / self.build_time
        self.progress_bar.update_progress_bar(progress)
        if progress >= 1:
            for w in self.workers.keys():
                w.task = None
            self.game.place_entity(self.building, self.rect.topleft)
            self.game.remove_entity(self)

    def check_resources(self):
        cost = self.cost
        if cost["food"] > self.game.food or cost["wood"] > self.game.wood or cost["stone"] > self.game.stone or self.game.population + cost["pop"] > self.game.population_limit:
            return False
        return True

    def check_collision(self):
        collisions = pygame.sprite.spritecollide(self, self.game.entities, False)
        if len(collisions) > 0:
            return False
        return True

    def buy(self):
        cost = self.cost
        self.game.food -= cost["food"]
        self.game.wood -= cost["wood"]
        self.game.stone -= cost["stone"]
        self.game.population += cost["pop"]

    @staticmethod
    def try_build(pos, building, game):

        obj = BuildingInProgress(pos, building, game)
        if not obj.check_resources() or not obj.check_collision():
            obj.progress_bar.kill()
            return None
        obj.buy()
        game.add_entity(obj)
        return True
