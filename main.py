import pygame

# Inicialize pygame
pygame.init()

# create a screen (width,height)
screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerPos = (playerX,playerY)

def player():
    # screen.blit(Object, Position): draw Object into the screen at Position
    screen.blit(playerImg, playerPos)

# Game loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill((0, 0, 255))

    # Close window event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()