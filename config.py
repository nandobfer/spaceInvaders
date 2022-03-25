import pygame, random

# Background
import init

background = pygame.image.load('background.jpg').convert()
background = pygame.transform.scale(background, init.resolution)

# Player starting variables
playerPos_x = 0.4625 * init.resolution[0]
playerPos_y = 0.8 * init.resolution[1]
playerImg = pygame.image.load('player.png').convert_alpha()
if init.resolution < (800,600):
    playerImg = pygame.transform.scale(playerImg, (0.08 * init.resolution[0], 0.1067 * init.resolution[1]))
playerSpeed = 0.4
bulletImg = pygame.image.load('bullet.png').convert_alpha()
bulletSpeed = 1

# Enemy starting variables
enemiesQuantity = 10
enemySpeed = 0.15
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
