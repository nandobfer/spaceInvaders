from init import *
inicializeGame()
playerImg, playerPos_x, playerPos_y = inicializePlayer()
screen = inicializeScreen()


def player(x,y):
    # screen.blit(Object, Position): draw Object into the screen at Position
    screen.blit(playerImg, (x,y))

# Game loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill((0, 0, 255))

    # Close window event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player(playerPos_x,playerPos_y)
    pygame.display.update()