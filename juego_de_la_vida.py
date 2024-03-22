import pygame
import numpy as np
import time

# Dimensiones de la cuadrícula
WIDTH, HEIGHT = 600, 600
# Tamaño de cada célula
CELL_SIZE = 10
# Número de células en la cuadrícula
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def create_grid():
    return np.zeros((ROWS, COLS))

def draw_grid(surface, grid):
    surface.fill(WHITE)
    for y in range(ROWS):
        for x in range(COLS):
            if grid[y, x] == 1:
                pygame.draw.rect(surface, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def update_grid(grid):
    new_grid = grid.copy()
    for y in range(ROWS):
        for x in range(COLS):
            neighbors = count_neighbors(grid, x, y)
            if grid[y, x] == 1:  # Célula viva
                if neighbors < 2 or neighbors > 3:
                    new_grid[y, x] = 0  # Muere por baja población o sobrepoblación
            else:  # Célula muerta
                if neighbors == 3:
                    new_grid[y, x] = 1  # Nace por reproducción
    return new_grid

def count_neighbors(grid, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if (0 <= x + i < COLS) and (0 <= y + j < ROWS):
                count += grid[y + j, x + i]
    return count

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("juego de la vida")
    clock = pygame.time.Clock()

    grid = create_grid()

    # Patrón inicial
    grid[5, 5] = 1
    grid[5, 6] = 1
    grid[5, 7] = 1
    
    grid[7, 7] = 1
    grid[7, 8] = 1
    grid[7, 9] = 1
    
    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_grid(screen, grid)
        grid = update_grid(grid)

        pygame.display.flip()
        clock.tick(10)  # Velocidad de actualización

    pygame.quit()

if __name__ == "__main__":
    main()
