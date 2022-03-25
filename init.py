import pygame

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
    screen = pygame.display.set_mode((800,600))
    return screen


