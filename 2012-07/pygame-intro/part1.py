import sys
import pygame

from pygame.locals import QUIT

# Constants
WINDOWHEIGHT = 600
WINDOWWIDTH = 800
BACKGROUNDCOLOR = (15, 15, 15)

FPS = 40

def terminate():
    pygame.quit()
    sys.exit()

def main():
    # Part 1: Initialize pygame, the clock, and the display surface
    pygame.init()
    mainClock = pygame.time.Clock()
    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Dodge!')
    pygame.mouse.set_visible(False)

    # Part 1: Load images
    player_sprite = pygame.image.load('images/player.png')
    player_rect = player_sprite.get_rect()

    # Part 1: Set Player start position
    player_rect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)

    # Start the game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

        # Render the scene
        windowSurface.fill(BACKGROUNDCOLOR)
        windowSurface.blit(player_sprite, player_rect)

        pygame.display.update()

        mainClock.tick(FPS)

if __name__ == '__main__':
    main()
