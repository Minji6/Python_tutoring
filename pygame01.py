import pygame # We will use the Pygame library.

pygame.init() #pygame initialize

background = pygame.display.set_mode((480, 360))
#I set the horizontal and vertical length of the game screen. 480 is horizontal and 360 is vertical.
pygame.display.set_caption("벽돌 게임")
# This will create a title for the game window.