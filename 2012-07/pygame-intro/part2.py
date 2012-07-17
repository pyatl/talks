import sys
import pygame

from pygame.locals import QUIT, \
    KEYDOWN, KEYUP, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE

# Constants
WINDOWHEIGHT = 600
WINDOWWIDTH = 800
BACKGROUNDCOLOR = (15, 15, 15)

PLAYERSPEED = 5

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

    # Set up player movement
    move_left = move_right = move_up = move_down = False

    # Start the game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            # Part 2: Handle keyboard input and movement
            elif event.type == KEYDOWN:
                if event.key == K_LEFT or event.key == ord('a'):
                    move_right = False
                    move_left = True
                elif event.key == K_RIGHT or event.key == ord('d'):
                    move_left = False
                    move_right = True
                elif event.key == K_UP or event.key == ord('w'):
                    move_down = False
                    move_up = True
                elif event.key == K_DOWN or event.key == ord('s'):
                    move_up = False
                    move_down = True
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()
                elif event.key == K_LEFT or event.key == ord('a'):
                    move_left = False
                elif event.key == K_RIGHT or event.key == ord('d'):
                    move_right = False
                elif event.key == K_UP or event.key == ord('w'):
                    move_up = False
                elif event.key == K_DOWN or event.key == ord('s'):
                    move_down = False

        # Part 2: Handle player movememnt
        if move_left and player_rect.left > 0:
            player_rect.move_ip(-1 * PLAYERSPEED, 0)
        if move_right and player_rect.right < WINDOWWIDTH:
            player_rect.move_ip(PLAYERSPEED, 0)
        if move_up and player_rect.top > 0:
            player_rect.move_ip(0, -1 * PLAYERSPEED)
        if move_down and player_rect.bottom < WINDOWHEIGHT:
            player_rect.move_ip(0, PLAYERSPEED)

        # Part 1: Render the scene
        windowSurface.fill(BACKGROUNDCOLOR)
        windowSurface.blit(player_sprite, player_rect)

        pygame.display.update()

        mainClock.tick(FPS)

if __name__ == '__main__':
    main()
