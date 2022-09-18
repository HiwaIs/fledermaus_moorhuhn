import pygame


pygame.init()
pygame.mixer.init()

### Sound ###
#Sound Class
class Sound:

    def __init__(self):
        
        # Initalize all sounds
        self.hit = pygame.mixer.Sound("./sounds/hit.Ogg")
        self.shot = pygame.mixer.Sound("sounds/shot.wav")
        self.reload = pygame.mixer.Sound("./sounds/reload.mp3")
        self.yeah = pygame.mixer.Sound("./sounds/yeah.aiff")
        self.muah = pygame.mixer.Sound("./sounds/evil_laugh.wav")
        self.noAmmo = pygame.mixer.Sound("./sounds/no_ammo.Ogg")

    
    def backgroundMusic(self):
        self.background = pygame.mixer.music.load("./sounds/background.mp3")
        pygame.mixer.music.play(-1)

    def hitSound(self):
        return self.hit.play()

    def shotSound(self):
        return self.shot.play()

    def reloadSound(self):
       return self.reload.play()

    def yeahSound(self):
        return self.yeah.play()

    def muahSound(self):
        return self.muah.play()
    
    def noAmmoSound(self):
        return self.noAmmo.play()