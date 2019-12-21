#!/usr/bin/env python3

"""
This module defines all system classes.
"""

import tcod
import tcod.event

from rogueish.component import ComponentPosition, ComponentSize, ComponentSprite, ComponentKeyboardControlled, ComponentRoom
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
            if e.has(ComponentPosition) and e.has(ComponentKeyboardControlled):
                x, y = e.get(ComponentPosition).pos
                for event in events:
                    if event.type == "KEYDOWN":
                        if event.scancode == tcod.event.SCANCODE_UP:
                            y -= 1
                        elif event.scancode == tcod.event.SCANCODE_DOWN:
                            y += 1
                        elif event.scancode == tcod.event.SCANCODE_LEFT:
                            x -= 1
                        elif event.scancode == tcod.event.SCANCODE_RIGHT:
                            x += 1
                        elif event.scancode == tcod.event.SCANCODE_Q or \
                             event.scancode == tcod.event.SCANCODE_ESCAPE:
                            self.quit = True
                    elif event.type == "QUIT":
                        self.quit = True
                e.get(ComponentPosition).pos = (x, y)

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

        # Handle background objects
        for e in entities:
            if e.has(ComponentPosition) and e.has(ComponentSize) and e.has(ComponentRoom):
                position = e.get(ComponentPosition).pos
                size = e.get(ComponentSize).size

                wall = e.get(ComponentRoom).wall
                wall_fg = e.get(ComponentRoom).wall_fg
                wall_bg = e.get(ComponentRoom).wall_bg

                floor = e.get(ComponentRoom).floor
                floor_fg = e.get(ComponentRoom).floor_fg
                floor_bg = e.get(ComponentRoom).floor_bg

                self.console.draw_rect(*position, *size, ch=ord(floor), fg=floor_fg, bg=floor_bg)
                for x in range(size[0]):
                    self.console.print(position[0] + x, position[1], string=wall, fg=wall_fg, bg=wall_bg)
                    self.console.print(position[0] + x, position[1] + size[1] - 1, string=wall, fg=wall_fg, bg=wall_bg)
                for y in range(size[1]):
                    self.console.print(position[0], position[1] + y, string=wall, fg=wall_fg, bg=wall_bg)
                    self.console.print(position[0] + size[0] - 1, position[1] + y, string=wall, fg=wall_fg, bg=wall_bg)

        # Handle foreground objects
        for e in entities:
            if e.has(ComponentPosition) and e.has(ComponentSprite):
                position = e.get(ComponentPosition).pos
                char = e.get(ComponentSprite).char
                color = e.get(ComponentSprite).color
                self.console.print(*position, string=char, fg=color)

        tcod.console_flush()
