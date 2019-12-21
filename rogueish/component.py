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

class ComponentSize(object):
    """
    Component for defining those with size.
    This is used for defining components with a specific size. Some components
    such as sprite will implicitly have a size of 1x1 and will not require this.
    """
    def __init__(self, width=1, height=1):
        self.size = (width, height)

class ComponentSprite(object):
    """
    Component for sprite.
    """
    def __init__(self, char, color):
        self.char = char
        self.color = color

class ComponentRoom(object):
    """
    Component for a room.
    """
    def __init__(self, wall, wall_fg_color, wall_bg_color, floor='.', floor_fg_color=(48, 48, 48), floor_bg_color=(0, 0, 0)):
        self.wall = wall
        self.wall_fg_color = wall_fg_color
        self.wall_bg_color = wall_bg_color
        self.floor = floor
        self.floor_fg_color = floor_fg_color
        self.floor_bg_color = floor_bg_color

class ComponentKeyboardControlled(object):
    """
    Component to indicate controlled by the keyboard.
    """
    def __init__(self):
        pass
