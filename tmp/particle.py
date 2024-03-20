import pygame
import random


class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.size = random.randint(2, 5)
        self.color = color
        self.lifetime = random.randint(50, 150)
        self.velocity_x = random.uniform(-3, 3)
        self.velocity_y = random.uniform(-3, 3)

    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.lifetime -= 1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color,
                           (int(self.x), int(self.y)), self.size)
