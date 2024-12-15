import pygame

# button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

def menu_button_rect(screen_width,
                screen_height,
                button_width,
                button_height):
  margin = button_height
  total_height = button_height * 3 + margin * 2
  
  x = (screen_width - button_width) // 2
  start_y = (screen_height - total_height) // 2

  rect1 = pygame.Rect(x, start_y, button_width, button_height)
  rect2 = pygame.Rect(x, start_y + button_height + margin, button_width, button_height)
  rect3 = pygame.Rect(x, start_y + button_height * 2 + margin * 2, button_width, button_height)

  return {
    "Easy": {
      "level": "Easy",
      "rect": rect1},
    "Hard":{
      "level": "Hard",
      "rect": rect2},
    "Pro": {
      "level": "Pro",
      "rect": rect3}
  }

  
