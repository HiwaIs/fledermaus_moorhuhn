import pygame
from pygame.locals import *
from settings import *
from font import *



### Buttons ###
# Button Class
class Button():

    def __init__(self, x, y, text, screen):
        # Settings for Buttons
        self.width = WIDTH * 0.15
        self.height = HEIGHT * 0.10
        self.x = x
        self.y = y
        self.text = text
        self.clicked = False
        self.screen = screen
        
    # Drawing the interactive Button
    def draw_Button(self):
        action = False

        pos = pygame.mouse.get_pos()

        # Create pygame Rect object for the Button
        button_rect = Rect(self.x, self.y, self.width, self.height)

        # Check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
                pygame.draw.rect(self.screen, LIGHT_YELLOW, button_rect)
                
            elif pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
                self.clicked = False
                action = True
            else:
                pygame.draw.rect(self.screen, RED, button_rect)
        else:
            pygame.draw.rect(self.screen, FIREBRICKS, button_rect)

        # Add shading to Button
        pygame.draw.line(self.screen, WHITE, (self.x, self.y), (self.x + self.width, self.y), 4)
        pygame.draw.line(self.screen, WHITE, (self.x, self.y), (self.x, self.y + self.height), 4)
        pygame.draw.line(self.screen, BLACK , (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 4)
        pygame.draw.line(self.screen, BLACK, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 4)

        # Add text to Button
        text_img = Fonts().getFont('Constantia', 30).render(self.text, True, WHITE)
        text_len = text_img.get_width()
        self.screen.blit(text_img, (self.x + int(self.width * 0.5) - int(text_len * 0.5), self.y + 20))
        
        # Returning the boolean, the button got hitted or not
        return action


    