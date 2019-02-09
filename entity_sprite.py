import pygame


class EntitySprite(pygame.sprite.Sprite):

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.position = pos

    def get_sprite(self):
        return self.image, self.rect


class EmptySprite(pygame.sprite.Sprite):

    def __init__(self, posUL, posBR):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(posUL, (posBR[0]-posUL[0], posBR[1] - posUL[1]))
