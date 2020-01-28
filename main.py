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
selected = None
offset_x = offset_y = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                selected = board.mouse_clicked(mouse_x, mouse_y)
                if selected:
                    offset_x = selected.draw_x - mouse_x
                    offset_y = selected.draw_y - mouse_y

        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            if selected:
                selected.move(mouse_x + offset_x, mouse_y + offset_y)

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = event.pos
            if event.button == 1 and selected:
                if board.check_move(selected, mouse_x, mouse_y):
                    selected = None

    board.draw_board(screen)
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()

