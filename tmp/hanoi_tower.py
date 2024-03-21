import pygame
import sys

# Initialize Pygame
pygame.init()

pygame.font.init()  # Initialize the font module
disk_font = pygame.font.SysFont("Arial", 20)

num_disks = 5

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 450
BACKGROUND_COLOR = (224, 224, 224)
ROD_COLOR = (0, 0, 0)
DISK_HEIGHT = 30
DISK_WIDTH_FACTOR = 50
ROD_WIDTH = 10
ROD_HEIGHT = DISK_HEIGHT * num_disks + 50
ROD_GAP = 250
BASELINE_Y = SCREEN_HEIGHT - 50

status = ""

# Function to draw a rod


def draw_rod(screen, x):
    pygame.draw.rect(
        screen, ROD_COLOR, (x, BASELINE_Y - ROD_HEIGHT, ROD_WIDTH, ROD_HEIGHT)
    )


def draw_baseline():
    pygame.draw.line(screen, ROD_COLOR, (0, BASELINE_Y), (SCREEN_WIDTH, BASELINE_Y), 2)


# Function to draw a disk
# def draw_disk(screen, x, y, width, color):
#     pygame.draw.rect(screen, color, (x - width // 2, y, width, DISK_HEIGHT))
def draw_disk(screen, x, y, width, color, number):
    # Convert pygame.Color to an RGBA tuple
    rgba_color = (
        color.r,
        color.g,
        color.b,
        200,
    )  # Set alpha to 128 for semi-transparency

    disk_surface = pygame.Surface(
        (width, DISK_HEIGHT), pygame.SRCALPHA
    )  # Create a Surface with alpha
    # Fill with the modified color including transparency
    disk_surface.fill(rgba_color)
    # Render the disk number text
    text_surface = disk_font.render(
        str(number), True, (255, 255, 255)
    )  # Black color for the text
    disk_surface.blit(
        text_surface,
        (
            (width - ROD_WIDTH) // 2,
            (DISK_HEIGHT - text_surface.get_height()) // 2,
        ),
    )  # horizontally, vertically centered

    screen.blit(disk_surface, (x - width // 2, y))


# Function to solve Tower of Hanoi recursively
def solve_hanoi(n, source, target, auxiliary):
    if n == 1:
        return [(source, target)]
    else:
        steps = solve_hanoi(n - 1, source, auxiliary, target)
        steps.append((source, target))
        steps.extend(solve_hanoi(n - 1, auxiliary, target, source))
        return steps


# Initialize game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tower of Hanoi")

# Define initial tower positions
tower_positions = [
    (SCREEN_WIDTH // 4 - ROD_WIDTH // 2, BASELINE_Y - ROD_HEIGHT),
    (2 * SCREEN_WIDTH // 4 - ROD_WIDTH // 2, BASELINE_Y - ROD_HEIGHT),
    (3 * SCREEN_WIDTH // 4 - ROD_WIDTH // 2, BASELINE_Y - ROD_HEIGHT),
]


# Initialize game variables
steps = solve_hanoi(num_disks, 0, 2, 1)
applied_steps = []

for i, step in enumerate(steps, start=1):
    print(step, end=", ")
    if i % 5 == 0:
        print()
print()
print("=" * 30)

# Initialize towers with disks
towers = [
    [i for i in range(num_disks, 0, -1)],
    [],
    [],
]  # Tower 0 has all disks at start


def get_current_step():
    ret = len(applied_steps)
    if ret >= len(steps):
        return -1
    return ret


def draw_disks():
    for tower_index, tower in enumerate(towers):
        for disk_index, disk in enumerate(tower):
            x = tower_positions[tower_index][0] + ROD_WIDTH // 2
            # Adjust y to start disks at the bottom of the rod
            y = BASELINE_Y - (DISK_HEIGHT * (disk_index + 1))
            disk_width = disk * DISK_WIDTH_FACTOR
            color = pygame.Color(0)
            hue = 50 + (180 / num_disks) * disk
            color.hsva = (hue, 100, 100, 100)
            draw_disk(screen, x, y, disk_width, color, disk)


def draw_status():
    current_step = get_current_step()
    if current_step == 0:
        msg = "Press the right arrow key to start the game."
    elif current_step == -1:
        msg = "Game over. No further moves."
    else:
        msg = f"Step {current_step}: {status}"
    text_surface = disk_font.render(msg, True, (128, 128, 128))
    screen.blit(text_surface, ((SCREEN_WIDTH - text_surface.get_width()) // 2, 100))


def next_move():
    global status
    current_step = get_current_step()
    if current_step == -1:
        return

    source, target = steps[get_current_step()]
    # Diagnostic print statement to observe the game state before attempting a move

    status = f"Moving from {source} to {target}. Towers state before move: {towers}"
    if towers[
        source
    ]:  # Check if the source tower is not empty before attempting to pop
        disk = towers[source].pop()  # Remove disk from source tower
        towers[target].append(disk)  # Add disk to target tower
        applied_steps.append((source, target))
    else:
        # Diagnostic message
        status = f"Attempted to move from empty tower {source}."


def revert():
    global status
    if applied_steps:
        current_step = get_current_step()
        source, target = applied_steps.pop()
        if towers[target]:
            disk = towers[target].pop()
            towers[source].append(disk)
            status = (
                f"Reverted step {current_step}. Towers state after revert: {towers}"
            )
        else:
            status = f"Error: Attempted to revert to empty tower {target}."
    else:
        status = "No steps to revert."


def draw_rods():
    for x in range(SCREEN_WIDTH // 4, SCREEN_WIDTH, SCREEN_WIDTH // 4):
        draw_rod(screen, x - ROD_WIDTH // 2)


clock = pygame.time.Clock()
# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if len(applied_steps) > 0:
                    revert()
            elif event.key == pygame.K_RIGHT:
                next_move()

    screen.fill(BACKGROUND_COLOR)
    draw_rods()
    draw_baseline()

    draw_status()
    draw_disks()  # Draw disks according to their current positions

    # Update the display
    pygame.display.flip()
    clock.tick(10)

# Quit Pygame
pygame.quit()
sys.exit()
