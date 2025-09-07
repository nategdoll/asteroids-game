from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    def __init__(self, position, velocity):
        super().__init__(position.x, position.y, radius=5)
        self.velocity = velocity
        self.lifetime = 1.0  # seconds

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)