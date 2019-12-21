#!/usr/bin/env python3

"""
Main entry point for the program.
"""

from rogueish.system import SystemKeyboard, SystemDisplay
from rogueish.component import ComponentPosition, ComponentSize, ComponentSprite, ComponentKeyboardControlled, ComponentRoom
from rogueish.entity import Entity

def main_loop():
    """
    Execute the main game loop.
    """
    entities = list()
    entities.append(Entity("Player", ComponentKeyboardControlled(), ComponentPosition(40, 25),
                           ComponentSprite('@', (255, 255, 255))))
    entities.append(Entity("Room", ComponentPosition(10, 10), ComponentSize(60, 30),
                           ComponentRoom('#', (180, 32, 32), (0, 0, 0))))

    keyboard = SystemKeyboard()
    display = SystemDisplay(80, 50)

    systems = (keyboard, display)

    # Display first frame before hitting game loop
    display.update(entities)

    while not keyboard.quit:
        for system in systems:
            system.update(entities)

if __name__ == "__main__":
    main_loop()
