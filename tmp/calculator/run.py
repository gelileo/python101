import pygame
import sys

# Initialize pygame
pygame.init()

# Constants for layout and dimensions
WINDOW_WIDTH = 320
WINDOW_HEIGHT = 480
BUTTON_WIDTH = 70
BUTTON_HEIGHT = 70
BUTTON_MARGIN = 10
DISPLAY_HEIGHT = 100

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (230, 230, 230)

# Fonts
FONT_SIZE = 40
font = pygame.font.Font(None, FONT_SIZE)

# Calculator state
current_input = ""
result = ""

# Set up the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Calculator")

# Button positions and labels using expressions
buttons = [
    ('7', BUTTON_MARGIN, DISPLAY_HEIGHT + BUTTON_MARGIN), 
    ('8', 1 * (BUTTON_MARGIN + BUTTON_WIDTH), DISPLAY_HEIGHT + BUTTON_MARGIN),
    ('9', 2 * (BUTTON_MARGIN + BUTTON_WIDTH), DISPLAY_HEIGHT + BUTTON_MARGIN), 
    ('/', 3 * (BUTTON_MARGIN + BUTTON_WIDTH), DISPLAY_HEIGHT + BUTTON_MARGIN),

    ('4', BUTTON_MARGIN, DISPLAY_HEIGHT + 1 * (BUTTON_MARGIN + BUTTON_HEIGHT)), 
    ('5', 1 * (BUTTON_MARGIN + BUTTON_WIDTH), DISPLAY_HEIGHT + 1 * (BUTTON_MARGIN + BUTTON_HEIGHT)),
    ('6', 2 * (BUTTON_MARGIN + BUTTON_WIDTH), DISPLAY_HEIGHT + 1 * (BUTTON_MARGIN + BUTTON_HEIGHT)), 
    ('*', 3 * (BUTTON_MARGIN + BUTTON_WIDTH), DISPLAY_HEIGHT + 1 * (BUTTON_MARGIN + BUTTON_HEIGHT)),

    ('1', BUTTON_MARGIN, DISPLAY_HEIGHT + 2 * (BUTTON_MARGIN + BUTTON_HEIGHT)), 
    ('2', 1 * (BUTTON_MARGIN + BUTTON_WIDTH), DISPLAY_HEIGHT + 2 * (BUTTON_MARGIN + BUTTON_HEIGHT)),
    ('3', 2 * (BUTTON_MARGIN + BUTTON_WIDTH), DISPLAY_HEIGHT + 2 * (BUTTON_MARGIN + BUTTON_HEIGHT)), 
    ('-', 3 * (BUTTON_MARGIN + BUTTON_WIDTH), DISPLAY_HEIGHT + 2 * (BUTTON_MARGIN + BUTTON_HEIGHT)),

    ('C', BUTTON_MARGIN, DISPLAY_HEIGHT + 3 * (BUTTON_MARGIN + BUTTON_HEIGHT)), 
    ('0', 1 * (BUTTON_MARGIN + BUTTON_WIDTH), DISPLAY_HEIGHT + 3 * (BUTTON_MARGIN + BUTTON_HEIGHT)),
    ('=', 2 * (BUTTON_MARGIN + BUTTON_WIDTH), DISPLAY_HEIGHT + 3 * (BUTTON_MARGIN + BUTTON_HEIGHT)), 
    ('+', 3 * (BUTTON_MARGIN + BUTTON_WIDTH), DISPLAY_HEIGHT + 3 * (BUTTON_MARGIN + BUTTON_HEIGHT)),
]

def draw_text(text, pos, color=BLACK):
    """Function to draw text on the screen."""
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, pos)

def draw_buttons():
    """Draw buttons on the screen."""
    for (text, x, y) in buttons:
        pygame.draw.rect(screen, LIGHT_GRAY, (x, y, BUTTON_WIDTH, BUTTON_HEIGHT), border_radius=5)
        draw_text(text, (x + BUTTON_WIDTH // 3, y + BUTTON_HEIGHT // 4))

def check_button_click(pos):
    """Check if a button was clicked based on mouse position."""
    for (text, x, y) in buttons:
        if x < pos[0] < x + BUTTON_WIDTH and y < pos[1] < y + BUTTON_HEIGHT:
            return text
    return None

def calculate_expression(expression):
    """Function to evaluate the calculator expression."""
    try:
        return str(eval(expression))
    except Exception:
        return "Error"

# Main game loop
while True:
    screen.fill(WHITE)

    # Draw the input/result display area
    pygame.draw.rect(screen, GRAY, (BUTTON_MARGIN, BUTTON_MARGIN, WINDOW_WIDTH - 2 * BUTTON_MARGIN, DISPLAY_HEIGHT), border_radius=5)

    # Draw current input and result
    draw_text(current_input, (BUTTON_MARGIN + 10, BUTTON_MARGIN + 10), color=BLACK)
    draw_text(result, (BUTTON_MARGIN + 10, BUTTON_MARGIN + 50), color=GRAY)

    # Draw buttons
    draw_buttons()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            button_clicked = check_button_click(pos)

            if button_clicked:
                if button_clicked == 'C':  # Clear
                    current_input = ""
                    result = ""
                elif button_clicked == '=':  # Evaluate the expression
                    result = calculate_expression(current_input)
                else:  # Any other button
                    current_input += button_clicked

    # Update the display
    pygame.display.update()
