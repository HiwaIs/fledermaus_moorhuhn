import pygame
import random
import sys
from factory import *
from settings import *
from weapon import *
from collider import *
from button import *
from font import *
from score import *
from variables import *
from background360 import *



###################################
### State Pattern ###
#Abstract Class
class GameState:
    def start(self):
        raise NotImplementedError

    def enter(self):
        raise NotImplementedError

# Class for Initial Game
class Game:
    def __init__(self):
        self.gameState = GameStartState(self)

    # Change screen 
    def changeState(self, newState: GameState):
        self.gameState = newState
        self.gameState.enter()

    def startGame(self):
        self.gameState.start()

#Start screen
class GameStartState(GameState):

    def __init__(self, game: Game):
        self.game = game
        self.counter = SPIELLAUFZEIT
        self.score = 0
        self.event = pygame.event
        screen.blit(bg_Intro, (0, 0))

    # Blitting background, Buttons,  Text
    def start(self):

        screen.blit(bg_Intro, (0, 0))
        if settingsButton.draw_Button():
            self.game.changeState(SettingState(self.game))

        elif playButton.draw_Button():

            self.game.changeState(GameLooping(self.game))

        elif exitButton.draw_Button():
            pygame.quit()
            sys.exit()

        else:
            pass

        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            screen.blit(font.getFont("Calibri", 80).render("Welcome to the hell", 1, RED),
                        (WIDTH * 0.16, HEIGHT * 0.035))

            pygame.display.flip()


    def enter(self):
        pass

# Setting screen 
class SettingState(GameState):
    def __init__(self, game: Game):
        self.game = game

    def start(self):
        #Blitting how game works, buttons, background
        for self.event in pygame.event.get():
            screen.blit(settingsImage, (0, 0))
            if self.event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if backButton.draw_Button():
            self.game.changeState(GameStartState(self.game))
        pygame.display.flip()

    def enter(self):
        pass

# The actual game class
class GameLooping(GameState):
    def __init__(self, game: Game):
        self.game = game

        # Setting the game time to the value which is given in the settings
        self.counter = SPIELLAUFZEIT
        self.score = score
        self.ammo = ammo
        self.event = pygame.event
        self.text = Fonts().getText("--")
        self.geschossen = False


    def getScore(self):
        return self.score

    def enter(self):
        pass

    def start(self):
        
        # Set the mouse cursor invisible
        pygame.mouse.set_visible(False)
        clock.tick(FPS)

        if self.counter > 0:

            draw_Background_360()
            for self.event in pygame.event.get():

                # Make it possible for the player to always leave the game
                if self.event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
           
                # Updating the ammo
                if self.event.type == pygame.MOUSEBUTTONDOWN:
                    self.ammo, self.geschossen = player.updateMuni(pygame.mouse.get_pressed(), self.ammo)

                # Check whether a legitimate shot has been taken
                if self.geschossen:
                    screen.blit(feuer, (WIDTH * 0.2, HEIGHT * 0.8))

                # Counting down the gametime 
                if self.event.type == pygame.USEREVENT + 2:
                    self.counter -= 1
                    if self.counter > 0:
                        self.text = str(self.counter)

                else:
                    pass

                # Spawn Pumpkins (PowerUps or PowerDows) on random positions
                if self.event.type == kurbes_spawn:
                    x = random.randint(0, WIDTH)
                    kurbese.append(kurbesFactory.createKurbesAtPosition(x))

                # Spawn Badsprites on random positions
                if self.event.type == fledermaus_spawn:
                    y = random.randint(54, HEIGHT-54)


                    fledermaeuse.append(flederFactory.createRandomObject(y))

            ### Collision ###
            # Checking if a badsprite got hit by a "bullet"
            for sprite in fledermaeuse:
                if collider.RectVsRect(sprite.getRect(), player.getRect()) and self.geschossen and sprite.isDead() == False:
                    Sound().hitSound()
                    self.score.punkteUpdate(sprite.groesse)
                    sprite.setDead()

                # Checking if the badsprite is out of screen
                if sprite.isWeg():
                    fledermaeuse.remove(sprite)

            # Checking if a pumpkin got hit by a "bullet"   
            for sprite in kurbese:
                if collider.RectVsRect(sprite.getRect(), player.getRect()):
                    if self.geschossen:

                        kurbese.remove(sprite)
                        
                        # Generate randomly if the pumpkin is speeding up the badsprite or slowing them down
                        n_speed = random.choice([SLOWMOW, SPEEDUP])
                        if n_speed == SLOWMOW:
                            Sound().yeahSound()
                        elif n_speed == SPEEDUP:
                            Sound().muahSound()
                        else:
                            pass
                        
                        # Giving the badsprites their new speed
                        for fledermaus in fledermaeuse:
                            fledermaus.neueSpeed(n_speed)

                        # Hier die powerUps rein


            # Update
            for kurbes in kurbese:
                kurbes.update()

            for sprite in fledermaeuse:
                sprite.update()

            player.update()

            self.geschossen = False


            # Render
            for sprite in fledermaeuse:
                sprite.render(screen)

            for kurbes in kurbese:
                screen.blit(kurbes.getImage(), kurbes.getRect())

            screen.blit(player.getImage(), player.getRect())

            player.drawAmmo(screen, self.ammo)

            # Blitting the score and the time on the screen
            screen.blit(
                font.getFont("Calibri", 25).render("Time left: " + font.getText(str(self.counter)), True, WHITE),
                (WIDTH * 0.03, HEIGHT * 0.05))
            screen.blit(font.getFont("Calibri", 25).render("Score: " + str(self.score.getScore()), True, YELLOW),
                        (WIDTH * 0.03, HEIGHT * 0.15))


            # Double Buffering
            pygame.display.flip()
        else:
            self.game.changeState(GameEndeState(self.game))

# Game-Over screen
class GameEndeState(GameState):

    def __init__(self, game: Game):
        #get the stats of actual game
        self.game = game
        self.event = pygame.event
        self.score = score.getScore()
        self.counter = SPIELLAUFZEIT


    def enter(self):
        pass

    def start(self):
        #set mouse visible
        pygame.mouse.set_visible(True)
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #Blitting background and Score
        screen.blit(bg_Intro2, (0, 0))
        screen.blit(font.getFont("Calibri", int(HEIGHT * 0.2)).render("Score: " + str(self.score), 1, YELLOW),
                    (WIDTH * 0.5, HEIGHT * 0.5))


        #Blitting exitButton and close if clicked
        if exitButton.draw_Button():
            pygame.quit()
            sys.exit()
        #Blitting Playagain Button and reset Gameobjects,Score to play again
        if playAgainButton.draw_Button():
            fledermaeuse.clear()
            kurbese.clear()
            score.setScoreZero()
            self.game.changeState(GameLooping(self.game))

        pygame.display.flip()



