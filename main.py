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
offset_x = offset_y = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                board.mouse_clicked(mouse_x, mouse_y)
                if board.piece_selected():
                    selected_x, selected_y = board.selected_draw_pos()
                    offset_x = selected_x - mouse_x
                    offset_y = selected_y - mouse_y

        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            if board.piece_selected():
                board.move(mouse_x + offset_x, mouse_y + offset_y)

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = event.pos
            if event.button == 1 and board.piece_selected():
                board.check_move(mouse_x, mouse_y)

    board.draw_board(screen)
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()

