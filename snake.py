
# importing libraries
import pygame
import time
import random

new_snake_speed = 15

# Window size
new_window_x = 720
new_window_y = 480

# defining colors
new_black = pygame.Color(0, 0, 0)
new_white = pygame.Color(255, 255, 255)
new_red = pygame.Color(255, 0, 0)
new_green = pygame.Color(0, 255, 0)
new_blue = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Retro Snake')
new_game_window = pygame.display.set_mode((new_window_x, new_window_y))

# FPS (frames per second) controller
new_fps = pygame.time.Clock()

# defining snake default position
new_snake_position = [100, 50]

# defining first 4 blocks of snake body
new_snake_body = [[100, 50],
                  [90, 50],
                  [80, 50],
                  [70, 50]
                  ]
# fruit position
new_fruit_position = [random.randrange(1, (new_window_x//10)) * 10,
                      random.randrange(1, (new_window_y//10)) * 10]

new_fruit_spawn = True

# setting default snake direction towards
# right
new_direction = 'RIGHT'
new_change_to = new_direction

# initial score
new_score = 0

# displaying Score function
def show_score(choice, color, font, size):

    # creating font object score_font
    new_score_font = pygame.font.SysFont(font, size)

    # create the display surface object
    # score_surface
    new_score_surface = new_score_font.render('Score : ' + str(new_score), True, color)

    # create a rectangular object for the text
    # surface object
    new_score_rect = new_score_surface.get_rect()

    # displaying text
    new_game_window.blit(new_score_surface, new_score_rect)

# game over function
def game_over():

    # creating font object my_font
    new_my_font = pygame.font.SysFont('times new roman', 50)

    # creating a text surface on which text
    # will be drawn
    new_game_over_surface = new_my_font.render(
        'Your Score is : ' + str(new_score), True, new_red)

    # create a rectangular object for the text
    # surface object
    new_game_over_rect = new_game_over_surface.get_rect()

    # setting position of the text
    new_game_over_rect.midtop = (new_window_x/2, new_window_y/4)

    # blit will draw the text on screen
    new_game_window.blit(new_game_over_surface, new_game_over_rect)
    pygame.display.flip()

    # after 2 seconds we will quit the program
    time.sleep(2)

    # deactivating pygame library
    pygame.quit()

    # quit the program
    quit()


# Main Function
while True:

    # handling key events
    for new_event in pygame.event.get():
        if new_event.type == pygame.KEYDOWN:
            if new_event.key == pygame.K_UP :
                new_change_to = 'UP'
            if new_event.key == pygame.K_DOWN:
                new_change_to = 'DOWN'
            if new_event.key == pygame.K_LEFT:
                new_change_to = 'LEFT'
            if new_event.key == pygame.K_RIGHT:
                new_change_to = 'RIGHT'

    # If two keys pressed simultaneously
    # we don't want snake to move into two
    # directions simultaneously
    if new_change_to == 'UP' and new_direction != 'DOWN':
        new_direction = 'UP'
    if new_change_to == 'DOWN' and new_direction != 'UP':
        new_direction = 'DOWN'
    if new_change_to == 'LEFT' and new_direction != 'RIGHT':
        new_direction = 'LEFT'
    if new_change_to == 'RIGHT' and new_direction != 'LEFT':
        new_direction = 'RIGHT'

    # Moving the snake
    if new_direction == 'UP':
        new_snake_position[1] -= 10
    if new_direction == 'DOWN':
        new_snake_position[1] += 10
    if new_direction == 'LEFT':
        new_snake_position[0] -= 10
    if new_direction == 'RIGHT':
        new_snake_position[0] += 10

    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    new_snake_body.insert(0, list(new_snake_position))
    if new_snake_position[0] == new_fruit_position[0] and new_snake_position[1] == new_fruit_position[1]:
        new_score += 10
        new_fruit_spawn = False
    else:
        new_snake_body.pop()

    if not new_fruit_spawn:
        new_fruit_position = [random.randrange(1, (new_window_x//10)) * 10,
                              random.randrange(1, (new_window_y//10)) * 10]

    new_fruit_spawn = True
    new_game_window.fill(new_black)

    for pos in new_snake_body:
        pygame.draw.rect(new_game_window, new_green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(new_game_window, new_white, pygame.Rect(
        new_fruit_position[0], new_fruit_position[1], 10, 10))

    # Game Over conditions
    if new_snake_position[0] < 0 or new_snake_position[0] > new_window_x-10:
        game_over()
    if new_snake_position[1] < 0 or new_snake_position[1] > new_window_y-10:
        game_over()

    # Touching the snake body
    for block in new_snake_body[1:]:
        if new_snake_position[0] == block[0] and new_snake_position[1] == block[1]:
            game_over()

    # displaying score continuously
    show_score(1, new_white, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    new_fps.tick(new_snake_speed)
