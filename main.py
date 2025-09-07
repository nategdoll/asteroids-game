# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    pygame.time.Clock().tick(60)
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    Shot.containers = (updatable, drawable)

    while pygame.get_init():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        # Call this last
        pygame.display.flip()
        dt = pygame.time.Clock().tick(60) / 1000
        for asteroid in asteroids:
            if player.check_for_collisions(asteroid):
                print("Game over!")
                return


if __name__ == "__main__":
    main()
