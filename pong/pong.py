import pygame, sys

# Setup
pygame.init()
clock = pygame.time.Clock()

# Settings
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1028
BALL_HEIGHT = 30
BALL_WIDTH = 30
PLAYER_HEIGHT = 100
PLAYER_WIDTH = 10
PLAYER_SPEED = 0
PLAYER_SCORE = 0 
OPPONENT_SPEED = 7
OPPONENT_SCORE = 0
BALL_X_SPEED = 7
BALL_Y_SPEED = 7
FPS = 60

# Game attributes
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ping Pong')
ball = pygame.Rect(SCREEN_WIDTH/2 - BALL_WIDTH/2, SCREEN_HEIGHT/2 - BALL_HEIGHT, BALL_HEIGHT, BALL_WIDTH)
player = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT/2 - PLAYER_HEIGHT/2, PLAYER_WIDTH, PLAYER_HEIGHT)
opponent = pygame.Rect(10, SCREEN_HEIGHT/2 - PLAYER_HEIGHT/2, PLAYER_WIDTH, PLAYER_HEIGHT)
bg_color = (0, 0, 0)
light_grey = (200, 200, 200)

# Score font
game_font = pygame.font.Font("freesansbold.ttf", 28)

# Functions
def ball_restart():
    global BALL_X_SPEED, BALL_Y_SPEED
    ball.center = (SCREEN_WIDTH/2 - BALL_WIDTH/2, SCREEN_HEIGHT/2 - BALL_HEIGHT)
    BALL_X_SPEED *= -1
    BALL_Y_SPEED *= -1


def ball_animation():
    global BALL_X_SPEED, BALL_Y_SPEED, PLAYER_SCORE, OPPONENT_SCORE
    ball.x += BALL_X_SPEED
    ball.y += BALL_Y_SPEED

    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        BALL_Y_SPEED *= -1
    if ball.left <= 0:
        PLAYER_SCORE += 1
        ball_restart()

    if ball.right >= SCREEN_WIDTH: 
        OPPONENT_SCORE += 1
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        BALL_X_SPEED *= -1

def player_animation():
    player.y += PLAYER_SPEED
    if player.top <= 0:
        player.top = 0
    if player.bottom >= SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT
    
def opponent_animation():
    if opponent.top <= ball.y:
        opponent.top += OPPONENT_SPEED
    if opponent.bottom >= ball.y:
        opponent.bottom -= OPPONENT_SPEED
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= SCREEN_HEIGHT:
        opponent.bottom = SCREEN_HEIGHT

# Game Loop
while True:
    # Reading inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                PLAYER_SPEED -= 7
            if event.key == pygame.K_DOWN:
                PLAYER_SPEED += 7
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                PLAYER_SPEED += 7
            if event.key == pygame.K_DOWN:
                PLAYER_SPEED -= 7

    ball_animation()
    player_animation()
    opponent_animation()

    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (SCREEN_WIDTH/2, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT))

    player_score = game_font.render(f"{PLAYER_SCORE}", False, light_grey)
    screen.blit(player_score, (SCREEN_WIDTH * 0.75, SCREEN_HEIGHT * 0.1))

    opponent_score = game_font.render(f"{OPPONENT_SCORE}", False, light_grey)
    screen.blit(opponent_score, (SCREEN_WIDTH * 0.25, SCREEN_HEIGHT * 0.1))

    pygame.display.flip()
    clock.tick(FPS)