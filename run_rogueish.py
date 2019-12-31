#!/usr/bin/env python3

"""
Main entry point for the program.
"""

from rogueish.system import SystemKeyboard, SystemStaticCollisions, SystemDynamics, SystemDisplay
from rogueish.component import ComponentPosition, ComponentDynamics, ComponentSprite, ComponentKeyboardControlled, \
    ComponentTile
from rogueish.entity import Entity

def build_world(entities):
    """
    Add world content to entities.
    """
    world = ""
    world += "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    world += "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    world += "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    world += "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    world += "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    world += "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    world += "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    world += "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    world += "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    world += "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxx                                                            xxxxxxxxxx"
    world += "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    world += "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    world += "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    world += "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    world += "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    world += "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    world += "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    world += "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    world += "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    world += "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

    for y in range(50):
        for x in range(80):
            if world[y * 80 + x] == 'x':
                entities.append(Entity("Rock", ComponentPosition(x, y),
                                       ComponentTile('#', (30, 180, 180), (0, 90, 90), True)))
            else:
                entities.append(Entity("Room", ComponentPosition(x, y),
                                       ComponentTile('.', (180, 180, 180), (60, 60, 60), False)))

def build_chars(entities):
    """
    Add player character and NPCs to world.
    """
    entities.append(Entity("Player", ComponentKeyboardControlled(), ComponentPosition(40, 25), ComponentDynamics(),
                           ComponentSprite('@', (255, 255, 255))))

def main_loop():
    """
    Execute the main game loop.
    """
    entities = list()
    build_world(entities)
    build_chars(entities)

    keyboard = SystemKeyboard()
    static_physics = SystemStaticCollisions(80, 50, entities)
    dynamics = SystemDynamics()
    display = SystemDisplay(80, 50)

    systems = (keyboard, static_physics, dynamics, display)

    # Display first frame before hitting game loop
    display.update(entities)

    while not keyboard.quit:
        for system in systems:
            system.update(entities)

if __name__ == "__main__":
    main_loop()
