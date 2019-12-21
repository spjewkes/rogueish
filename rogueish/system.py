#!/usr/bin/env python3

"""
This module defines all system classes.
"""

import tdl

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
        user_input = tdl.event.key_wait()
        key = user_input.keychar

        for e in entities:
            if e.has(ComponentPosition) and e.has(ComponentKeyboardControlled):
                x, y = e.get(ComponentPosition).get()
                if key == "UP":
                    y -= 1
                elif key == "DOWN":
                    y += 1
                elif key == "LEFT":
                    x -= 1
                elif key == "RIGHT":
                    x += 1
                elif key == "ESCAPE" or key == 'q':
                    self.quit = True
                e.get(ComponentPosition).set(x, y)

class SystemDisplay(object):
    """
    System for handling the display.
    """
    def __init__(self, width, height):
        self.size = (width, height)
        self.console = tdl.init(width, height)

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
                self.console.draw_char(*position, char=char, fg=color)

        tdl.flush()
