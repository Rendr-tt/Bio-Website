import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30
COLUMNS = WIDTH // BLOCK_SIZE
ROWS = HEIGHT // BLOCK_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (128, 0, 128)]

# Tetrimino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]]   # J
]

# Tetromino class
class Tetromino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = COLUMNS // 2 - len(self.shape[0]) // 2
        self.y = 0
    
    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

def check_collision(grid, shape, x, y):
    for row_idx, row in enumerate(shape):
        for col_idx, cell in enumerate(row):
            if cell:
                new_x, new_y = x + col_idx, y + row_idx
                if new_x < 0 or new_x >= COLUMNS or new_y >= ROWS or grid[new_y][new_x]:
                    return True
    return False

def merge_tetromino(grid, tetromino):
    for row_idx, row in enumerate(tetromino.shape):
        for col_idx, cell in enumerate(row):
            if cell:
                grid[tetromino.y + row_idx][tetromino.x + col_idx] = tetromino.color

def clear_lines(grid):
    return [row for row in grid if any(cell == 0 for cell in row)] + [[0] * COLUMNS] * (ROWS - len(grid))

def draw_grid(screen, grid):
    screen.fill(BLACK)
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, cell, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.flip()

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    grid = [[0] * COLUMNS for _ in range(ROWS)]
    current_tetromino = Tetromino()
    running = True
    fall_time = 0

    while running:
        screen.fill(BLACK)
        fall_time += clock.get_rawtime()
        clock.tick(30)
        
        if fall_time > 500:
            fall_time = 0
            if not check_collision(grid, current_tetromino.shape, current_tetromino.x, current_tetromino.y + 1):
                current_tetromino.y += 1
            else:
                merge_tetromino(grid, current_tetromino)
                grid = clear_lines(grid)
                current_tetromino = Tetromino()
                if check_collision(grid, current_tetromino.shape, current_tetromino.x, current_tetromino.y):
                    running = False  # Game over
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not check_collision(grid, current_tetromino.shape, current_tetromino.x - 1, current_tetromino.y):
                    current_tetromino.x -= 1
                elif event.key == pygame.K_RIGHT and not check_collision(grid, current_tetromino.shape, current_tetromino.x + 1, current_tetromino.y):
                    current_tetromino.x += 1
                elif event.key == pygame.K_DOWN and not check_collision(grid, current_tetromino.shape, current_tetromino.x, current_tetromino.y + 1):
                    current_tetromino.y += 1
                elif event.key == pygame.K_UP:
                    rotated = Tetromino()
                    rotated.shape = [list(row) for row in zip(*current_tetromino.shape[::-1])]
                    if not check_collision(grid, rotated.shape, current_tetromino.x, current_tetromino.y):
                        current_tetromino.shape = rotated.shape
        
        draw_grid(screen, grid)
        
        for row_idx, row in enumerate(current_tetromino.shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, current_tetromino.color, ((current_tetromino.x + col_idx) * BLOCK_SIZE, (current_tetromino.y + row_idx) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
