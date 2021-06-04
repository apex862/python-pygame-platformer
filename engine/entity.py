import pygame
from .component_transform import TransformComponent
from .component_tag import TagsComponent
from .component_imagegroups import ImageGroups

def resetEntity(entity):
    pass

class Entity:
    
    # class-level ID, used to create new entities
    ID = 0

    def __init__(self, *componentList):

        # set and increment the entity id
        self.ID = Entity.ID
        Entity.ID += 1

        # create component dictionary
        self.components = {}

        # set up default components
        self.addComponent(ImageGroups())
        self.addComponent(TransformComponent())
        self.addComponent(TagsComponent())

        # populate component dictionary from passed componenets
        # (this will overwrite existing default components)
        for component in componentList:
            self.addComponent(component)

        self.state = 'idle'
        self.type = 'normal'
        self.position = None
        self.imageGroups = ImageGroups()
        self.direction = 'right'
        self.camera = None
        self.score = None
        self.battle = None
        self.input = None
        self.intention = None
        self.on_ground = False
        self.effect = None
        self.reset = resetEntity
        self.trauma = 0
        self.collider = None
        self.transform = TransformComponent()
        self.motion = None
        self.tags = TagsComponent()
        self.particle_emitter = None
        self.emote = None
        self.text = None
        self.owner = self
        self.triggers = None
    
    def clear(self):
        self.components = {}
    
    def reset(self):
        self.reset()

    def hasComponent(self, componentKey):
        return componentKey in self.components.keys()
    
    def getComponent(self, componentKey):
        if componentKey not in self.components.keys():
            return None
        return self.components[componentKey]

    def addComponent(self, component):
        if component.key is not None:
            self.components[component.key] = component
    
    def removeComponent(self, componentKey):
        if componentKey in self.components.keys():
            self.components.pop(componentKey)
