import pygame
from board import Board
from constant import SCREEN_WIDTH, SCREEN_HEIGHT

FPS = 30

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Chess")

clock = pygame.time.Clock()
board = Board()
turn = -1
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    board.draw_board(screen)
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()

