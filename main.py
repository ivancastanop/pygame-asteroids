import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
import sys


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids_group, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots_group, updatable, drawable)
    asteroids_field = AsteroidField()
    player_avatar = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for uptodate in updatable:
            uptodate.update(dt)

        for asteroid in asteroids_group:
            if asteroid.collision_check(player_avatar):
                print("Game over!")
                sys.exit()

            for bullet in shots_group:
                if asteroid.collision_check(bullet):
                    asteroid.split()
                    bullet.kill()

        pygame.Surface.fill(screen, (0, 0, 0))

        for drawing in drawable:
            drawing.draw(screen)

        pygame.display.flip()
        time_lapse = clock.tick(60)
        dt = time_lapse / 1000


if __name__ == "__main__":
    main()
