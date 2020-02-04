from piece import Pawn, Rook, Bishop, Knight, King, Queen
import pygame
from constant import SCREEN_WIDTH, SCREEN_HEIGHT, LIGHTBROWN, DARKBROWN


class Board:
    def __init__(self):
        self.pieces = []
        self.selected_idx = None
        self._player_name = None
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
        if self.selected_idx is not None:
            self.pieces[self.selected_idx].draw(surface)

    def mouse_clicked(self, mouse_x, mouse_y):
        x = int(mouse_x / (SCREEN_WIDTH / 8))
        y = int(mouse_y / (SCREEN_HEIGHT / 8))
        for idx, piece in enumerate(self.pieces):
            if (x, y) == piece.pos():
                self.selected_idx = idx

    def check_move(self, mouse_x, mouse_y):
        moved_piece = self.pieces[self.selected_idx]
        start_pos = moved_piece.pos()
        x = int(mouse_x / (SCREEN_WIDTH / 8))
        y = int(mouse_y / (SCREEN_HEIGHT / 8))
        invalid_move = False
        piece_to_remove = None
        if moved_piece.valid_move(x, y):
            path = self.get_move_path((x, y))
            for idx, piece in enumerate(self.pieces):
                if idx != self.selected_idx and piece.pos() in path[:-1] and type(moved_piece) != Knight:
                    invalid_move = True
                    break
                elif piece.pos() == (x, y):
                    if piece.colour != moved_piece.colour:
                        piece_to_remove = piece
                    else:
                        invalid_move = True
                        break

        else:
            invalid_move = True

        if invalid_move:
            self.selected_idx = None
            moved_piece.reset_draw()
            return None
        if piece_to_remove is not None:
            self.pieces.remove(piece_to_remove)
        idx = self.selected_idx
        self.commit(mouse_x, mouse_y)
        return type(moved_piece), idx, start_pos, (mouse_x, mouse_y)

    def piece_selected(self):
        return self.selected_idx is not None

    def selected_draw_pos(self):
        selected_piece = self.pieces[self.selected_idx]
        return selected_piece.draw_x, selected_piece.draw_y

    def move(self, x, y):
        if self.selected_idx is None:
            raise Exception
        self.pieces[self.selected_idx].move(x, y)

    def commit(self, x, y):
        if self.selected_idx is None:
            raise Exception
        self.pieces[self.selected_idx].commit(x, y)
        self.selected_idx = None

    def get_move_path(self, end):
        start = self.pieces[self.selected_idx].pos()
        path = []
        delta_x = end[0] - start[0]
        delta_y = end[1] - start[1]
        if delta_x != 0:
            x_step = int(delta_x / abs(delta_x))
            if delta_y != 0:
                y_step = int(delta_y / abs(delta_y))
                for i in range(abs(end[0] - start[0]) + 1):  # absolute change in x == absolute change in y
                    path.append((start[0] + (i * x_step), start[1] + (i * y_step)))
            else:
                for i in range(abs(end[0] - start[0]) + 1):
                    path.append((start[0] + (i * x_step), start[1]))
        elif delta_y != 0:
            y_step = int(delta_y / abs(delta_y))
            for i in range(abs(end[1] - start[1]) + 1):
                path.append((start[0], start[1] + (i * y_step)))
        return path

    def process_message(self, message):
        # Receives a message from the client and passes it to the relevant helper function
        name = message["name"]
        key = message["key"]
        payload = message["payload"]
        if key == "JOIN":
            self._process_join(name)
        elif key == "EXIT":
            self._process_exit(name)
        if payload and name != self._player_name and key == "MOVE":
            return self._process_move(payload)
        return None

    def _process_move(self, payload):
        self.selected_idx = payload["idx"]
        x, y = payload["end"]
        self.commit(x, y)

    def _process_join(self, name):
        if not self._player_name:
            self._player_name = name
            print("Joined the game as Player {}".format(name))
        elif name:
            print("Player {} has joined the game".format(name))

    def _process_exit(self, name):
        print("Player {} has left the game".format(name))
        pass
