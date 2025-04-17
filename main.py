import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2 )
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    player.containers(updateable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        updateable.update()
        for draw in drawable:
            draw.draw()
        pygame.display.flip()
        delta = clock.tick(60)
        dt = delta/1000



if __name__ == "__main__":
    main()