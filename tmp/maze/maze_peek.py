import pygame
import sys
from mazes import maze_data1
from colors import GRID_COLOR, BRICK_COLOR, BLACK, WHITE, BLUE, GRAY, LIGHT_GRAY
from layouts import *
from appearance import brick

# Pygame initialization
pygame.init()
pygame.font.init()

cell_pos_font = pygame.font.Font(None, 14)
brick_texture = brick()

POPUP_H = 50
POPUP_W = 100
TOOLBAR_H = 2 * POPUP_H
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT + TOOLBAR_H))
pygame.display.set_caption("Maze Peek")

button_rect = pygame.Rect(
    WINDOW_WIDTH - POPUP_W - 10,
    (TOOLBAR_H - POPUP_H) // 2,
    POPUP_W,
    POPUP_H,
)
popup_rect = pygame.Rect(100, 100, 300, 200)


def draw_pop(active):
    if active:
        pygame.draw.rect(screen, BLUE, button_rect)
    else:
        pygame.draw.rect(screen, LIGHT_GRAY, button_rect)

    font = pygame.font.SysFont(None, 36)
    text = font.render("Pop", True, WHITE)
    screen.blit(text, (button_rect.x + 20, button_rect.y + 5))


def draw_popup_menu():
    # Darken the background with a semi-transparent overlay
    overlay = pygame.Surface((500, 400))  # Create an overlay
    overlay.set_alpha(150)  # Set transparency level
    overlay.fill(GRAY)  # Fill overlay with gray color
    screen.blit(overlay, (0, 0))  # Draw the overlay

    # Draw the popup window
    pygame.draw.rect(screen, LIGHT_GRAY, popup_rect)

    # Add text inside the popup
    font = pygame.font.SysFont(None, 36)
    text = font.render("This is a popup!", True, BLACK)
    screen.blit(text, (popup_rect.x + 50, popup_rect.y + 50))

    # Close button
    close_button_rect = pygame.Rect(popup_rect.x + 100, popup_rect.y + 120, 100, 40)
    pygame.draw.rect(screen, BLUE, close_button_rect)

    close_text = font.render("Close", True, WHITE)
    screen.blit(close_text, (close_button_rect.x + 20, close_button_rect.y + 5))

    return close_button_rect


def draw_maze():
    # print(maze_data1)
    screen.fill(WHITE, rect=pygame.Rect(0, 0, WINDOW_WIDTH, TOOLBAR_H))
    screen.fill(BLACK, rect=pygame.Rect(0, TOOLBAR_H, WINDOW_WIDTH, WINDOW_HEIGHT))
    draw_grid()

    for y in range(MAZE_HEIGHT):
        for x in range(MAZE_WIDTH):
            if maze_data1[y][x] == 1:
                screen.blit(brick_texture, (x * CELL_SIZE, TOOLBAR_H + y * CELL_SIZE))


def draw_cell_pos(mouse_x, mouse_y):
    cell_x = mouse_x // CELL_SIZE
    cell_y = mouse_y // CELL_SIZE
    cell_pos_text = cell_pos_font.render(f"({cell_x}, {cell_y})", True, WHITE)
    screen.blit(cell_pos_text, (mouse_x + 10, mouse_y + 10))


def draw_grid():
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(
            screen, GRID_COLOR, (x, TOOLBAR_H), (x, WINDOW_HEIGHT + TOOLBAR_H)
        )
    for y in range(TOOLBAR_H, WINDOW_HEIGHT + TOOLBAR_H, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WINDOW_WIDTH, y))


while True:
    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    draw_maze()

    draw_cell_pos(x, y)

    draw_pop(False)

    # Update screen
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
