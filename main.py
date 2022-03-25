import pygame, config, math
from init import initializeGame, initializeScreen, initializePlayer

# Calling initializing functions
score = 0
initializeGame()
initializePlayer()
screen = initializeScreen()
# Initializing player variables
playerSpeed = config.playerSpeed
playerPos_x = config.playerPos_x
playerPos_y = config.playerPos_y
newPlayerPos_x, newPlayerPos_y = 0, 0
# Inicializing bullet variables
bulletPos_x, bulletPos_y = 0, playerPos_y
newBulletPos_x, newBulletPos_y = 0, config.bulletSpeed
bulletState = 'ready'
shooting_x = 0
# Initializing enemy variables
enemySpeed = config.enemySpeed
enemyPos_x = config.enemyPos_x
enemyPos_y = config.enemyPos_y
newEnemyPos_x, newEnemyPos_y = enemySpeed, 0

# def enemyMove(enemy_x, enemy_y, player_x, player_y):
#     if player_x - enemy_x > 0:
#         x = enemySpeed
#     elif player_x - enemy_x < 0:
#         x = -enemySpeed
#     else:
#         x = 0
#     if player_y - enemy_y > 0:
#         y = enemySpeed
#     elif player_y - enemy_y < 0:
#         y = -enemySpeed
#     else:
#         y = 0
#     return x, y

def player(x,y):
    # screen.blit(Object, Position): draw Object into the screen at Position
    screen.blit(config.playerImg, (x,y))

def enemy(x,y):
    screen.blit(config.enemyImg, (x, y))

def shoot(x, y):
    global bulletState
    bulletState = 'fire'
    screen.blit(config.bulletImg, (x+16,y+10))

def resetBullet():
    global bulletState
    global bulletPos_y
    bulletState = 'ready'
    bulletPos_y = 500

def getCollision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) + math.pow(enemy_y - bullet_y, 2))
    if distance < 30:
        return True


# Game loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill((0, 0, 255))
    # Background
    screen.blit(config.background, (0,0))

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

    # Bullet event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bulletState == 'ready':
                    shooting_x = playerPos_x
                    bulletPos_y = playerPos_y
                    shoot(shooting_x, playerPos_y)
    if bulletState == 'fire':
        shoot(shooting_x,bulletPos_y)
        bulletPos_y -= newBulletPos_y
        if bulletPos_y <= 0:
            resetBullet()


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

    # Collision event
    if getCollision(enemyPos_x, enemyPos_y, shooting_x, bulletPos_y):
        resetBullet()
        score += 1
        print(score)

    player(playerPos_x,playerPos_y)
    enemy(enemyPos_x,enemyPos_y)
    pygame.display.update()