import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE, FPS
import colors
from maze_data import MAZE1, START_POSITION, END_POSITION


def draw_maze(
    screen,
    maze
):
    """
    Draw the maze, highlighting visited cells, step numbers,
    and optionally the final path. Also label start/end squares.
    """
    font = pygame.font.SysFont(None, 20)  # Font for step labels

    rows = len(maze)
    cols = len(maze[0])

    # 1) Draw the base maze
    for r in range(rows):
        for c in range(cols):
            rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if maze[r][c] == 1:
                color = colors.WALL_COLOR
            else:
                color = colors.UNEXPLORED_COLOR
            pygame.draw.rect(screen, color, rect)

    # 4) Label the start and end squares with "A" and "B"
    #    (on top of whatever color they currently have)
    start_r, start_c = START_POSITION
    start_rect = pygame.Rect(
        start_c * CELL_SIZE, start_r * CELL_SIZE, CELL_SIZE, CELL_SIZE
    )
    pygame.draw.rect(screen, colors.START_COLOR, start_rect)
    start_text = font.render("A", True, (255, 255, 255))  # white text
    start_text_rect = start_text.get_rect(center=start_rect.center)
    screen.blit(start_text, start_text_rect)

    end_r, end_c = END_POSITION
    end_rect = pygame.Rect(end_c * CELL_SIZE, end_r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, colors.END_COLOR, end_rect)
    end_text = font.render("B", True, (255, 255, 255))  # white text
    end_text_rect = end_text.get_rect(center=end_rect.center)
    screen.blit(end_text, end_text_rect)


def draw_grid(screen):
    rows = len(MAZE1)
    cols = len(MAZE1[0])
    for r in range(rows):
        pygame.draw.line(
            screen,
            colors.GRID_COLOR,
            (0, r * CELL_SIZE),
            (cols * CELL_SIZE, r * CELL_SIZE),
        )

    for c in range(cols):
        pygame.draw.line(
            screen,
            colors.GRID_COLOR,
            (c * CELL_SIZE, 0),
            (c * CELL_SIZE, rows * CELL_SIZE),
        )


def run_game(screen, clock):
    
    # Start at the defined starting position.
    player_pos = list(START_POSITION)

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False


        # Clear the screen.
        screen.fill((0, 0, 0))
        
        draw_maze(screen, MAZE1)
        draw_grid(screen)
        pygame.display.flip()


def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Maze Game")
    clock = pygame.time.Clock()

    run_game(screen, clock)
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
