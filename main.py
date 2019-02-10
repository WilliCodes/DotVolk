import pygame
import config
import game
import event_handling

# load settings
cfg = config.Config()

# initialize pygame
pygame.init()
window = pygame.display.set_mode((cfg.DISPLAY_WIDTH, cfg.DISPLAY_HEIGHT))
pygame.display.set_caption("DotVolk")
clock = pygame.time.Clock()

# load game instance
game = game.Game()
event_handler = event_handling.EventHandling(game)


# tell each drawing to draw itself
def draw():
    # reset window
    window.fill((255, 255, 255))

    # draw in this order for overlapping
    for e in game.entities:
        e.draw()
    for d in game.drawings:
        d.draw()
    for c in game.control:
        c.draw()

    pygame.display.update()


# tell each entity to update itself
def update():
    for e in game.entities:
        e.update()


# main game loop

run = True
while run:
    if event_handler.handle():
        run = False
    update()
    draw()
    clock.tick(cfg.FPS)

pygame.quit()


