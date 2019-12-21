#!/usr/bin/env python3

"""
This module defines all system classes.
"""

import tcod
import tcod.event

from rogueish.component import ComponentPosition, ComponentSprite, ComponentKeyboardControlled
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
                x, y = e.get(ComponentPosition).get()
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
                e.get(ComponentPosition).set(x, y)

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

        for e in entities:
            if e.has(ComponentPosition) and e.has(ComponentSprite):
                position = e.get(ComponentPosition).get()
                char = e.get(ComponentSprite).get_char()
                color = e.get(ComponentSprite).get_color()
                self.console.print(*position, string=char, fg=color)

        tcod.console_flush()
