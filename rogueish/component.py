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

class ComponentDynamics(object):
    """
    Defines the dynamics of an object.
    """
    def __init__(self):
        self.velocity = (0, 0)

class ComponentSprite(object):
    """
    Component for sprite.
    """
    def __init__(self, char, color):
        self.char = char
        self.color = color

class ComponentTile(object):
    """
    Component for describing a tile.
    """
    def __init__(self, char, color_fg, color_bg, solid):
        self.char = char
        self.color_fg = color_fg
        self.color_bg = color_bg
        self.solid = solid

class ComponentKeyboardControlled(object):
    """
    Component to indicate controlled by the keyboard.
    """
    def __init__(self):
        pass
