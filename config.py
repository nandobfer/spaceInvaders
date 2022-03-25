import pygame, random

# Player starting variables
playerPos_x = 370
playerPos_y = 480
playerImg = pygame.image.load('player.png')
playerSpeed = 0.2

# Enemy starting variables
enemyPos_x = random.randint(0, 730)
enemyPos_y = random.randint(30, 60)
enemyImg = pygame.image.load('enemy.png')
enemySpeed = 0.15