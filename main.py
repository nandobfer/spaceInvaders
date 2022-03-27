import pygame, math, random, init
from pygame import mixer
import config

game_over_flag = False
pause = False
running = False
start_menu = True
# Initializing player variables
playerSpeed = config.playerSpeed
playerPos_x = config.playerPos_x
playerPos_y = config.playerPos_y
newPlayerPos_x, newPlayerPos_y = 0, 0

# Inicializing bullet variables
shooting_x, bulletPos_x, bulletPos_y, newBulletPos_x, newBulletPos_y = 0, 0, 0, 0, config.bulletSpeed
bulletState = 'ready'

# Initializing enemy variables
enemySpeed = 1
enemyPos_x = config.enemyPos_x[:]
enemyPos_y = config.enemyPos_y[:]
newEnemyPos_x = config.enemyNewPos_x[:]
newEnemyPos_y = config.enemyPos_y[:]

# Score
score_value = 0


def game_over_text():
    game_over_text = config.game_over_font.render("GAME OVER", True, (255, 255, 255))
    game_over_score = config.game_over_font.render("Score: " + str(score_value), True, (0, 255, 0))
    init.screen.blit(game_over_text, (0.28 * init.resolution[0], 0.35 * init.resolution[1]))
    init.screen.blit(game_over_score, (0.35 * init.resolution[0], 0.45 * init.resolution[1]))


def showScore(x, y):
    score = config.text.render("Score: " + str(score_value), True, (255, 255, 255))
    init.screen.blit(score, (x, y))


def showSpeed(x, y):
    speedText = config.text.render("Speed " + str(round(enemySpeed, 1)), True, (255, 255, 255))
    init.screen.blit(speedText, (x, y))


def player(x, y):
    # init.screen.blit(Object, Position): draw Object into the init.screen at Position
    init.screen.blit(config.playerImg, (x, y))


def enemy(x, y, i):
    init.screen.blit(config.enemyImg[i], (x, y))


def shoot(x, y):
    global bulletState
    bulletState = 'fire'
    init.screen.blit(config.bulletImg, (x + 24, y + 10))


def resetBullet():
    global bulletState
    global bulletPos_y
    bulletState = 'ready'
    bulletPos_y = 500


def getBulletCollision(enemy_x, enemy_y, bullet_x, bullet_y):
    global enemySpeed
    distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) + math.pow(enemy_y - bullet_y, 2))
    if distance < config.enemyHitbox:
        collisionSound = mixer.Sound('explosion.wav')
        collisionSound.play()
        enemySpeed += 0.1
        return True


def getPlayerCollision(enemy_x, enemy_y, player_x, player_y):
    distance = math.sqrt(math.pow(enemy_x - player_x, 2) + math.pow(enemy_y - player_y, 2))
    if distance < config.playerHitbox:
        collisionSound = mixer.Sound('explosion.wav')
        collisionSound.play()
        return True


# PAUSE MENU
def paused():
    pauseText = config.largeText.render(("Paused"), True, (255, 255, 255))
    init.screen.blit(pauseText, (0.35 * init.resolution[0], 0.4 * init.resolution[1]))
    mixer.music.pause()
    menu()


def menu():
    global pause, running, start_menu
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Unpause Button
                if config.unpause_x <= mouse[0] <= config.unpause_x + 200 and config.unpause_y <= mouse[
                    1] <= config.unpause_y + 40:
                    pause = False
                    mixer.music.unpause()
                # Restart Button
                if config.restart_x <= mouse[0] <= config.restart_x + 200 and config.restart_y <= mouse[
                    1] <= config.restart_y + 40:
                    restart()
                    mixer.music.unpause()
                # Quit Button
                if config.quit_x <= mouse[0] <= config.quit_x + 200 and config.quit_y <= mouse[1] <= config.quit_y + 40:
                    running = False
                    start_menu = False
                    return False

        mouse = pygame.mouse.get_pos()

        # Unpause Button Rect
        if config.unpause_x <= mouse[0] <= config.unpause_x + 200 and config.unpause_y <= mouse[
            1] <= config.unpause_y + 40:
            pygame.draw.rect(init.screen, (170, 170, 170), [config.unpause_x, config.unpause_y, 200, 40])
        else:
            pygame.draw.rect(init.screen, (100, 100, 100), [config.unpause_x, config.unpause_y, 200, 40])
        # Unpause Button Text
        init.screen.blit(config.buttonUnpause, (config.unpause_x + 15, config.unpause_y))

        # Restart Button Rect
        if config.restart_x <= mouse[0] <= config.restart_x + 200 and config.restart_y <= mouse[
            1] <= config.restart_y + 40:
            pygame.draw.rect(init.screen, (170, 170, 170), [config.restart_x, config.restart_y, 200, 40])
        else:
            pygame.draw.rect(init.screen, (100, 100, 100), [config.restart_x, config.restart_y, 200, 40])
        # Restart Button Text
        init.screen.blit(config.buttonRestart, (config.restart_x + 15, config.restart_y))

        # Quit Button Rect
        if config.quit_x <= mouse[0] <= config.quit_x + 200 and config.quit_y <= mouse[
            1] <= config.quit_y + 40:
            pygame.draw.rect(init.screen, (170, 170, 170), [config.quit_x, config.quit_y, 200, 40])
        else:
            pygame.draw.rect(init.screen, (100, 100, 100), [config.quit_x, config.quit_y, 200, 40])
        # Quit Button Text
        init.screen.blit(config.buttonQuit, (config.quit_x + 55, config.quit_y))

        pygame.display.update()


def restart():
    global game_over_flag, playerSpeed, playerPos_x, playerPos_y, newPlayerPos_x, newPlayerPos_y, shooting_x, bulletPos_x, bulletPos_y, newBulletPos_x, newBulletPos_y, bulletState, score_value
    global pause, enemySpeed, enemyPos_x, enemyPos_y, newEnemyPos_x, newEnemyPos_y
    init.initializeGame()
    init.screen = init.initializeScreen()
    mixer.music.load('background.wav')
    mixer.music.play(-1)
    game_over_flag = False
    pause = False
    playerSpeed = config.playerSpeed
    playerPos_x = config.playerPos_x
    playerPos_y = config.playerPos_y
    newPlayerPos_x, newPlayerPos_y = 0, 0
    shooting_x, bulletPos_x, bulletPos_y, newBulletPos_x, newBulletPos_y = 0, 0, 0, 0, config.bulletSpeed
    bulletState = 'ready'
    enemySpeed = 1
    enemyPos_x = config.enemyPos_x[:]
    enemyPos_y = config.enemyPos_y[:]
    newEnemyPos_x = config.enemyNewPos_x[:]
    newEnemyPos_y = config.enemyPos_y[:]
    score_value = 0
    game()


def game():
    global game_over_flag, playerSpeed, playerPos_x, playerPos_y, newPlayerPos_x, newPlayerPos_y, shooting_x, bulletPos_x, bulletPos_y, newBulletPos_x, newBulletPos_y, bulletState, score_value
    # Music
    mixer.music.load('background.wav')
    mixer.music.play(-1)
    mixer.music.set_volume(mixer.music.get_volume() / 4)
    # Game loop
    global running
    running = True
    while running:
        # RGB - Red, Green, Blue
        # init.screen.fill((0, 0, 255))
        # Background
        init.screen.blit(config.background, (0, 0))

        for event in pygame.event.get():
            # Close window event
            if event.type == pygame.QUIT:
                running = False

            # Player movement events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    newPlayerPos_x = -playerSpeed
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    newPlayerPos_x = playerSpeed
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    newPlayerPos_y = -playerSpeed
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    newPlayerPos_y = playerSpeed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    newPlayerPos_x = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                    newPlayerPos_y = 0

            # Mouse events
            # PAUSE
            if event.type == pygame.MOUSEBUTTONDOWN:
                if config.pause_x <= mouse[0] <= config.pause_x + 140 and config.pause_y <= mouse[
                    1] <= config.pause_y + 40:
                    paused()

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
            if enemyPos_x[i] <= 5 or enemyPos_x[i] >= 0.9125 * init.resolution[0]:
                newEnemyPos_x[i] = -newEnemyPos_x[i]
                enemyPos_y[i] += 40
            enemyPos_x[i] += newEnemyPos_x[i] * enemySpeed

            # Enemy Collision event
            if getBulletCollision(enemyPos_x[i], enemyPos_y[i], shooting_x, bulletPos_y):
                resetBullet()
                score_value += 1
                enemyPos_x[i] = random.randint(0, int(0.9125 * init.resolution[0]))
                enemyPos_y[i] = random.randint(5, int(0.1 * init.resolution[1]))

            # Update enemy position
            enemy(enemyPos_x[i], enemyPos_y[i], i)

        # Update player position
        playerPos_x += newPlayerPos_x
        playerPos_y += newPlayerPos_y

        # Setting player boundaries
        if playerPos_x <= 10:
            playerPos_x = 10
        if playerPos_x >= 0.93 * init.resolution[0]:
            playerPos_x = 0.93 * init.resolution[0]
        if playerPos_y <= 10:
            playerPos_y = 10
        if playerPos_y >= 0.9125 * init.resolution[1]:
            playerPos_y = 0.9125 * init.resolution[1]

        player(playerPos_x, playerPos_y)
        if game_over_flag:
            game_over_text()
            mixer.music.stop()
            startMenu()
        else:
            showScore(config.score_x, config.score_y)
            showSpeed(0.8125 * init.resolution[0] - config.score_x, config.score_y)

        # Buttons
        mouse = pygame.mouse.get_pos()
        # Pause Button Rect
        if config.pause_x <= mouse[0] <= config.pause_x + 140 and config.pause_y <= mouse[1] <= config.pause_y + 40:
            pygame.draw.rect(init.screen, (170, 170, 170), [config.pause_x, config.pause_y, 140, 40])
        else:
            pygame.draw.rect(init.screen, (100, 100, 100), [config.pause_x, config.pause_y, 140, 40])
        # Pause Button Text
        init.screen.blit(config.buttonPause, (config.pause_x + 12.5, config.pause_y))

        pygame.display.update()

    return True


def startMenu():
    global start_menu, running
    config.enemiesQuantity = 10
    difficulty_text = ''
    difficulty_active = False
    screen_alphaed = pygame.Surface(init.resolution)
    screen_alphaed.set_alpha(235)
    screen_alphaed.fill((40, 40, 40))
    while start_menu:
        init.screen.blit(config.background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_menu = False
                running = False
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Difficulty chooser, if clicked, activate chooser
                if config.unpause_x <= mouse[0] <= config.unpause_x + 200 and config.unpause_y <= mouse[
                    1] <= config.unpause_y + 40:
                    difficulty_active = True
                else:
                    difficulty_active = False
                # Start Button
                if config.restart_x <= mouse[0] <= config.restart_x + 200 and config.restart_y <= mouse[
                    1] <= config.restart_y + 40:
                    if game_over_flag:
                        restart()
                    else:
                        game()
                    start_menu = False
                # Quit Button
                if config.quit_x <= mouse[0] <= config.quit_x + 200 and config.quit_y <= mouse[1] <= config.quit_y + 40:
                    start_menu = False
                    running = False
                    return False

            # Input Check
            if event.type == pygame.KEYDOWN and difficulty_active:
                if event.key == pygame.K_RETURN:
                    if difficulty_text:
                        config.enemiesQuantity = int(difficulty_text)
                    difficulty_active = False
                elif event.key == pygame.K_BACKSPACE:
                    difficulty_text = difficulty_text[:-1]
                else:
                    difficulty_text += event.unicode

        mouse = pygame.mouse.get_pos()

        # Game Over Screen
        if game_over_flag:
            game_over_text()

        # Start Button Rect
        if config.restart_x <= mouse[0] <= config.restart_x + 200 and config.restart_y <= mouse[
            1] <= config.restart_y + 40:
            pygame.draw.rect(init.screen, (170, 170, 170), [config.restart_x, config.restart_y, 200, 40])
        else:
            pygame.draw.rect(init.screen, (100, 100, 100), [config.restart_x, config.restart_y, 200, 40])
        # Start Button Text
        init.screen.blit(config.buttonStart, (config.restart_x + 50, config.restart_y))

        # Quit Button Rect
        if config.quit_x <= mouse[0] <= config.quit_x + 200 and config.quit_y <= mouse[
            1] <= config.quit_y + 40:
            pygame.draw.rect(init.screen, (170, 170, 170), [config.quit_x, config.quit_y, 200, 40])
        else:
            pygame.draw.rect(init.screen, (100, 100, 100), [config.quit_x, config.quit_y, 200, 40])
        # Quit Button Text
        init.screen.blit(config.buttonQuit, (config.quit_x + 55, config.quit_y))

        # Difficulty Chooser Rect
        if config.unpause_x <= mouse[0] <= config.unpause_x + 200 and config.unpause_y <= mouse[
            1] <= config.unpause_y + 40 or difficulty_active:
            if difficulty_active:
                # Black Transparent Screen
                init.screen.blit(screen_alphaed, (0, 0))
            pygame.draw.rect(init.screen, (170, 170, 170), [config.unpause_x, config.unpause_y, 200, 40])
        else:
            pygame.draw.rect(init.screen, (100, 100, 100), [config.unpause_x, config.unpause_y, 200, 40])

        # Difficulty Chooser Text
        init.screen.blit(config.enemiesButton, (config.difficulty_text_x + 85, config.difficulty_text_y))
        # Difficult Chosen Text
        difficulty_text_show = config.text.render(difficulty_text, True, (255, 255, 255))
        init.screen.blit(difficulty_text_show, (config.unpause_x + 85, config.unpause_y))

        pygame.display.update()


startMenu()
