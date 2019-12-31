#!/usr/bin/env python3

"""
This module defines all system classes.
"""

import tcod
import tcod.event
import numpy as np

from rogueish.component import ComponentPosition, ComponentDynamics, ComponentSprite, ComponentKeyboardControlled, ComponentTile
from rogueish.entity import Entity

class SystemKeyboard(object):
    """
    Syetem for managing the keyboard.
    """
    def __init__(self):
        self.quit = False

    def update(self, entities):
        """
        Get keyboard input and handle entities that can deal with this.
        """
        events = tcod.event.get()

        for e in entities:
            if e.has(ComponentDynamics) and e.has(ComponentKeyboardControlled):
                x, y = (0, 0)
                for event in events:
                    if event.type == "KEYDOWN":
                        if event.scancode == tcod.event.SCANCODE_UP:
                            y = -1
                        elif event.scancode == tcod.event.SCANCODE_DOWN:
                            y = 1
                        elif event.scancode == tcod.event.SCANCODE_LEFT:
                            x = -1
                        elif event.scancode == tcod.event.SCANCODE_RIGHT:
                            x = 1
                        elif event.scancode == tcod.event.SCANCODE_Q or \
                             event.scancode == tcod.event.SCANCODE_ESCAPE:
                            self.quit = True
                    elif event.type == "QUIT":
                        self.quit = True
                e.get(ComponentDynamics).velocity = (x, y)

class SystemStaticCollisions(object):
    """
    Handle collisions with static objects
    """
    def __init__(self, width, height, entities):
        # Get array of tiles in world to make it easier for this system to check
        # static collisions
        dummy_entity = Entity("Dummy")
        self.world = [[dummy_entity for y in range(height)] for x in range(width)]
        for e in entities:
            if e.has(ComponentPosition) and e.has(ComponentTile):
                pos = e.get(ComponentPosition).pos
                self.world[pos[0]][pos[1]] = e
                
    def update(self, entities):
        """
        Process any objects with position and dynamics.
        """
        for e in entities:
            if e.has(ComponentPosition) and e.has(ComponentDynamics):
                # If there's no tile or the tile is solid then the entity stops
                position = e.get(ComponentPosition)
                dynamics = e.get(ComponentDynamics)
                new_pos_x, new_pos_y = tuple(np.add(position.pos, dynamics.velocity))
                e = self.world[new_pos_x][new_pos_y]
                if not e.has(ComponentTile) or e.get(ComponentTile).solid:
                    dynamics.velocity = (0, 0)

class SystemDynamics(object):
    """
    Handle velocities of entities. This should be done after any collision systems have been applied.
    """
    def __init__(self):
        pass

    def update(self, entities):
        """
        Apply an entity's dynamics to its position.
        """
        for e in entities:
            if e.has(ComponentPosition) and e.has(ComponentDynamics):
                position = e.get(ComponentPosition)
                position.pos = tuple(np.add(position.pos, e.get(ComponentDynamics).velocity))

class SystemDisplay(object):
    """
    System for handling the display.
    """
    def __init__(self, width, height):
        self.size = (width, height)
        tcod.console_set_custom_font("prestige12x12_gs_tc.png", tcod.FONT_LAYOUT_TCOD | tcod.FONT_TYPE_GREYSCALE)
        self.console = tcod.console_init_root(width, height, order='F')
        tcod.console_flush()

    def update(self, entities):
        """
        Handle the display update using the entities capable of being rendered.
        """
        self.console.clear()

        # Handle tiles
        for e in entities:
            if e.has(ComponentPosition) and e.has(ComponentTile):
                position = e.get(ComponentPosition)
                tile = e.get(ComponentTile)

                self.console.print(position.pos[0], position.pos[1], string=tile.char, fg=tile.color_fg, bg=tile.color_bg)

        # Handle foreground objects
        for e in entities:
            if e.has(ComponentPosition) and e.has(ComponentSprite):
                position = e.get(ComponentPosition).pos
                char = e.get(ComponentSprite).char
                color = e.get(ComponentSprite).color
                self.console.print(*position, string=char, fg=color)

        tcod.console_flush()
