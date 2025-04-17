import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")


    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_container = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroid_container, updateable, drawable)
    AsteroidField.containers = (updateable)
    AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2 )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        updateable.update(dt)
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()
        delta = clock.tick(60)
        dt = delta/1000



if __name__ == "__main__":
    main()