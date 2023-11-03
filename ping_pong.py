import pygame
import sys
import random

# Initializing pygame
pygame.init()

# Frames per second
clock = pygame.time.Clock()

# Dimensions for window
width = 900
height = 600

# Creating game window
screen = pygame.display.set_mode((width, height))

# Title and icon
pygame.display.set_caption("hamza o anas l7a9din")

# Game rectangles
ball = pygame.Rect(width / 2 - 15, height / 2 - 15, 30, 30)
player1 = pygame.Rect(width - 20, height / 2 - 70, 10, 140)
player2 = pygame.Rect(10, height / 2 - 70, 10, 140)

# Game variables
ball_speedx = 6 * random.choice((1, -1))
ball_speedy = 6 * random.choice((1, -1))
player1_speed = 0
player2_speed = 6
player1_score = 0
player2_score = 0

# Function for ball movement
def ball_movement():
    global ball_speedx, ball_speedy, player1_score, player2_score
    ball.x += ball_speedx
    ball.y += ball_speedy

    # Bouncing the ball
    if ball.top <= 0 or ball.bottom >= height:
        ball_speedy *= -1
    if ball.left <= 0:
        player1_score += 1
        ball_restart()
    if ball.right >= width:
        player2_score += 1
        ball_restart()

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speedx *= -1

# Function for player1 movement
def player1_movement():
    global player1_speed
    player1.y += player1_speed
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= height:
        player1.bottom = height

# Function for player2 movement
def player2_movement():
    global player2_speed
    if player2.top < ball.y:
        player2.top += player2_speed
    if player2.bottom > ball.y:
        player2.bottom -= player2_speed
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= height:
        player2.bottom = height

# Function to reset the ball position and randomize ball speed
def ball_restart():
    global ball_speedx, ball_speedy
    ball.center = (width / 2, height / 2)
    ball_speedy = 6 * random.choice((1, -1))
    ball_speedx = 6 * random.choice((1, -1))

# Function to set the bot difficulty
def set_bot_difficulty(difficulty):
    global player2_speed
    if difficulty == "easy":
        player2_speed = 3
    elif difficulty == "normal":
        player2_speed = 6
    elif difficulty == "hard":
        player2_speed = 9
    elif difficulty == "insane":
        player2_speed = 15
    elif difficulty == "alae":
        player2_speed = 20

# Function to choose difficulty
def choose_difficulty():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    set_bot_difficulty("easy")
                    return
                elif event.key == pygame.K_n:
                    set_bot_difficulty("normal")
                    return
                elif event.key == pygame.K_h:
                    set_bot_difficulty("hard")
                    return
                elif event.key == pygame.K_i:
                    set_bot_difficulty("insane")
                    return
                elif event.key == pygame.K_a:
                    set_bot_difficulty("alae")
                    return
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont("calibri", 25)
        difficulty_text = font.render("Choose Difficulty:", True, (255, 255, 255))
        screen.blit(difficulty_text, (width / 2 - 100, height / 2 - 90))
        easy_text = font.render("Press 'E' for Easy", True, (255, 255, 255))
        screen.blit(easy_text, (width / 2 - 100, height / 2))
        normal_text = font.render("Press 'N' for Normal", True, (255, 255, 255))
        screen.blit(normal_text, (width / 2 - 100, height / 2 + 50))
        hard_text = font.render("Press 'H' for Hard", True, (255, 255, 255))
        screen.blit(hard_text, (width / 2 - 100, height / 2 + 100))
        insane_text = font.render("Press 'I' for Insane", True, (255, 255, 255))
        screen.blit(insane_text, (width / 2 - 100, height / 2 + 150))
        alae_text = font.render("Press 'A' for Alae the Boss", True, (150, 25, 5))
        screen.blit(alae_text, (width / 2 - 100, height / 2 + 200))


        pygame.display.update()
        clock.tick(60)

# Call the function to choose difficulty before starting the game
choose_difficulty()

# Font variable
font = pygame.font.SysFont("calibri", 25)

# Game Loop
while True:
    for event in pygame.event.get():
        # Checking for quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Checking for key pressed event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player1_speed += 8
            if event.key == pygame.K_UP:
                player1_speed -= 8
        # Checking for key released event
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player1_speed -= 8
            if event.key == pygame.K_UP:
                player1_speed += 8

    # Calling the functions
    ball_movement()
    player1_movement()
    player2_movement()

    # Setting the score condition
    if ball.x < 0:
        player1_score += 1
        ball_restart()
    elif ball.x > width:
        player2_score += 1
        ball_restart()

    # Visuals
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (220, 220, 220), player1)
    pygame.draw.rect(screen, (220, 220, 220), player2)
    pygame.draw.ellipse(screen, (220, 220, 220), ball)
    pygame.draw.aaline(screen, (220, 220, 220), (width / 2, 0), (width / 2, height))

    # Drawing the score
    player1_text = font.render("Score: " + str(player1_score), True, (255, 255, 255))
    screen.blit(player1_text, [600, 50])
    player2_text = font.render("Score: " + str(player2_score), True, (255, 255, 255))
    screen.blit(player2_text, [300, 50])

    # Updating the game window
    pygame.display.update()

    # 60 frames per second
    clock.tick(60)
