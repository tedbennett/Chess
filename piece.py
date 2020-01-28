import pygame
import os
from constant import SCREEN_WIDTH, SCREEN_HEIGHT


class Piece:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.draw_x = x * SCREEN_WIDTH / 8
        self.draw_y = y * SCREEN_HEIGHT / 8

        self.colour = colour
        self.selected = False
        self.type = None
        self.image = None

    def load_image(self):
        piece = pygame.image.load(os.path.join("media", "{}{}.png".format(self.colour, self.type)))
        self.image = pygame.transform.scale(piece, (int(SCREEN_WIDTH / 8), int(SCREEN_HEIGHT / 8)))

    def draw(self, surface):
        surface.blit(self.image, (self.draw_x, self.draw_y))

    def valid_move(self, new_x, new_y, piece):
        return False

    def move(self, x, y):
        self.draw_x = x
        self.draw_y = y

    def commit(self, x, y):
        self.x = int(x / (SCREEN_WIDTH / 8))
        self.y = int(y / (SCREEN_HEIGHT / 8))
        self.reset_draw()

    def reset_draw(self):
        self.draw_x = self.x * SCREEN_WIDTH / 8
        self.draw_y = self.y * SCREEN_HEIGHT / 8

    def pos(self):
        return self.x, self.y


class Pawn(Piece):
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour)
        self.type = "Pawn"
        self.load_image()

    def valid_move(self, new_x, new_y, board=False):
        if (new_y - self.y == 1 * self.colour and new_x - self.x == 0) and board.is_occupied(new_x, new_y) == False:
            # check_collision()
            return True
        elif (new_y - self.y == 2 * self.colour and new_x - self.x == 0) and (
                self.y == 1 or self.y == 6) and board.is_occupied(new_x, new_y) == False:
            # check_collision()
            return True
        if (new_y - self.y == 1 * self.colour
                and abs(new_x - self.x) == 1
                and board.is_occupied(new_x, new_y) != False
                and board.is_occupied(new_x, new_y) != self.colour):
            # check_collision()
            return True
        # print('fail')
        else:
            return False


class Rook(Piece):
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour)
        self.type = "Rook"
        self.load_image()

    def valid_move(self, new_x, new_y, board=False):
        if (new_y - self.y != 0 and new_x - self.x == 0) or (new_y - self.y == 0 and new_x - self.x != 0):
            # check_collision()
            return True
        else:
            return False


class Knight(Piece):
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour)
        self.type = "Knight"
        self.load_image()

    def valid_move(self, new_x, new_y, board=False):
        if (abs(new_y - self.y) == 1 and abs(new_x - self.x) == 2) or (
                abs(new_y - self.y) == 2 and abs(new_x - self.x) == 1):
            return True
        else:
            return False


class Bishop(Piece):
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour)
        super().__init__(x, y, colour)
        self.type = "Bishop"
        self.load_image()

    def valid_move(self, new_x, new_y, board=False):
        if (abs(new_y - self.y) == abs(new_x - self.x) and abs(new_x - self.x) > 0):
            # check_collision()
            return True
        else:
            return False


class Queen(Piece):
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour)
        super().__init__(x, y, colour)
        self.type = "Queen"
        self.load_image()

    def valid_move(self, new_x, new_y, board=False):
        if (abs(new_y - self.y) == abs(new_x - self.x) and abs(new_x - self.x) > 0):
            # check_collision()
            return True
        elif (new_y - self.y != 0 and new_x - self.x == 0) or (new_y - self.y == 0 and new_x - self.x != 0):
            return True
        else:
            return False


class King(Piece):
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour)
        super().__init__(x, y, colour)
        self.type = "King"
        self.load_image()

    def valid_move(self, new_x, new_y, board=False):
        if (abs(new_y - self.y) == 1 and abs(new_x - self.x) == 0) or (
                abs(new_y - self.y) == 0 and abs(new_x - self.x) == 1) or (
                abs(new_y - self.y) == 1 and abs(new_x - self.x) == 1):
            return True
        elif (abs(new_y - self.y) == 0 and abs(new_x - self.x) == 2):
            if self.colour == 'white' and self.y == 7 or self.colour == 'black' and self.y == 0:
                return True
