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
newEnemyPos_x, newEnemyPos_y = enemySpeed, 0

def enemyMove(enemy_x, enemy_y, player_x, player_y):
    if player_x - enemy_x > 0:
        x = enemySpeed
    elif player_x - enemy_x < 0:
        x = -enemySpeed
    else:
        x = 0
    if player_y - enemy_y > 0:
        y = enemySpeed
    elif player_y - enemy_y < 0:
        y = -enemySpeed
    else:
        y = 0
    return x, y

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

        # Player movement events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                newPlayerPos_x = -playerSpeed
            if event.key == pygame.K_RIGHT:
                newPlayerPos_x = playerSpeed
            if event.key == pygame.K_UP:
                newPlayerPos_y = -playerSpeed
            if event.key == pygame.K_DOWN:
                newPlayerPos_y = playerSpeed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                newPlayerPos_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                newPlayerPos_y = 0

    # Enemy movement events
    # newEnemyPos_x, newEnemyPos_y = enemyMove(enemyPos_x, enemyPos_y, playerPos_x, playerPos_y)

    # Setting new position
    playerPos_x += newPlayerPos_x
    playerPos_y += newPlayerPos_y
    enemyPos_x += newEnemyPos_x
    # enemyPos_y += newEnemyPos_y

    # Setting boundaries
    if playerPos_x <= 10:
        playerPos_x = 10
    elif playerPos_x >= 730:
        playerPos_x = 730    
    if enemyPos_x <= 10:
        enemyPos_x = 10
        newEnemyPos_x = -newEnemyPos_x
        enemyPos_y += 40
    elif enemyPos_x >= 730:
        enemyPos_x = 730
        newEnemyPos_x = -newEnemyPos_x
        enemyPos_y += 40

    player(playerPos_x,playerPos_y)
    enemy(enemyPos_x,enemyPos_y)
    pygame.display.update()