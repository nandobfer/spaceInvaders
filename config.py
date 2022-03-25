import pygame, random
# Background
background = pygame.image.load('background.jpg')

# Player starting variables
playerPos_x = 370
playerPos_y = 480
playerImg = pygame.image.load('player.png')
playerSpeed = 0.2
bulletImg = pygame.image.load('bullet.png')
bulletSpeed = 1

# Enemy starting variables
enemiesQuantity = 6
enemySpeed = 0.15
enemyPos_x = []
enemyPos_y = []
enemyImg = []
for i in range(enemiesQuantity):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyPos_x.append(random.randint(0, 730))
    enemyPos_y.append(random.randint(30, 60))
