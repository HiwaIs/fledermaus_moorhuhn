from settings import *
from sprites import *
from flyweight import *
import pygame as pg
import random
from weapon import *


### Factory ###
# Factory Class for the badsprites
class FlederFactory:
    def __init__(self):
        self.imageDict = ImageFlyweight().getFlyweightImages()

    # Create a random badsprite object with random given sizes and speed
    def createRandomObject(self, y):
        
        choice1 = random.choice([-1, 1])
        choice2 = random.choice([0.7, 0.3])
        groesse = random.choice([(93,54), (186, 108), (47, 27)])

        return Fledermaus(self.imageDict, y, SPEED * choice1 * choice2, 0 , groesse)

# Factory Class for the pumpkins 
class KurbesFactory:
    def __init__(self):
        self.image = ImageFlyweight().getFlyweightImagesKurbes()

    # Create a pumpkin object
    def createKurbesAtPosition(self, x):

        return NewSpeed(self.image, x, FLUG * 0.5)
