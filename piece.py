import pygame
import os
from constant import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK

class Piece:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.draw_x = x * SCREEN_WIDTH/8
        self.draw_y = y * SCREEN_HEIGHT/8
        self.pos = (x,y)
        if colour == 'white':
            self.colour = WHITE
        elif colour == 'black':
            self.colour = BLACK

    def load_piece(self, filename):
        piece = pygame.image.load(os.path.join("resources", "{}.png".format(filename)))
        return pygame.transform.scale(piece, (int(SCREEN_WIDTH/8),int(SCREEN_HEIGHT/8)))

    def is_clicked(self, mouse_pos):
        if (self.draw_x < mouse_pos[0] <= self.draw_x + SCREEN_WIDTH/8 
        and self.draw_y < mouse_pos[1] <= self.draw_y + SCREEN_HEIGHT/8):
            return True
        else:
            return False

    def valid_move(self):
        return False

    def move(self, new_x, new_y):
        self.x = int(new_x/(SCREEN_WIDTH/8))
        self.y = int(new_y/(SCREEN_HEIGHT/8))
        self.draw_x = self.x*SCREEN_HEIGHT/8
        self.draw_y = self.y*SCREEN_WIDTH/8

    def return_home(self):
        self.draw_x = self.x*SCREEN_HEIGHT/8
        self.draw_y = self.y*SCREEN_WIDTH/8

        
    def dragged(self, new_x, new_y):
        self.draw_x = new_x
        self.draw_y = new_y




class Pawn(Piece):
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour)
        if self.colour == BLACK:
            self.surface = self.load_piece("b_pawn")
        elif self.colour == WHITE:
            self.surface = self.load_piece("w_pawn")

    def valid_move(self, new_x, new_y, board = False):
        if(new_y - self.y == 1*self.colour and new_x - self.x == 0) and board.is_occupied(new_x,new_y) == False:
            # check_collision()
            return True
        elif(new_y - self.y == 2*self.colour and new_x - self.x == 0) and (self.y == 1 or self.y == 6) and board.is_occupied(new_x,new_y) == False:
            # check_collision()
            return True
        if(new_y - self.y == 1*self.colour 
            and abs(new_x - self.x) == 1 
            and board.is_occupied(new_x,new_y) != False
            and board.is_occupied(new_x,new_y) != self.colour):
            # check_collision()
            return True
        # print('fail')
        else:
            return False
    
    def type(self):
        return('pawn')


class Rook(Piece):
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour)
        if self.colour == BLACK:
            self.surface = self.load_piece("b_rook")
        elif self.colour == WHITE:
            self.surface = self.load_piece("w_rook")

    def valid_move(self, new_x, new_y, board = False):
        if(new_y - self.y != 0 and new_x - self.x == 0) or (new_y - self.y == 0 and new_x - self.x != 0):
            # check_collision()
            return True
        else:
            return False

    def type(self):
        return('rook')

class Knight(Piece):
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour)
        if self.colour == BLACK:
            self.surface = self.load_piece("b_knight")
        elif self.colour == WHITE:
            self.surface = self.load_piece("w_knight")


    def valid_move(self, new_x, new_y, board = False):
        if(abs(new_y - self.y) == 1 and abs(new_x - self.x) == 2) or (abs(new_y - self.y) == 2 and abs(new_x - self.x) == 1):
            return True
        else:
            return False

    def type(self):
        return('knight')


class Bishop(Piece):
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour)
        if self.colour == BLACK:
            self.surface = self.load_piece("b_bishop")
        elif self.colour == WHITE:
            self.surface = self.load_piece("w_bishop")

    def valid_move(self, new_x, new_y, board = False):
        if(abs(new_y - self.y) == abs(new_x - self.x) and abs(new_x - self.x) > 0):
            # check_collision()
            return True
        else:
            return False

    def type(self):
        return('bishop')


class Queen(Piece):
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour)
        if self.colour == BLACK:
            self.surface = self.load_piece("b_queen")
        elif self.colour == WHITE:
            self.surface = self.load_piece("w_queen")

    def valid_move(self, new_x, new_y, board = False):
        if(abs(new_y - self.y) == abs(new_x - self.x) and abs(new_x - self.x) > 0):
            # check_collision()
            return True
        elif (new_y - self.y != 0 and new_x - self.x == 0) or (new_y - self.y == 0 and new_x - self.x != 0):
            return True
        else:
            return False

    def type(self):
        return('queen')

class King(Piece):
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour)
        if self.colour == BLACK:
            self.surface = self.load_piece("b_king")
        elif self.colour == WHITE:
            self.surface = self.load_piece("w_king")

    def valid_move(self, new_x, new_y, board = False):
        if(abs(new_y - self.y) == 1 and abs(new_x - self.x) == 0) or (abs(new_y - self.y) == 0 and abs(new_x - self.x) == 1):
            return True

    def type(self):
        return('king')
