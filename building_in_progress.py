from building import Building
import pygame
import time
import progress_bar


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

        self.start_time = time.time()
        self.end_time = self.start_time + self.build_time

        self.progress_bar = progress_bar.ProgressBar(self, self.game)

    def draw(self):
        pygame.draw.rect(self.surface, (125, 125, 125), self.rect)

        progress = (time.time() - self.start_time) / self.build_time
        self.progress_bar.update_progress_bar(progress)
        if progress >= 1:
            self.game.place_entity(self.building, self.rect.topleft)
            self.kill()

    def check_resources(self):
        cost = self.cost
        if cost["food"] > self.game.food or cost["wood"] > self.game.wood or cost["stone"] > self.game.stone or self.game.population + cost["pop"] > self.game.population_limit:
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
        if not obj.check_resources():
            obj.progress_bar.kill()
            return None
        obj.buy()
        game.entities.add(obj)
        return True
