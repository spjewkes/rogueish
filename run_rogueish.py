#!/usr/bin/env python3

"""
Main entry point for the program.
"""

from system import SystemKeyboard, SystemDisplay
from component import ComponentPosition, ComponentSprite, ComponentKeyboardControlled
from entity import Entity

def main_loop():
    """
    Execute the main game loop.
    """
    entities = list()
    entities.append(Entity("Player", ComponentKeyboardControlled(), ComponentPosition(40, 25),
                                      ComponentSprite('@', 255, 255, 255)))

    keyboard = SystemKeyboard()
    display = SystemDisplay(80, 50)

    systems = (keyboard, display)

    while not keyboard.quit:
        for system in systems:
            system.update(entities)

if __name__ == "__main__":
    main_loop()
