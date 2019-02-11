import pygame
from entity_sprite import EmptySprite


class EventHandling:

    def __init__(self, game):
        self.game = game

        self.mouse_down = None
        self.sel_sprites = []

    def handle(self):
        for e in pygame.event.get():

            # X pressed
            if e.type == pygame.QUIT:
                return True

            # mouse button down
            if e.type == pygame.MOUSEBUTTONDOWN:

                # left mouse button
                if e.button == 1:
                    self.mouse_down = e.pos

                # middle mouse button
                elif e.button == 2:
                    self.game.placing_building = False

                # right mouse button
                elif e.button == 3:
                    self.game.placing_building = False
                    self.right_click(e)

            # mouse button up
            elif e.type == pygame.MOUSEBUTTONUP:

                # left mouse button
                if e.button == 1 and self.mouse_down is not None:

                    # left click
                    if self.mouse_down == e.pos:
                        self.left_click(e)

                    # left drag
                    else:
                        self.game.placing_building = False
                        self.left_drag(e)

                    # reset for next click
                    self.mouse_down = None

            # key pressed
            elif e.type == pygame.KEYUP:
                self.game.placing_building = False
                self.key_pressed(e)

    # right click currently only moves entities
    def right_click(self, event):
        if self.sel_sprites is None:
            return
        for s in self.sel_sprites:
            s.right_click(event.pos)

    def left_click(self, event):

        if self.game.placing_building:
            for c in self.game.control:
                c.left_click(event.pos, self.sel_sprites)
            self.game.placing_building = False

        # check collisions with control and entity sprites
        clicked = EmptySprite(event.pos, event.pos)
        control_col = pygame.sprite.spritecollide(clicked, self.game.control, False)
        entities_col = pygame.sprite.spritecollide(clicked, self.game.entities, False)

        # update selected sprites if no control element clicked
        if len(control_col) == 0:
            if len(entities_col) > 0:
                self.sel_sprites = [entities_col[0]]
            else:
                self.sel_sprites = None

        # pass event to all control elements (eg to unfocus info_bar)
        for c in self.game.control:
            c.left_click(event.pos, self.sel_sprites)

    def left_drag(self, event):
        clicked = EmptySprite(self.mouse_down, event.pos)
        collisions = pygame.sprite.spritecollide(clicked, self.game.entities, False)
        if len(collisions) > 0:
            self.sel_sprites = collisions
        else:
            self.sel_sprites = None

        # pass event to all control elements (eg to display selected entities)
        for c in self.game.control:
            c.left_click(event.pos, self.sel_sprites)

    def key_pressed(self, event):
        if self.sel_sprites is None:
            return
        for s in self.sel_sprites:
            s.key_pressed(pygame.key.name(event.key))
