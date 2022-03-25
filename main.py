import pygame, config, math, random
from init import initializeGame, initializeScreen, initializePlayer
from pygame import mixer

# Calling initializing functions
initializeGame()
game_over_flag = False
initializePlayer()
screen = initializeScreen()
# Background sound
mixer.music.load('background.wav')
mixer.music.play(-1)
# Initializing player variables
playerSpeed = config.playerSpeed
playerPos_x = config.playerPos_x
playerPos_y = config.playerPos_y
newPlayerPos_x, newPlayerPos_y = 0, 0
# Inicializing bullet variables
bulletPos_x, bulletPos_y = 0, 0
newBulletPos_x, newBulletPos_y = 0, config.bulletSpeed
bulletState = 'ready'
shooting_x = 0
# Initializing enemy variables
enemySpeed = 1
enemyPos_x = []
enemyPos_y = []
newEnemyPos_x = []
newEnemyPos_y = []
for i in range(config.enemiesQuantity):
    enemyPos_x.append(config.enemyPos_x[i])
    enemyPos_y.append(config.enemyPos_y[i])
    newEnemyPos_x.append(config.enemySpeed)
    newEnemyPos_y.append(0)

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    over_score = over_font.render("Score: " + str(score_value), True, (0, 255, 0))
    screen.blit(over_text, (200, 250))
    screen.blit(over_score, (270, 320))


def showScore(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    # screen.blit(Object, Position): draw Object into the screen at Position
    screen.blit(config.playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(config.enemyImg[i], (x, y))


def shoot(x, y):
    global bulletState
    bulletState = 'fire'
    screen.blit(config.bulletImg, (x + 16, y + 10))


def resetBullet():
    global bulletState
    global bulletPos_y
    bulletState = 'ready'
    bulletPos_y = 500


def getBulletCollision(enemy_x, enemy_y, bullet_x, bullet_y):
    global enemySpeed
    distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) + math.pow(enemy_y - bullet_y, 2))
    if distance < 30:
        collisionSound = mixer.Sound('explosion.wav')
        collisionSound.play()
        enemySpeed += 0.1
        return True


def getPlayerCollision(enemy_x, enemy_y, player_x, player_y):
    distance = math.sqrt(math.pow(enemy_x - player_x, 2) + math.pow(enemy_y - player_y, 2))
    if distance < 30:
        collisionSound = mixer.Sound('explosion.wav')
        collisionSound.play()
        return True


# Game loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill((0, 0, 255))
    # Background
    screen.blit(config.background, (0, 0))

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
                    bulletSound = mixer.Sound('laser.wav')
                    bulletSound.play()
    if bulletState == 'fire':
        shoot(shooting_x, bulletPos_y)
        bulletPos_y -= newBulletPos_y
        if bulletPos_y <= 0:
            resetBullet()

    # Enemy events
    for i in range(config.enemiesQuantity):

        # Game Over
        if getPlayerCollision(enemyPos_x[i], enemyPos_y[i], playerPos_x, playerPos_y):
            for j in range(config.enemiesQuantity):
                enemyPos_y[j] = 2000
            game_over_flag = True
            break

        # Enemy Movement
        if enemyPos_x[i] <= 5 or enemyPos_x[i] >= 730:
            newEnemyPos_x[i] = -newEnemyPos_x[i]
            enemyPos_y[i] += 40
        enemyPos_x[i] += newEnemyPos_x[i] * enemySpeed

        # Enemy Collision event
        if getBulletCollision(enemyPos_x[i], enemyPos_y[i], shooting_x, bulletPos_y):
            resetBullet()
            score_value += 1
            enemyPos_x[i] = random.randint(0, 730)
            enemyPos_y[i] = random.randint(30, 60)

        # Update enemy position
        enemy(enemyPos_x[i], enemyPos_y[i], i)

    # Update player position
    playerPos_x += newPlayerPos_x
    playerPos_y += newPlayerPos_y

    # Setting player boundaries
    if playerPos_x <= 10:
        playerPos_x = 10
    elif playerPos_x >= 730:
        playerPos_x = 730

    player(playerPos_x, playerPos_y)
    if game_over_flag:
        game_over_text()
        mixer.music.stop()
    else:
        showScore(text_x, text_y)
    pygame.display.update()
