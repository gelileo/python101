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
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)


def draw_particles(particles, screen):
    for particle in particles:
        particle.update()
        particle.draw(screen)
    particles = [p for p in particles if p.lifetime > 0]
    return particles


def celebration(x, y, particles):
    for _ in range(100):  # Number of particles
        color = random.choice(
            [(255, 255, 255), (255, 215, 0), (255, 69, 0)]
        )  # Particle colors
        particles.append(Particle(x, y, color))
