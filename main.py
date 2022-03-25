import pygame, config, math, random
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
enemyPos_x = []
enemyPos_y = []
newEnemyPos_x = []
newEnemyPos_y = []
for i in range(config.enemiesQuantity):
    enemyPos_x.append(config.enemyPos_x[i])
    enemyPos_y.append(config.enemyPos_y[i])
    newEnemyPos_x.append(enemySpeed)
    newEnemyPos_y.append(0)

def player(x,y):
    # screen.blit(Object, Position): draw Object into the screen at Position
    screen.blit(config.playerImg, (x,y))

def enemy(x,y,i):
    screen.blit(config.enemyImg[i], (x, y))

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
    for i in range(config.enemiesQuantity):
        enemyPos_x[i] += newEnemyPos_x[i]
        if enemyPos_x[i] <= 10:
            newEnemyPos_x[i] = -newEnemyPos_x[i]
            enemyPos_y[i] += 40
        elif enemyPos_x[i] >= 730:
            newEnemyPos_x[i] = -newEnemyPos_x[i]
            enemyPos_y[i] += 40

        # Collision event
        if getCollision(enemyPos_x[i], enemyPos_y[i], shooting_x, bulletPos_y):
            resetBullet()
            score += 1
            print(score)
            enemyPos_x[i] = random.randint(0, 730)
            enemyPos_y[i] = random.randint(30, 60)

        enemy(enemyPos_x[i], enemyPos_y[i], i)

    # Setting new position
    playerPos_x += newPlayerPos_x
    playerPos_y += newPlayerPos_y

    # Setting player boundaries
    if playerPos_x <= 10:
        playerPos_x = 10
    elif playerPos_x >= 730:
        playerPos_x = 730



    player(playerPos_x,playerPos_y)
    pygame.display.update()