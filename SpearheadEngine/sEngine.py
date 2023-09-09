import sys
import pygame as pg

#Spearhead Engine v0.1.1 - created by Kappa of Kaffeehaus Software

pg.init()
running = True

# TODO:
#   - Create function to open / close window 
#   - GameObject class
#   - Sprite class
#   - Collision class
#   - simple physics system? (maybe use outside library)
#   - Audio system
#   - DOOR SYSTEM BECAUSE ENGINES NEED THESE 
# (FRICK YOU UNITY AND GODOT (not as much gamemaker because the room specific code is super awesome and useful))
#   - ECS


# windowing [

def openWindow(title: str, width: int, height: int):
    pg.display.set_caption(title)
    screen = pg.display.set_mode((width, height))
    screen.fill("purple")
    running = True

# ]


# classes (objects and components) [

    # Basic Game object

class gameObject:
    def __init__(x: float, y: float, name: str):
        self.x = x
        self.y = y
        self.name = name

        self.components = []

    def addComponent(comp):
        components.append(comp)

    # Sprite Components

class spriteComponent:
    def __init__(pathToImage: str):
        pass

class AnimatedSpriteComponent:
    def __init__(pathToImage: str, rows: int, columns: int, frameSize: float):
        pass

    # Collision Component

class collisionComponent:
    def __init__():
        pass

# ]

# graphics [






# ]

# physics [







# ]


# doors [







# ]


# audio [ 








#]


# general tick function [

def tick():

    running = True

    while running == True:

        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False

        keys = pg.key.get_pressed()

        # updateObjects()
        # drawSprites()
        # checkCollisions()
        pg.display.flip()

# ]


# quit [

def spearheadQuit():
    pg.quit()
    sys.exit()

# ]
