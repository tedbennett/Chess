from piece import Pawn, Rook, Bishop, Knight, King, Queen
import pygame
from constant import SCREEN_WIDTH, SCREEN_HEIGHT, LIGHTBROWN, DARKBROWN


class Board:
    def __init__(self):
        self.pieces = []
        self.selected_idx = None
        for i in range(8):
            self.pieces += [Pawn(i, 1, 'black')]
            self.pieces += [Pawn(i, 6, 'white')]
        self.pieces += [Rook(0, 0, 'black'),
                        Rook(7, 0, 'black'),
                        Knight(1, 0, 'black'),
                        Knight(6, 0, 'black'),
                        Bishop(2, 0, 'black'),
                        Bishop(5, 0, 'black'),
                        Queen(3, 0, 'black'),
                        King(4, 0, 'black'),
                        Rook(0, 7, 'white'),
                        Rook(7, 7, 'white'),
                        Knight(1, 7, 'white'),
                        Knight(6, 7, 'white'),
                        Bishop(2, 7, 'white'),
                        Bishop(5, 7, 'white'),
                        Queen(3, 7, 'white'),
                        King(4, 7, 'white'), ]

    def draw_board(self, screen):
        screen.fill(LIGHTBROWN)
        for i in range(0, 8, 1):
            for j in range(0, 8, 2):
                if i % 2:
                    pygame.draw.rect(screen, DARKBROWN,
                                     pygame.rect.Rect(SCREEN_WIDTH * (j + 1) / 8, (SCREEN_HEIGHT * i) / 8,
                                                      SCREEN_WIDTH / 8, SCREEN_HEIGHT / 8))
                else:
                    pygame.draw.rect(screen, DARKBROWN,
                                     pygame.rect.Rect((SCREEN_WIDTH * j) / 8, (SCREEN_HEIGHT * i) / 8,
                                                      SCREEN_WIDTH / 8,
                                                      SCREEN_HEIGHT / 8))
        self.draw_pieces(screen)

    def draw_pieces(self, surface):
        for idx, piece in enumerate(self.pieces):
            if idx != self.selected_idx:
                piece.draw(surface)
        if self.selected_idx:
            self.pieces[self.selected_idx].draw(surface)

    def mouse_clicked(self, mouse_x, mouse_y):
        x = int(mouse_x / (SCREEN_WIDTH / 8))
        y = int(mouse_y / (SCREEN_HEIGHT / 8))
        for idx, piece in enumerate(self.pieces):
            if (x, y) == piece.pos():
                self.selected_idx = idx

    def check_move(self, mouse_x, mouse_y):
        x = int(mouse_x / (SCREEN_WIDTH / 8))
        y = int(mouse_y / (SCREEN_HEIGHT / 8))
        invalid_move = False
        moved_piece = self.pieces[self.selected_idx]
        if moved_piece.valid_move(x, y):
            path = self.get_move_path((x, y))
            for idx, piece in enumerate(self.pieces):
                if idx != self.selected_idx and piece.pos() in path:
                    if piece.pos() == (x, y):
                        if piece.colour != moved_piece.colour:
                            self.pieces.remove(piece)
                        elif type(moved_piece) != Knight:
                            invalid_move = True
                            break
                    else:
                        invalid_move = True
                        break

        else:
            invalid_move = True

        if invalid_move:
            self.selected_idx = None
            moved_piece.reset_draw()
            return
        moved_piece.commit(mouse_x, mouse_y)
        self.selected_idx = None

    def piece_selected(self):
        return self.selected_idx is not None

    def selected_draw_pos(self):
        selected_piece = self.pieces[self.selected_idx]
        return selected_piece.draw_x, selected_piece.draw_y

    def move(self, x, y):
        if self.selected_idx is None:
            raise Exception
        self.pieces[self.selected_idx].move(x, y)

    def get_move_path(self, end):
        start = self.pieces[self.selected_idx].pos()
        path = []
        delta_x = end[0] - start[0]
        delta_y = end[1] - start[1]
        if delta_x != 0:
            x_step = int(delta_x / abs(delta_x))
            if delta_y != 0:
                y_step = int(delta_y / abs(delta_y))
                for i in range(abs(end[0] - start[0])):  # absolute change in x == absolute change in y
                    path.append((start[0] + (i * x_step), start[1] + (i * y_step)))
            else:
                for i in range(abs(end[0] - start[0])):
                    path.append((start[0] + (i * x_step), start[1]))
        elif delta_y != 0:
            y_step = int(delta_y / abs(delta_y))
            for i in range(abs(end[1] - start[1])):
                path.append((start[0], start[1] + (i * y_step)))
        return path
