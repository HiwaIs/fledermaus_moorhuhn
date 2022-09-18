import pygame as pg
from pygame.time import *
from flyweight import *
from settings import *
from sound import *


### Weapon ###
# Weapon Class
class Weapon():

    def __init__(self):

        # Loading the image of the Crosshair
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'img')

        self.image = pg.image.load(os.path.join(
                img_folder, 'crosshair1.png')).convert_alpha()

        # Loading the image of the ammo
        self.ammo_image = Image().getAmmoImage()
        self.ammo_out_image = self.ammo_image
        self.ammo_rect = self.ammo_image.get_rect(center=(AMMOABSTAND, HEIGHT * 0.95))
        self.rect = self.image.get_rect()

        # Variables for Delay between shoots and reloads
        self.lastShoot =  pygame.time.get_ticks()
        self.colldown  = 1000
        self.lastReload = pygame.time.get_ticks()
        self.colldown2 = 2000

    # Returning the Crosshair rect
    def getRect(self):
        return self.rect

    def getImage(self):
        return self.image
        
    # Making the crosshair image to the new mouse cursor
    def update(self):
        self.rect.center = (pg.mouse.get_pos())
    
    # Updating the ammo
    def updateMuni(self, mouse_buttons, ammo):
        geschossen = False
        currentTicks = pygame.time.get_ticks()

        # Setting its requirements to shoot 
        if mouse_buttons[0] and ammo > 0 and currentTicks - self.lastShoot >= self.colldown  and  currentTicks - self.lastReload >= self.colldown2:
            self.lastShoot = currentTicks
            ammo -=1
            Sound().shotSound()
            geschossen = True

        # Playing the sound of "out of ammo" status
        elif mouse_buttons[0] and ammo == 0:
            Sound().noAmmoSound()
           
        # Setting its requirements to reload
        elif mouse_buttons[2] and currentTicks - self.lastReload >= self.colldown2:
            self.lastReload = currentTicks
            ammo = MAXAMMO
            Sound().reloadSound()

        return ammo, geschossen
    

    # Draw the max- and current ammo on the screen, to make it visual and easy readable for the player
    def drawAmmo(self, screen, ammo):
        self.ammo_out_image.set_alpha(100)
        self.ammo_rect.x = AMMOABSTAND

        # drawing the transparent maxammo
        for i in range(MAXAMMO):
            self.ammo_rect.x += 30
            screen.blit(self.ammo_out_image, self.ammo_rect)

        # drawing the current ammo
        self.ammo_rect.x = AMMOABSTAND
        for i in range(ammo):
            self.ammo_rect.x += 30
            screen.blit(self.ammo_image, self.ammo_rect)        


