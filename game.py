import pygame

import field
import house
import info_display
import status_bar
import towncenter
import worker
import building

class Game:

    def __init__(self):
        self.entities = pygame.sprite.Group()
        self.drawings = pygame.sprite.Group()
        self.control = []

        self.wood = 100
        self.stone = 100
        self.food = 100

        self.population = 0
        self.population_limit = 10

        self.board_init()

        self.placing_building = False

    def board_init(self):

        # fixes circular imports
        worker.Worker.buildable.append(towncenter.Towncenter)

        self.control.append(status_bar.StatusBar(20, self))
        self.control.append(info_display.InfoDisplay(self))
        self.entities.add(towncenter.Towncenter((70, 70), self))
        self.entities.add(field.Field((200, 200), self))
        self.entities.add(house.House((300, 300), self))
        self.place_entity(worker.Worker, (50, 50))

    def place_worker(self, pos):
        self.entities.add(worker.Worker(pos, self))

    def place_entity(self, entity, pos):
        new_entity = entity(pos, self)
        if isinstance(new_entity, building.Building):
            new_entity.on_build()
        self.entities.add(new_entity)

    def remove_entity(self, entity):
        if isinstance(entity, building.Building):
            entity.on_destroy()
        self.entities.remove(entity)

    def add_drawing(self, drawing):
        self.drawings.append(drawing)

    def rmv_drawing(self, drawing):
        self.drawings.remove(drawing)
