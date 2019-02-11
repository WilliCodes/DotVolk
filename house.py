from building import Building
import pygame


class House(Building):
    initial_hp = 200
    hp_factor = 1
    hp_max = initial_hp * hp_factor

    name = "House"
    cost = {"food": 0, "wood": 50, "stone": 0, "pop": 0}
    image_path = './assets/house.png'

    build_time = 10

    def __init__(self, pos, game):
        super(House, self).__init__(pos)

        self.image = pygame.image.load(self.image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

        self.surface = pygame.display.get_surface()

        self.game = game

        self.hp = self.initial_hp * self.hp_factor

    def draw(self):
        self.surface.blit(self.image, self.rect)

    def on_build(self):
        self.game.population_limit += 10

    def on_destroy(self):
        self.game.population_limit -= 10
