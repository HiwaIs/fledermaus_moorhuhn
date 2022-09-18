import pygame as pg
from pygame.time import *
from flyweight import *
from settings import *



### Sprites ####
# Sprite Class
class Sprite:
    def __init__(self, flyweightImages: dict, x: int, y: int, imagename: str):
        self.x = x
        self.y = y
        self.image = flyweightImages[imagename]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):
        raise NotImplementedError

    def getImage(self):
        return self.image

    def getRect(self):
        return self.rect

    def verschwinden(self):
        raise NotImplementedError

# Badsprite Class
class Fledermaus(Sprite):
    def __init__(self, flyweightImages: dict, y: int, sx: int, sy: int, groesse: tuple):

        # Make the badsprite start from the screenedges 
        if sx > 0:
            self.x = 0
        else:
            self.x = WIDTH
        self.y = y

        # Badsprite Images
        self.flyweightImages = flyweightImages
        self.image = self.flyweightImages['fleder1']
        self.imageIndex = 1

        # Size
        self.groesse = groesse

        # Image rect of badsprite respectively the hitbox of the badsprite
        self.rect = pg.Rect(self.x, self.y, self.groesse[0] * 0.8 , self.groesse[1] * 0.7)
        self.rect.center = (self.x, self.y)

        # Badsprite speed
        self.sx = sx
        self.sy = sy
        self.speed = 1

        # Rotate the badsprite Image
        self.maxtimer = FLEDERSPEED
        self.timer = 0

        # Variables for setting a new speed but time limited
        self.last_timer = pg.time.get_ticks()
        self.laengeTimer = 3500
        self.neueGeschwindigkeit = False

        # Variables for declaring a badsprite to dead
        self.dead = False
        self.wegVomFenster = False
        self.deadTimer = 0

    
    def update(self):
        
        # Rotate living badsprite Images after check if its dead
        if self.dead == False:
            self.rotate()

        # Check Time for setting badsprites speed
        if pg.time.get_ticks() - self.last_timer > self.laengeTimer:
            self.speed = 1
            self.neueGeschwindigkeit = False

        if self.neueGeschwindigkeit:                        
            self.x = self.x + self.sx * self.speed      
        else:
            self.x = self.x + self.sx

        self.y = self.y + self.sy
        self.rect.center = (self.x, self.y)

        # Adjust badsprite speed depending on background movement
        allKeys = pg.key.get_pressed()
        if allKeys[pg.K_LEFT]:
            self.x += KEY_SPEED
        elif allKeys[pg.K_RIGHT]:
            self.x -= KEY_SPEED

        self.rect.center = (self.x, self.y)

        # Checking if the dead sprite is in the gamewindow anymore
        if self.y > HEIGHT:
            self.wegVomFenster = True

        # Death animation
        if self.dead == True:
            self.checkFlugbahn()

    # Setting a dead animation
    def checkFlugbahn(self):
        self.deadTimer += 1
        if self.deadTimer == 3:
            self.sy = HEIGHT * 0.02        

    # Setting a new speed
    def neueSpeed(self, n_speed):

        self.speed = n_speed
        self.neueGeschwindigkeit = True
        self.last_timer = pg.time.get_ticks()

    # Making the badsprite rotate its image
    def rotate(self):
        self.timer += 1
        if self.timer == self.maxtimer:
            self.timer = 0
            self.imageIndex += 1
            if (self.imageIndex == 4):
                self.imageIndex = 1
            self.image = self.flyweightImages['fleder'+str(self.imageIndex)]

    # Declaring a badsprite to dead
    def setDead(self):

        # Changing the Image to a dead badsprite
        self.dead = True
        self.image = self.flyweightImages['tot1']
        self.y -= 50
        # Changing the direction of flight
        self.sy = -HEIGHT * 0.02

        
    # Render the badsprite image
    def render(self, screen):
        blit_image = pg.transform.scale(self.image, self.groesse)
        if self.sx < 0:
            blit_image = pg.transform.flip(blit_image, True, False)
        screen.blit(blit_image, self.rect)


    def isDead(self):
        return self.dead

    
    def isWeg(self):
        return self.wegVomFenster


### Interface Class of Pumpkins ###
class IPowerUp(Sprite):

    def __init__(self, flyweightImages: dict, x: int,  sy: int):
        self.x = x
        self.y = 0
        self.flyweightImages = flyweightImages
        self.image = self.flyweightImages['kurbes1']
        self.imageIndex = 1
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.sy = sy
        self.maxtimer = KURBESSPEED
        self.timer = 0

    # Rotate the pumpkin image
    def rotate(self):
        self.timer += 1
        if self.timer == self.maxtimer:
            self.timer = 0
            self.imageIndex += 1
            if (self.imageIndex == 5):
                self.imageIndex = 1
            self.image = self.flyweightImages['kurbes'+str(self.imageIndex)]

    def update(self):
        self.rotate()
        self.x = self.x
        allKeys = pg.key.get_pressed()

        # Adjust the pumpkin falling speed depending on the background movement
        if allKeys[pg.K_LEFT]:
            self.x += KEY_SPEED
        elif allKeys[pg.K_RIGHT]:
            self.x -= KEY_SPEED
        self.y = self.y + self.sy
        self.rect.center = (self.x, self.y)


# Pumpkin speedchanger Class
class NewSpeed(IPowerUp):

    def update(self):
        IPowerUp.update(self)




