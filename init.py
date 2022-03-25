import pygame
from pygame.locals import *
from pygame import mixer

resolution = (1024, 768)


def initializeGame():
    # Initialize pygame
    pygame.init()
    # Title and Icon
    pygame.display.set_caption("Space Invaders")
    icon = pygame.image.load('player.png')
    pygame.display.set_icon(icon)
    return True


def initializeScreen():
    # create a screen (width,height)
    screen = pygame.display.set_mode(resolution, DOUBLEBUF, 16)
    return screen


# Calling initializing functions
initializeGame()
screen = initializeScreen()
# Music
mixer.music.load('background.wav')
mixer.music.play(-1)
