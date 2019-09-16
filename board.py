import piece
import pygame
from constant import SCREEN_WIDTH
from constant import SCREEN_HEIGHT
from constant import LIGHTBROWN
from constant import DARKBROWN

class Board:
    def __init__(self):
        self.pieces = []
        for i in range(8):
            self.pieces += [piece.Pawn(i, 1, 'black')]
        self.pieces += [piece.Rook(0, 0, 'black')] 
        self.pieces += [piece.Rook(7, 0, 'black')]
        self.pieces += [piece.Knight(1, 0, 'black')]
        self.pieces += [piece.Knight(6, 0, 'black')]
        self.pieces += [piece.Bishop(2, 0, 'black')]
        self.pieces += [piece.Bishop(5, 0, 'black')]
        self.pieces += [piece.Queen(3, 0, 'black')]
        self.pieces += [piece.King(4, 0, 'black')]
        for i in range(8):
            self.pieces += [piece.Pawn(i, 6, 'white')]
        self.pieces += [piece.Rook(0, 7, 'white') ]
        self.pieces += [piece.Rook(7, 7, 'white') ]
        self.pieces += [piece.Knight(1, 7, 'white')]
        self.pieces += [piece.Knight(6, 7, 'white')]
        self.pieces += [piece.Bishop(2, 7, 'white')]
        self.pieces += [piece.Bishop(5, 7, 'white')]
        self.pieces += [piece.Queen(4, 7, 'white')]
        self.pieces += [piece.King(3, 7, 'white')]

    def draw_board(self, screen):
        screen.fill(LIGHTBROWN)
        for i in range(0,8,1):
            for j in range(0,8,2): 
                if i%2:
                    pygame.draw.rect(screen, DARKBROWN, pygame.rect.Rect(SCREEN_WIDTH*(j+1)/8, (SCREEN_HEIGHT*i)/8, SCREEN_WIDTH/8, SCREEN_HEIGHT/8))
                else:
                    pygame.draw.rect(screen, DARKBROWN, pygame.rect.Rect((SCREEN_WIDTH*j)/8, (SCREEN_HEIGHT*i)/8, SCREEN_WIDTH/8, SCREEN_HEIGHT/8))
        for piece in self.pieces:
            screen.blit(piece.surface,(piece.draw_x,piece.draw_y)) 

    def is_occupied(self, x, y):
        for piece in self.pieces:
            if piece.x == x and piece.y == y:
                return piece
        return False

    def delete(self, piece):
        self.pieces.remove(piece)

    def check_collision(self,new_x, new_y, original_piece):
        if original_piece.type() == 'knight': return True
        old_x = original_piece.x
        old_y = original_piece.y
        x_diff = new_x - old_x
        y_diff = new_y - old_y
        if x_diff != 0:
            x_step = int(x_diff / abs(x_diff))
        if y_diff != 0:
            y_step = int(y_diff / abs(y_diff))

        path = []
        if abs(x_diff) == abs(y_diff):
            for inter_x, inter_y in zip(range(old_x, new_x,x_step), range(old_y, new_y,y_step)):
                if inter_x == old_x: continue
                path.append([inter_x, inter_y])
            for piece in self.pieces:
                if [piece.x, piece.y] in path:
                    return False
            return True

        elif (abs(x_diff) == 0 and abs(y_diff) > 0):
            for inter_y in range(old_y,new_y, y_step):
                if old_y == inter_y: continue
                path.append([old_x, inter_y])
            for piece in self.pieces:
                if [piece.x, piece.y] in path:
                    return False
            return True

        elif (abs(x_diff) > 0 and abs(y_diff) == 0):
            for inter_x in range(old_x,new_x, x_step):
                if old_x == inter_x: continue
                path.append([inter_x, old_y])
            for piece in self.pieces:
                if [piece.x, piece.y] in path:
                    return False
            return True
        return False
