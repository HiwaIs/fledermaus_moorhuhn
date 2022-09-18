
from settings import *
import pygame


### Font Class ###
class Fonts:
    def __init__(self):
        pass
        
    # Returning the desired font
    def getFont(self, name:str, size: int):
        self.name = name
        self.size = size
        font = pygame.font.SysFont(name,size)

        return font
    

    # Return the desired text
    def getText(self, text:str):
        self.text = text
        text1 = text.rjust(3)
        return text1
    

    

        

       
        
            
        