import pygame
import config
from entity_sprite import EmptySprite
import game as game_module
import towncenter
import worker

cfg = config.Config()

pygame.init()
window = pygame.display.set_mode((cfg.DISPLAY_WIDTH, cfg.DISPLAY_HEIGHT))
pygame.display.set_caption("DotCrowd")
clock = pygame.time.Clock()

game = game_module.Game()


def draw():
    window.fill((255, 255, 255))

    for e in game.entities:
        img, rect = e.get_sprite()
        window.blit(img, rect)
    for d in game.drawings:
        pygame.draw.rect(window, (0, 255, 0), d)
    for c in game.control:
        c.draw(window)

    pygame.display.update()


m_down = None
sel_sprites = []


def events():
    for event in pygame.event.get():
        global m_down, sel_sprites, run
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                m_down = event.pos
            elif event.button == 3:
                for s in sel_sprites:
                    s.target = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and m_down is not None:
                selection = EmptySprite(m_down, event.pos)
                sel_sprites = pygame.sprite.spritecollide(selection, game.entities, False)
                if m_down == event.pos and sel_sprites:
                    sel_sprites = [sel_sprites[0]]
                selection.kill()
                m_down = None
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                for s in sel_sprites:
                    if type(s) == towncenter.Towncenter:
                        s.append_to_queue(worker.Worker)


def update():
    for e in game.entities:
        e.update()


run = True

while run:
    events()
    update()
    draw()
    clock.tick(cfg.FPS)

pygame.quit()


