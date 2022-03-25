import pygame
import config
from init import initializeGame, initializeScreen, initializePlayer

# Calling initializing functions
initializeGame()
initializePlayer()
screen = initializeScreen()
# Initializing player variables
playerSpeed = config.playerSpeed
playerPos_x = config.playerPos_x
playerPos_y = config.playerPos_y
newPlayerPos_x, newPlayerPos_y = 0, 0
# Initializing enemy variables
enemySpeed = config.enemySpeed
enemyPos_x = config.enemyPos_x
enemyPos_y = config.enemyPos_y
newenemyPos_x, newenemyPos_y = 0, 0

def player(x,y):
    # screen.blit(Object, Position): draw Object into the screen at Position
    screen.blit(config.playerImg, (x,y))

def enemy(x,y):
    screen.blit(config.enemyImg, (x, y))

# Game loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill((0, 0, 255))

    for event in pygame.event.get():
        # Close window event
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                newPlayerPos_x = -playerSpeed
            elif event.key == pygame.K_RIGHT:
                newPlayerPos_x = playerSpeed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                newPlayerPos_x = 0

    playerPos_x += newPlayerPos_x
    if playerPos_x <= 10:
        playerPos_x = 10
    elif playerPos_x >= 730:
        playerPos_x = 730
    player(playerPos_x,playerPos_y)
    enemy(enemyPos_x,enemyPos_y)
    pygame.display.update()