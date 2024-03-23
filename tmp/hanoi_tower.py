import pygame
import sys


num_disks = 4

# Layout Constants
# -----------------------------------
#           Status Label
#
#      Rod 1     Rod 2     Rod 3
#        |         |         |
#        |         |         |
#        |         |         |
#       ---       ---       ---
#          Start Over Button
# -----------------------------------
#
DISK_HEIGHT = 30
DISK_WIDTH_FACTOR = 50
ROD_WIDTH = 10
ROD_HEIGHT = DISK_HEIGHT * num_disks + 50
ROD_GAP = 250
FONT_SIZE = 20
PADDING = 20
SCREEN_WIDTH = 800
BASE_LINE_THICKNESS = 2
# SCREEN_HEIGHT = 600


# Colors
BACKGROUND_COLOR = (224, 224, 224)
WHITE = (255, 255, 255)
BLUE = (64, 128, 255, 160)
BLACK = (0, 0, 0)
SOURCE_COLOR = (0, 255, 191)
TARGET_COLOR = (255, 191, 0)
GRAY = (200, 200, 200, 128)
DARK_GRAY = (128, 128, 128)  # Darker color for hover effect
WARNING_COLOR = (255, 0, 0)

# Initialize Pygame
pygame.init()

# Initialize the font module
pygame.font.init()
disk_font = pygame.font.SysFont("Arial", FONT_SIZE)

status = ""
selected_source = -1
selected_target = -1


def clear_selections():
    global selected_source, selected_target
    selected_source = -1
    selected_target = -1


WARNING_DURATION = 3000  # 3 seconds
warning = None
warning_start = None


def create_warning(msg):
    global warning, warning_start
    warning = msg
    warning_start = pygame.time.get_ticks()


def should_show_warning():
    return warning is not None and pygame.time.get_ticks() - warning_start < WARNING_DURATION


def clear_warning():
    global warning, warning_start
    warning = None
    warning_start = None


# Button properties
button_width, button_height = 200, 40
button_font_size = 30
button_x = (SCREEN_WIDTH - button_width) // 2
button_color = GRAY
button_text_color = BLUE
button_font = pygame.font.SysFont(None, button_font_size)


def get_screen_height():
    status_height = PADDING * 2 + FONT_SIZE
    rod_names_height = PADDING * 2 + FONT_SIZE
    rod_height = ROD_HEIGHT + BASE_LINE_THICKNESS
    btn_height = button_height + PADDING * 2
    return status_height + rod_names_height + rod_height + btn_height


def get_button_y():
    return get_screen_height() - button_height - PADDING


def get_baseline_y():
    return get_screen_height() - button_height - PADDING * 2


# Button rectangle for hover detection
button_rect = pygame.Rect(
    button_x, get_baseline_y() + PADDING, button_width, button_height
)

move_button_width, move_button_height = 100, 40
move_button_rect = pygame.Rect(
    SCREEN_WIDTH - move_button_width - PADDING,
    get_baseline_y() + PADDING,
    move_button_width,
    button_height
)


def draw_rod(screen, x):
    pygame.draw.rect(
        screen, BLACK, (x, get_baseline_y() - ROD_HEIGHT,
                        ROD_WIDTH, ROD_HEIGHT)
    )


def draw_rods():
    for x in range(SCREEN_WIDTH // 4, SCREEN_WIDTH, SCREEN_WIDTH // 4):
        draw_rod(screen, x - ROD_WIDTH // 2)


def get_rod_name_rects():
    return [
        pygame.Rect(
            x - ROD_WIDTH * 1.5,
            get_baseline_y() - ROD_HEIGHT - PADDING // 2 - button_font_size,
            ROD_WIDTH * 3,
            button_font_size,
        )
        for x in range(SCREEN_WIDTH // 4, SCREEN_WIDTH, SCREEN_WIDTH // 4)
    ]


def draw_rod_names(mouse_pos):
    rod_names = ["A", "B", "C"]
    rod_name_rects = get_rod_name_rects()
    # print(rod_name_rects)

    for index, rect in enumerate(rod_name_rects):
        if index == selected_source:
            pygame.draw.rect(screen, SOURCE_COLOR, rect)
            pygame.draw.rect(screen, BLACK, rect, width=1)
        elif index == selected_target:
            pygame.draw.rect(screen, TARGET_COLOR, rect)
            pygame.draw.rect(screen, BLACK, rect, width=1)
        else:
            if rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, button_color, rect)

    for rod_name, rod_name_rect in zip(rod_names, rod_name_rects):
        text_surface = button_font.render(rod_name, True, (128, 128, 128))

        screen.blit(
            text_surface,
            (
                rod_name_rect.x + (rod_name_rect.width -
                                   text_surface.get_width()) // 2,
                rod_name_rect.y + 5,
            ),
        )


def rod_rects():
    return [
        pygame.Rect(
            x - ROD_WIDTH // 2, get_baseline_y() - ROD_HEIGHT, ROD_WIDTH, ROD_HEIGHT
        )
        for x in range(SCREEN_WIDTH // 4, SCREEN_WIDTH, SCREEN_WIDTH // 4)
    ]


def draw_baseline():
    pygame.draw.line(
        screen,
        BLACK,
        (0, get_baseline_y()),
        (SCREEN_WIDTH, get_baseline_y()),
        BASE_LINE_THICKNESS,
    )


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


def draw_reset_button(mouse_pos):
    # Check if mouse is over the button
    if button_rect.collidepoint(mouse_pos):
        button_color = DARK_GRAY  # Mouse is hovering over the button
        button_text_color = WHITE
    else:
        button_color = GRAY  # Mouse is not hovering over the button
        button_text_color = BLUE

    pygame.draw.rect(screen, button_color, button_rect, border_radius=10)
    button_text = button_font.render("Start Over", True, button_text_color)
    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)


def draw_move_button(mouse_pos):
    # Hide if source or target is not selected
    if selected_source == -1 or selected_target == -1:
        return

    # Check if mouse is over the button
    if move_button_rect.collidepoint(mouse_pos):
        button_color = DARK_GRAY  # Mouse is hovering over the button
        button_text_color = WHITE
    else:
        button_color = GRAY  # Mouse is not hovering over the button
        button_text_color = BLUE

    pygame.draw.rect(screen, button_color, move_button_rect, border_radius=10)
    button_text = button_font.render("Move", True, button_text_color)
    text_rect = button_text.get_rect(center=move_button_rect.center)
    screen.blit(button_text, text_rect)


def redraw(mouse_pos=[0, 0]):
    screen.fill(BACKGROUND_COLOR)
    draw_rods()
    draw_rod_names(mouse_pos)
    draw_baseline()
    draw_reset_button(mouse_pos)
    draw_move_button(mouse_pos)
    draw_status()
    draw_disks()  # Draw disks according to their current positions


def reset_game(mouse_pos):
    global steps, applied_steps, selected_source, selected_target
    steps = []
    applied_steps = []
    clear_selections()
    redraw(mouse_pos)


# Initialize game variables
steps = []
applied_steps = []


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
            y = get_baseline_y() - (DISK_HEIGHT * (disk_index + 1))
            disk_width = disk * DISK_WIDTH_FACTOR
            color = pygame.Color(0)
            hue = 50 + (180 / num_disks) * disk
            color.hsva = (hue, 100, 100, 100)
            draw_disk(screen, x, y, disk_width, color, disk)


def rod_name(index):
    if index < 0 or index > 2:
        return ""
    return ["A", "B", "C"][index]


def draw_status():
    color = DARK_GRAY
    msg = "Click on a rod name (A, B or C) to select source or target."
    if should_show_warning():
        msg = warning
        color = WARNING_COLOR
    else:
        if selected_source != -1 and selected_target != -1:
            msg = f"Souce: {rod_name(selected_source)}, Target: {rod_name(selected_target)}"
        elif selected_source != -1:
            msg = f"Selected source: {rod_name(selected_source)}, click on another rod to select target."
        elif selected_target != -1:
            msg = f"Selected target: {rod_name(selected_target)}, click on another rod to select source."

    text_surface = disk_font.render(msg, True, color)
    screen.blit(
        text_surface, ((SCREEN_WIDTH - text_surface.get_width()) // 2, PADDING))


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


def should_select_rod(rod_index):
    return selected_source == -1 or selected_target == -1 or selected_source == rod_index or selected_target == rod_index


def update_cursor(mouse_pos):
    if button_rect.collidepoint(mouse_pos):
        # Change cursor when hovering over the button
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        rod_name_rects = get_rod_name_rects()
        for index, rect in enumerate(rod_name_rects):
            if rect.collidepoint(mouse_pos):
                if should_select_rod(index):
                    # Change cursor when hovering over a rod name
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    return
        # Set to default cursor otherwise
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


def check_clicked_on_rod_names(mouse_pos):
    rod_name_rects = get_rod_name_rects()
    for index, rect in enumerate(rod_name_rects):
        if rect.collidepoint(mouse_pos):
            if should_select_rod(index):
                return index
    return -1


def on_click_rod_name(index):
    if index < 0 or index > 2:
        return

    global selected_source, selected_target
    if selected_source == index:
        selected_source = -1
    elif selected_target == index:
        selected_target = -1
    elif selected_source == -1:
        selected_source = index
    elif selected_target == -1:
        selected_target = index
    else:
        return  # Do nothing if both source and target are already selected


def can_move(source, target):
    if source == -1 or target == -1:
        create_warning("Please select source and target towers.")
        return False
    if source == target:
        create_warning("Source and target cannot be the same.")
        return False
    if not towers[source]:
        create_warning(f"Source tower {rod_name(source)} is empty.")
        return False
    if towers[target] and towers[target][-1] < towers[source][-1]:
        create_warning(
            f"Cannot move larger disk {towers[source][-1]} to smaller disk {towers[target][-1]}."
        )
        return False
    return True


def on_click_move():
    global status, applied_steps
    source, target = selected_source, selected_target
    if not can_move(source, target):
        return

    status = f"Moved from {source} to {target}. Towers state before move: {towers}"
    disk = towers[source].pop()  # Remove disk from source tower
    towers[target].append(disk)  # Add disk to target tower
    applied_steps.append((source, target))
    clear_selections()


# Initialize game window
screen = pygame.display.set_mode((SCREEN_WIDTH, get_screen_height()))
pygame.display.set_caption("Tower of Hanoi")

# Define initial tower positions
tower_positions = [
    (SCREEN_WIDTH // 4 - ROD_WIDTH // 2, get_baseline_y() - ROD_HEIGHT),
    (2 * SCREEN_WIDTH // 4 - ROD_WIDTH // 2, get_baseline_y() - ROD_HEIGHT),
    (3 * SCREEN_WIDTH // 4 - ROD_WIDTH // 2, get_baseline_y() - ROD_HEIGHT),
]

# Initialize towers with disks
towers = [
    [i for i in range(num_disks, 0, -1)],
    [],
    [],
]  # Tower 0 has all disks at start


clock = pygame.time.Clock()
# Game loop
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()  # Get mouse position continuously
    # Check if the mouse is hovering over the button
    update_cursor(mouse_pos)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(mouse_pos):
                reset_game(mouse_pos)
            elif move_button_rect.collidepoint(mouse_pos):
                on_click_move()
            else:
                on_click_rod_name(check_clicked_on_rod_names(mouse_pos))
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         if len(applied_steps) > 0:
        #             revert()
        #     elif event.key == pygame.K_RIGHT:
        #         next_move()
    redraw(mouse_pos)

    # Update the display
    pygame.display.flip()
    clock.tick(10)

# Quit Pygame
pygame.quit()
sys.exit()
