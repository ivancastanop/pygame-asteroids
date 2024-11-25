import pygame
from constants import *
from player import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    player_avatar = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0))
        player_avatar.draw(screen)
        pygame.display.flip()
        time_lapse = clock.tick(60)
        dt = time_lapse / 1000


if __name__ == "__main__":
    main()
