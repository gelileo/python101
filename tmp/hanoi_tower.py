import pygame
import sys

# Initialize Pygame
pygame.init()

pygame.font.init()  # Initialize the font module
disk_font = pygame.font.SysFont("Arial", 20)

num_disks = 4

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
    pygame.draw.line(screen, ROD_COLOR, (0, BASELINE_Y),
                     (SCREEN_WIDTH, BASELINE_Y), 2)


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
current_step = -1
steps = solve_hanoi(num_disks, 0, 2, 1)
print(steps)
# Initialize towers with disks
towers = [
    [i for i in range(num_disks, 0, -1)],
    [],
    [],
]  # Tower 0 has all disks at start


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
    if current_step < 0:
        msg = "Press the right arrow key to start the game."
    else:
        msg = f"Step {current_step}: {status}"
    text_surface = disk_font.render(msg, True, (128, 128, 128))
    screen.blit(text_surface, ((SCREEN_WIDTH -
                                text_surface.get_width()) // 2,
                               100))


def move_disk(step):
    global status
    source, target = step
    # Diagnostic print statement to observe the game state before attempting a move

    status = f"Moving from {source} to {target}. Towers state before move: {towers}"
    if towers[
        source
    ]:  # Check if the source tower is not empty before attempting to pop
        disk = towers[source].pop()  # Remove disk from source tower
        towers[target].append(disk)  # Add disk to target tower
    else:
        # Diagnostic message
        status = f"Attempted to move from empty tower {source}."


def draw_rods():
    for x in range(SCREEN_WIDTH // 4, SCREEN_WIDTH, SCREEN_WIDTH // 4):
        draw_rod(screen, x - ROD_WIDTH // 2)


clock = pygame.time.Clock()
# Game loop
running = True
while running:

    step_changed = False  # Flag to track if the current step has changed

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            previous_step = current_step  # Store the previous step
            if event.key == pygame.K_LEFT:
                current_step = max(0, current_step - 1)
            elif event.key == pygame.K_RIGHT:
                current_step = min(len(steps) - 1, current_step + 1)
            print(f"proposed step: {current_step}")
            step_changed = (
                current_step != previous_step
            )  # Check if the step has changed
            print(f"step changed: {step_changed}")
            print("")

    screen.fill(BACKGROUND_COLOR)
    draw_rods()
    draw_baseline()

    # Only move and draw disks if the step has changed
    if step_changed and steps:  # Check if the step has changed and there are steps
        source, target = steps[current_step]
        if not towers[
            source
        ]:  # If the source tower is empty, print an error message or handle it appropriately.
            status = f"Error: Attempted to move from empty tower {source}. Current state: {towers}"
        else:
            move_disk(
                steps[current_step]
            )  # Only call move_disk if the step has actually changed and is valid.

    draw_status()
    draw_disks()  # Draw disks according to their current positions

    # Update the display
    pygame.display.flip()
    clock.tick(10)

# Quit Pygame
pygame.quit()
sys.exit()
