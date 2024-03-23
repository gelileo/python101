import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()
running = True

x = 40 
y = 40
radius = 20
step = radius


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill('blue')
    # pygame.draw.circle(screen, "red", (40,40), 20)

    pygame.draw.circle(screen, "red", (x,y), radius)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= step
    if keys[pygame.K_DOWN]:
        y += step
    if keys[pygame.K_LEFT]:
        x -= step
    if keys[pygame.K_RIGHT]:
        x += step
  
  # rect(surface, color, rect) -> Rect
    # pygame.draw.rect(screen, (200, 255, 127, 128), (200, 70, 100, 100), width = 0, border_radius=20)

  # Create a surface with transparency
  #   transparent_surface = pygame.Surface((100, 100), pygame.SRCALPHA)
    
  # pygame.draw.rect(transparent_surface, (200, 255, 127, 100), (0, 0, 100, 100), width=0, border_radius=20)

  # # Blit the transparent surface onto the main screen
  #   screen.blit(transparent_surface, (200, 70))

  # rect(surface, color, rect, width=0, border_radius=0, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1) -> Rect
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()