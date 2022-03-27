import pygame, random, init

# Background
background = pygame.image.load('background.jpg').convert()
background = pygame.transform.scale(background, init.resolution)

# Player starting variables
playerPos_x = 0.4625 * init.resolution[0]
playerPos_y = 0.8 * init.resolution[1]
playerImg = pygame.image.load('player.png').convert_alpha()
if init.resolution < (800, 600):
    playerImg = pygame.transform.scale(playerImg, (0.08 * init.resolution[0], 0.1067 * init.resolution[1]))
playerSpeed = 0.4
playerHitbox = 50
bulletImg = pygame.image.load('bullet.png').convert_alpha()
bulletSpeed = 1

# Enemy starting variables
enemiesQuantity = 100
enemySpeed = 0.15
enemyHitbox = 30
enemyPos_x = []
enemyPos_y = []
enemyNewPos_x = []
enemyNewPos_y = []
enemyImg = []
for i in range(enemiesQuantity):
    enemyImg.append(pygame.image.load('enemy.png').convert_alpha())
    if init.resolution < (800, 600):
        enemyImg[i] = pygame.transform.scale(enemyImg[i], (0.08 * init.resolution[0], 0.1067 * init.resolution[1]))
    enemyPos_x.append(random.randint(40, 660))
    enemyPos_y.append(random.randint(10, 90))
    enemyNewPos_x.append(enemySpeed)
    enemyNewPos_y.append(0)

# General Text
text = pygame.font.Font('walkthemoon.ttf', int(0.04 * init.resolution[0]))
largeText = pygame.font.Font('walkthemoon.ttf', int(0.08 * init.resolution[0]))

# Score
score_x = 10
score_y = 10

# Game Over
game_over_font = pygame.font.Font('walkthemoon.ttf', int(0.08 * init.resolution[0]))

# Buttons
pause_x = 40 + 0.38 * init.resolution[0]
pause_y = 10
unpause_x = 0.4 * init.resolution[0]
unpause_y = 10 + init.screen.get_height() * 3 / 5
difficulty_text_x = 0.34 * init.resolution[0]
difficulty_text_y = 10 + init.screen.get_height() * 2.69 / 5
restart_x = 0.4 * init.resolution[0]
restart_y = 10 + init.screen.get_height() * 3.5 / 5
quit_x = 0.4 * init.resolution[0]
quit_y = 10 + init.screen.get_height() * 4 / 5
buttonQuit = text.render("Quit", True, (255, 255, 255))
buttonPause = text.render("Pause", True, (255, 255, 255))
buttonUnpause = text.render("Unpause", True, (255, 255, 255))
buttonRestart = text.render("Restart", True, (255, 255, 255))
buttonStart = text.render("Play", True, (255, 255, 255))
enemiesButton = text.render("Enemies", True, (255, 255, 255))
