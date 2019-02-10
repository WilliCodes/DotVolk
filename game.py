import pygame
from worker import Worker
import towncenter
import field
import status_bar
import info_display


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

    def board_init(self):
        self.control.append(status_bar.StatusBar(20, self))
        self.control.append(info_display.InfoDisplay(self))
        self.entities.add(towncenter.Towncenter((70, 70), self))
        self.entities.add(field.Field((200, 200), self))

    def place_worker(self, pos):
        self.entities.add(Worker(pos, self))

    def add_drawing(self, drawing):
        self.drawings.append(drawing)

    def rmv_drawing(self, drawing):
        self.drawings.remove(drawing)
