import pygame

def inicializeGame():
    # Inicialize pygame
    pygame.init()
    # Title and Icon
    pygame.display.set_caption("Space Invaders")
    icon = pygame.image.load('spaceship.png')
    pygame.display.set_icon(icon)
    return True

def inicializeScreen():
    # create a screen (width,height)
    screen = pygame.display.set_mode((800,600))
    return screen

def inicializePlayer():
    # Player
    start_x = 370
    start_y = 480
    playerImg = pygame.image.load('player.png')
    return playerImg, start_x, start_y