import pygame


def game_level_buttons(screen_width, screen_height, button_width, button_height):
    button_margin = button_height  # Space between buttons
    total_height = 3 * button_height + 2 * button_margin
    start_y = (screen_height - total_height) // 2

    return [
        {
            "label": "Easy",
            "rect": pygame.Rect(
                (screen_width - button_width) // 2, start_y, button_width, button_height
            ),
        },
        {
            "label": "Hard",
            "rect": pygame.Rect(
                (screen_width - button_width) // 2,
                start_y + button_height + button_margin,
                button_width,
                button_height,
            ),
        },
        {
            "label": "Pro",
            "rect": pygame.Rect(
                (screen_width - button_width) // 2,
                start_y + 2 * (button_height + button_margin),
                button_width,
                button_height,
            ),
        },
    ]


def clicked_level(mouse_pos, buttons):
    for button in buttons:
        if button["rect"].collidepoint(mouse_pos):
            return button["label"]
    return None
