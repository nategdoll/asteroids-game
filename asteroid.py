from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20, 50)
        angle1 = self.velocity.angle_to(pygame.Vector2(0, 1)) + random_angle
        angle2 = self.velocity.angle_to(pygame.Vector2(0, 1)) - random_angle
        speed = self.velocity.length() * 1.2

        velocity1 = pygame.Vector2(0, 1).rotate(angle1) * speed
        velocity2 = pygame.Vector2(0, 1).rotate(angle2) * speed

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2

        return [asteroid1, asteroid2]