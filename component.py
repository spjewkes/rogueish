#!/usr/bin/env python3

"""
This module defines all component classes.
"""

class ComponentPosition(object):
    """
    Component for defining position.
    """
    def __init__(self, x=0, y=0):
        self.pos = (x, y)

    def set(self, x, y):
        """
        Update the position
        """
        self.pos = (x, y)

    def get(self):
        """
        Fetch the position
        """
        return self.pos

class ComponentSprite(object):
    """
    Component for sprite.
    """
    def __init__(self, char, red, green, blue):
        self.char = char
        self.color = (red, green, blue)


    def get_char(self):
        """
        Return character used for this sprite.
        """
        return self.char

    def get_color(self):
        """
        Return color to be used for this sprite.
        """
        return self.color

class ComponentKeyboardControlled(object):
    """
    Component to indicate controlled by the keyboard.
    """
    def __init__(self):
        pass
