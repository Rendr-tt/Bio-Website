import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Screen dimensions
WIDTH = 800
HEIGHT = 500

# Snake block size
BLOCK_SIZE = 10

# Speed
SPEED = 15

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling speed
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont("bahnschrift", 25)

def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], block_size, block_size])

def display_message(msg, color, position):
    text = font.render(msg, True, color)
    screen.blit(text, position)

def game_loop():
    game_over = False
    game_close = False
    
    x = WIDTH // 2
    y = HEIGHT // 2
    dx = 0
    dy = 0
    
    snake_list = []
    snake_length = 1
    
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
    
    while not game_over:
        while game_close:
            screen.fill(BLACK)
            display_message("Game Over! Press C to Play Again or Q to Quit", RED, (WIDTH // 6, HEIGHT // 3))
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -BLOCK_SIZE
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = BLOCK_SIZE
                    dx = 0
        
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True
        
        x += dx
        y += dy
        
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        
        if len(snake_list) > snake_length:
            del snake_list[0]
        
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True
        
        draw_snake(BLOCK_SIZE, snake_list)
        pygame.display.update()
        
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
            snake_length += 1
        
        clock.tick(SPEED)
    
    pygame.quit()
    quit()

game_loop()

