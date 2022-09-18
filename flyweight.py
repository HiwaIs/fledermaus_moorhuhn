import os
import pygame as pg
from settings import * 
import random

### Images ###
# Image Class
class Image:
    def __init__(self):

        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'img')

        # Loading the static images of the game
        self.crosshairImage = pg.image.load(os.path.join(img_folder, 'crosshair1.png')).convert_alpha()
        self.bgImage = pg.transform.smoothscale(pg.image.load(os.path.join(img_folder, 'b.png')).convert_alpha(), (WIDTH, HEIGHT))
        self.bgIntroImage = pg.transform.smoothscale(pg.image.load(os.path.join(img_folder, 'Intro.png')).convert_alpha(), (WIDTH, HEIGHT))
        self.bgIntro2Image = pg.transform.smoothscale(pg.image.load(os.path.join(img_folder, 'b2.png')).convert_alpha(), (WIDTH, HEIGHT))
        self.feuerImage = pg.transform.smoothscale(pg.image.load(os.path.join(img_folder, 'f.png')).convert_alpha(), (WIDTH * 0.9, HEIGHT * 0.4))
        self.settingImage = pg.transform.smoothscale(pg.image.load(os.path.join(img_folder, 'set.png')).convert_alpha(), (WIDTH, HEIGHT))
        self.geistImage = pg.transform.smoothscale(pg.image.load(os.path.join(img_folder, 'geist.png')).convert_alpha(), (random.randint(50,100), random.randint(50,100)))
        self.ammoImage = pg.transform.scale(pg.transform.rotozoom(
                        pg.image.load(
                        os.path.join(img_folder, 'ammo.png')).convert_alpha(), -15, 1.7),(60,60))


    def getCrosshairImage(self):
        return self.crosshairImage

    def getBackgroundImage(self):
        return self.bgImage  

    def getIntroImage(self):
        return self.bgIntroImage

    def getIntro2Image(self):
        return self.bgIntro2Image

    def getFeuerImage(self):
        return self.feuerImage

    def getSettingImage(self):
        return self.settingImage

    def getGeistImage(self):
        return self.geistImage

    def getAmmoImage(self):
        return self.ammoImage


# Imageflyweight Class
class ImageFlyweight:
    def __init__(self):

        # Initialize all variables and do all the setup for a new game
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'img')

        # Make Dictionary of Images
        self.images = {}
        self.imagesDead = {}

        # Pumpkin dict
        self.imageKurbes = {}

        # Loading the pumpkin images into a dict
        for i in range(1, 5):
            self.imageKurbes['kurbes'+str(i)] = pg.image.load(os.path.join(
                img_folder, 'kurbes'+str(i)+'.png')).convert_alpha()

        # Loading images of badsprites
        for i in range(1, 5):
            self.images['fleder'+str(i)] = pg.image.load(os.path.join(
                img_folder, 'fleder'+str(i)+'.png')).convert_alpha()


        # Loading images of dead badsprites into dict
        for i in range(1, 2):
            self.images['tot'+str(i)] = pg.image.load(os.path.join(
                img_folder, 'tot'+str(i)+'.png')).convert_alpha()


    # Returning badsprite images
    def getFlyweightImages(self):
        return self.images


    # Returning pumpkin images
    def getFlyweightImagesKurbes(self):
        return self.imageKurbes

