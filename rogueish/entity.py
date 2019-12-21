#!/usr/bin/env python3

"""
This module defines the entity class.
"""

class Entity(object):
    """
    The entity class defines a list of objects that make up the game environment.
    The type of entity is defined by its components.
    """

    all_entities = list()

    def __init__(self, name, *components):
        self._components = {}
        Entity.all_entities.append(self)

        self.name = name

        for component in components:
            self.set(component)

    def set(self, component):
        """
        Add component to entity. If a component of this type already
        exists then it is replaced.
        """
        key = type(component)
        self._components[key] = component

    def get(self, component_class):
        """
        Returns this entity's component of specified type or None (if none exists).
        """
        return self._components[component_class]

    def has(self, component_class):
        """
        Returns boolean to indicate whether a component of a specified type exists
        in this entity.
        """
        return self.get(component_class) is not None
