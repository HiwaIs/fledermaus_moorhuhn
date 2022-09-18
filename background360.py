import pygame
from settings import *
from weapon import *
from variables import *


###################################
# Beginning position of the view
background_pos_x = 0

# Make the player being able to move the background and creating a 360 degrees gamefield (optically)
def draw_Background_360():
    global background_pos_x

    # Moving right and left
    allKeys = pygame.key.get_pressed()
    if allKeys[pygame.K_LEFT]:
        background_pos_x += KEY_SPEED
    elif allKeys[pygame.K_RIGHT]:
        background_pos_x -= KEY_SPEED
    else:
        background_pos_x += 0

    # for background scrolling we need to draw the background two times
    Background_x_part1 = background_pos_x % WIDTH
    if Background_x_part1 > 0:
        Background_x_part2 = Background_x_part1 - WIDTH
    else:
        Background_x_part2 = Background_x_part1 + WIDTH
    screen.blit(bg, (Background_x_part1, 0))
    screen.blit(bg, (Background_x_part2, 0))
###################################