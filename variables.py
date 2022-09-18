import pygame
import random
from factory import *
from settings import *
from weapon import *
from collider import *
from button import *
from font import *
from score import *



### Game variables ###
#init
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.SCALED)
pygame.display.set_caption("Fledermaus")

# Background
size = (WIDTH, HEIGHT)

# Create object
fledermaeuse = []
kurbese = []

# Factory
flederFactory = FlederFactory()
kurbesFactory = KurbesFactory()

# Crosshair
player = Weapon()

# Font
font = Fonts()
score = Score()

# Sound
Sound().backgroundMusic()

# Collider
collider = Collider()

# Ammo
ammo = MAXAMMO

# Images
bg = Image().getBackgroundImage()
bg_Intro = Image().getIntroImage()
bg_Intro2 = Image().getIntro2Image()
feuer = Image().getFeuerImage()
settingsImage = Image().getSettingImage()
geist = Image().getGeistImage()
ammo_Image = Image().getAmmoImage()

# Buttons
playButton = Button(WIDTH * 0.1, HEIGHT * 0.23, 'Play', screen)
settingsButton = Button(WIDTH * 0.1, HEIGHT * 0.4, 'Settings', screen)
exitButton = Button(WIDTH * 0.1, HEIGHT * 0.57, 'Exit', screen)
backButton = Button(WIDTH * 0.1, HEIGHT * 0.8, 'Back', screen)
playAgainButton = Button(WIDTH * 0.1, HEIGHT * 0.3, 'Try Again', screen)

# Pygame Clock
clock = pygame.time.Clock()
counter = SPIELLAUFZEIT
pygame.time.set_timer(pygame.USEREVENT + 2, 1000)

### Events ###
# Pumpkin Event
kurbes_spawn = pygame.USEREVENT + 1
pygame.time.set_timer(kurbes_spawn, random.randint(7000, 11000))

# Badsprite Event
fledermaus_spawn = pygame.USEREVENT + 0
pygame.time.set_timer(fledermaus_spawn, random.randint(1000,1500))

