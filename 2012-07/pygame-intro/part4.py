import sys
import random
import pygame

from pygame.locals import QUIT, \
    KEYDOWN, KEYUP, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE

# Constants
WINDOWHEIGHT = 600
WINDOWWIDTH = 800
BACKGROUNDCOLOR = (15, 15, 15)
TEXTCOLOR = (255, 255, 255)

# Size of Baddie sprite
BADDIE_WIDTH = 40
BADDIE_HEIGHT = 40
# Pixel move rate per loop iteration
BADDIEMINSPEED = 1
BADDIEMAXSPEED = 8
# Number of loop iterations between adding new bombs
NEWBADDIERATE = 6

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
    # Part 4: Fonts
    font = pygame.font.SysFont(None, 48)

    # Part 1: Load images
    player_sprite = pygame.image.load('images/player.png')
    player_rect = player_sprite.get_rect()
    baddie_sprite = pygame.image.load('images/baddie.png')

    # Part 1: Set Player start position
    player_rect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)

    # Set up player movement
    move_left = move_right = move_up = move_down = False

    baddies = []
    baddie_add_counter = 0
    # Part 4: Start the score at 0
    score = 0

    # Start the game loop
    while True:
        # Part 4: Increase the score the longer the player lasts
        score += 1

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

        # Part 3: Managing addition of new enemies
        baddie_add_counter += 1
        if NEWBADDIERATE == baddie_add_counter:
            baddie_add_counter = 0
            new_baddie = {
                'rect': pygame.Rect(
                            random.randint(0, WINDOWWIDTH - BADDIE_WIDTH),
                            0 - BADDIE_HEIGHT,
                            BADDIE_WIDTH,
                            BADDIE_HEIGHT
                        ),
                'speed':random.randint(BADDIEMINSPEED, BADDIEMAXSPEED), 
                'surface': pygame.transform.scale(baddie_sprite, 
                    (BADDIE_WIDTH, BADDIE_HEIGHT))
            }

            baddies.append(new_baddie)

        # Part 2: Handle player movememnt
        if move_left and player_rect.left > 0:
            player_rect.move_ip(-1 * PLAYERSPEED, 0)
        if move_right and player_rect.right < WINDOWWIDTH:
            player_rect.move_ip(PLAYERSPEED, 0)
        if move_up and player_rect.top > 0:
            player_rect.move_ip(0, -1 * PLAYERSPEED)
        if move_down and player_rect.bottom < WINDOWHEIGHT:
            player_rect.move_ip(0, PLAYERSPEED)

        # Part 3: Move the baddies
        for baddie in baddies:
            baddie['rect'].move_ip(0, baddie['speed'])

        # Part 3: Remove any invisible baddies
        for baddie in baddies[:]:
            if baddie['rect'].top > WINDOWHEIGHT:
                baddies.remove(baddie)

        # Part 1: Render the scene
        windowSurface.fill(BACKGROUNDCOLOR)

        # Part 4: Show score
        score_text = font.render('Score: {0}'.format(score), 1, TEXTCOLOR)
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, 0)
        windowSurface.blit(score_text, score_rect)

        windowSurface.blit(player_sprite, player_rect)

        # Part 3: Add Baddies
        for baddie in baddies:
            windowSurface.blit(baddie['surface'], baddie['rect'])

        pygame.display.update()

        # Check for collisions
        got_hit = False
        for baddie in baddies:
            if player_rect.colliderect(baddie['rect']):
                got_hit = True
                break
        if got_hit:
            break

        mainClock.tick(FPS)

    # Part 4: End the game
    gameover_text = font.render('GAME OVER!', 1, TEXTCOLOR)
    gameover_rect = gameover_text.get_rect()
    gameover_rect.topleft = ((WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
    windowSurface.blit(gameover_text, gameover_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()

if __name__ == '__main__':
    main()
