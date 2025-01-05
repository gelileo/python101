import pygame

def game_level_buttons(screen_width, screen_height, button_width, button_height):
    """
    Creates button data for three game levels (Easy, Hard, Pro) centered vertically on the screen.
  
    Args:
        screen_width (int): The width of the screen.
        screen_height (int): The height of the screen.
        button_width (int): The width of each button.
        button_height (int): The height of each button.
  
    Returns:
        list[dict]: A list of dictionaries, each containing:
            - 'label' (str): The label for the button (e.g., "Easy").
            - 'rect' (pygame.Rect): A pygame rectangle defining the button's position and size.
    """
    button_margin = button_height  # Space between buttons
    total_height = 3 * button_height + 2 * button_margin
    start_y = (screen_height - total_height) // 2
    x = (screen_width - button_width) // 2
    return [
        {
            "label": "Easy",
            "rect": pygame.Rect(
                x, start_y, button_width, button_height
            ),
        },
        {
            "label": "Hard",
            "rect": pygame.Rect(
                x,
                start_y + button_height + button_margin,
                button_width,
                button_height,
            ),
        },
        {
            "label": "Pro",
            "rect": pygame.Rect(
                x,
                start_y + 2 * (button_height + button_margin),
                button_width,
                button_height,
            ),
        },
    ]


def clicked_level(mouse_pos, buttons):
    """
    Args:
        mouse_pos(tuple): x,y
        buttons: list of button data returned by game_level_buttons
    Returns:
        str: the selected level or None
    """
    # Put your implementation here
    for button in buttons:
        if button["rect"].collidepoint(mouse_pos):
            return button["label"]
    return None
