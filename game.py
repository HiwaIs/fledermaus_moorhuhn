import pygame
from state import *


### Gameloop ###
# Enjoy the Game ;D

# Initalize gameclass
game = Game()

while game:
    game.startGame()

# Time to end 
pygame.quit()
