import pygame
import os
import board
from constant import SCREEN_WIDTH
from constant import SCREEN_HEIGHT

FPS = 30

# --- classses --- (CamelCase names)

# empty

# --- functions --- (lower_case names)
# empty

# --- main ---

# - init -

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#screen_rect = screen.get_rect()

pygame.display.set_caption("Chess")

# - objects -

rectangle = pygame.rect.Rect(176, 134, 17, 17)
piece_draging = False

# - mainloop -

clock = pygame.time.Clock()
board = board.Board()
turn = -1
running = True

while running:

    # - events -

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                for piece in board.pieces:           
                    if piece.is_clicked(event.pos):
                        selected_piece = piece
                        selected_piece.type()
                        piece_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = selected_piece.draw_x - mouse_x
                        offset_y = selected_piece.draw_y - mouse_y
                        if piece.colour != turn:
                            piece_draging = False


        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and piece_draging == True:
                new_x = int(event.pos[0]/(SCREEN_WIDTH/8))
                new_y = int(event.pos[1]/(SCREEN_HEIGHT/8))
                if selected_piece.valid_move(new_x, new_y, board):
                    if board.check_collision(new_x, new_y, selected_piece):
                        dest_piece = board.is_occupied(new_x, new_y)
                        if dest_piece != False:
                            if dest_piece.colour != selected_piece.colour:
                                board.delete(dest_piece)
                                selected_piece.move(event.pos[0], event.pos[1]) 
                            else:
                                selected_piece.return_home()
                    
                        else:
                            selected_piece.move(event.pos[0], event.pos[1])
                        turn *= -1
                    else:
                        selected_piece.return_home()
                else:
                    selected_piece.return_home()     
                piece_draging = False


        elif event.type == pygame.MOUSEMOTION:
            if piece_draging:
                mouse_x, mouse_y = event.pos
                selected_piece.dragged(mouse_x + offset_x, mouse_y + offset_y)

    board.draw_board(screen)
    pygame.display.flip()

    clock.tick(FPS)

# - end -

pygame.quit()