import pygame
import os
# load in game pieces images
Black_Advisor = pygame.image.load(os.path.join("img", "Advisor_Black.png"))
Black_Horse = pygame.image.load(os.path.join("img", "Horse_Black.png"))
Black_King = pygame.image.load(os.path.join("img", "King_Black.png"))
Black_Elephant = pygame.image.load(os.path.join("img", "Elephant_Black.png"))
Black_Pawn = pygame.image.load(os.path.join("img", "Pawn_Black.png"))
Black_Chariot = pygame.image.load(os.path.join("img", "Chariot_Black.png"))
Black_Canon = pygame.image.load(os.path.join("img", "Canon_Black.png"))

Red_Advisor = pygame.image.load(os.path.join("img", "Advisor_Red.png"))
Red_Horse = pygame.image.load(os.path.join("img", "Horse_Red.png"))
Red_King = pygame.image.load(os.path.join("img", "King_Red.png"))
Red_Elephant = pygame.image.load(os.path.join("img", "Elephant_Red.png"))
Red_Pawn = pygame.image.load(os.path.join("img", "Pawn_Red.png"))
Red_Chariot = pygame.image.load(os.path.join("img", "Chariot_Red.png"))
Red_Canon = pygame.image.load(os.path.join("img", "Canon_Red.png"))
selected = pygame.image.load(os.path.join("img", "Select.png"))
moved = pygame.image.load(os.path.join("img", "Move.png"))
captured = pygame.image.load(os.path.join("img", "Capture.png"))

b = [Black_Advisor,Black_Horse,Black_King,Black_Elephant,Black_Pawn,Black_Chariot,Black_Canon]
r = [Red_Advisor,Red_Horse,Red_King,Red_Elephant,Red_Pawn,Red_Chariot,Red_Canon]
B = []
R = []
for img in b:
    B.append(img)

for img in r:
    R.append(img)

class piece:
    image = -1
    rect = (216, 10, 650, 700)
    startX=rect[0]
    startY=rect[1]
    def __init__(self,row,col,color):
        self.row = row
        self.col = col
        self.color = color
        self.selected = False
        self.move_list = []
        self.king = False

    def isSelected(self):
        return self.selected

    def update_valid_moves(self, board):
        self.move_list = self.valid_moves(board)

    def draw(self, win, board):
        if self.color == "r":
            drawThis= R[self.image]
        else:
            drawThis= B[self.image]

        if self.selected:
            moves = self.move_list
            for move in moves:
                x = self.startX + (move[0] * 71) + 7
                y = self.startY + (move[1] * 71)
                p = board[move[1]][move[0]]
                if p != 0:
                    if p.color != self.color:
                        win.blit(captured,[x-5,y-5])
                else:
                    win.blit(moved, [x+5,y+5])

        x = self.startX + (self.col * 71) + 7
        y = self.startY + (self.row * 71)
        if self.selected:
            win.blit(selected,[x-6,y-6])
        win.blit(drawThis,(x,y))

    def change_pos(self, pos):
        self.row = pos[0]
        self.col = pos[1]
class Advisor(piece):
    image = 0
    def valid_moves(self, board):
        i = self.row
        j = self.col
        move = []
        targets = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
        if self.color == "r":
            for k in range(4):
                if 7 <= i+targets[k][0] <= 9 and 3 <= j+targets[k][1] <= 5:
                    p = board[i+targets[k][0]][j+targets[k][1]]
                    if p == 0 or p.color != self.color:
                        move.append((j+targets[k][1],i+targets[k][0]))
        else:
            for k in range(4):
                if 0 <= i+targets[k][0] <= 2 and 3 <= j+targets[k][1] <= 5:
                    p = board[i+targets[k][0]][j+targets[k][1]]
                    if p == 0 or p.color != self.color:
                        move.append((j+targets[k][1],i+targets[k][0]))
        return move
class Horse(piece):
    image = 1

    def valid_moves(self, board):
        i = self.row
        j = self.col
        move = []
        targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
        for k in range(8):
            flag = False
            pieces = [(0, 1), (0, -1), (1, 0), (1, 0), (0, 1), (0, -1), (-1, 0), (-1, 0)]
            if 0 <= i + pieces[k][0] <= 9 and 0 <= j + pieces[k][1] <= 8:
                p = board[i + pieces[k][0]][j + pieces[k][1]]
                if p != 0:
                    flag = True
                if flag == False:
                    if 0 <= i + targets[k][0] <= 9 and 0 <= j + targets[k][1] <= 8:
                        p = board[i + targets[k][0]][j + targets[k][1]]
                        if p == 0 or p.color != self.color:
                            move.append((j + targets[k][1], i + targets[k][0]))
        return move
class King(piece):
    image = 2
    def __init__(self,row , col , color):
        super().__init__(row,col,color)
        self.king = True

    def valid_moves(self, board):
        i = self.row
        j = self.col
        move = []
        targets = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        if self.color == "r":
            for k in range(4):
                if 7 <= i+targets[k][0] <= 9 and 3 <= j+targets[k][1] <= 5:
                    p = board[i+targets[k][0]][j+targets[k][1]]
                    if p == 0 or p.color != self.color:
                        move.append((j+targets[k][1],i+targets[k][0]))
        else:
            for k in range(4):
                if 0 <= i+targets[k][0] <= 2 and 3 <= j+targets[k][1] <= 5:
                    p = board[i+targets[k][0]][j+targets[k][1]]
                    if p == 0 or p.color != self.color:
                        move.append((j+targets[k][1],i+targets[k][0]))
        return move
class Elephant(piece):
    image = 3

    def valid_moves(self, board):
        i = self.row
        j = self.col
        move = []
        targets = [(2, 2), (-2, 2), (-2, -2), (2, -2)]
        if self.color == "r":
                for k in range(4):
                    flag = False
                    pieces = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
                    if 5 <= i + pieces[k][0] <= 9 and 0 <= j + pieces[k][1] <= 8:
                        p = board[i + pieces[k][0]][j+pieces[k][1]]
                        if p != 0:
                            flag = True
                        if flag == False:
                            p = board[i + targets[k][0]][j+targets[k][1]]
                            if p == 0 or p.color != self.color:
                                move.append((j+targets[k][1], i + targets[k][0]))
        else:
                for k in range(4):
                    pieces = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
                    flag = False
                    if 0 <= i + pieces[k][0] <= 4 and 0 <= j + pieces[k][1] <= 8:
                        p = board[i + pieces[k][0]][j+pieces[k][1]]
                        if p != 0:
                            flag = True
                        if flag == False:
                            p = board[i + targets[k][0]][j+targets[k][1]]
                            if p == 0 or p.color != self.color:
                                move.append((j+targets[k][1], i + targets[k][0]))
        return move


class Pawn(piece):
    image = 4
    def __init__(self,row,col,color):
        super().__init__(row,col,color)

    def valid_moves(self,board):
        i = self.row
        j = self.col
        move = []
        if self.color == "r":
            if i > 4:
                p = board[i-1][j]
                if p == 0 or p.color == "b":
                    move.append((j,i-1))
            elif 0 < i <= 4:
                p = board[i-1][j]
                if p == 0 or p.color == "b":
                    move.append((j,i-1))
                if 0 < j < 8:
                    p = board[i][j-1]
                    if p == 0 or p.color == "b":
                        move.append((j-1,i))
                    p = board[i][j+1]
                    if p == 0 or p.color == "b":
                        move.append((j+1,i))
        else:
            if i < 5:
                p = board[i+1][j]
                if p == 0 or p.color == "r":
                    move.append((j, i + 1))
            elif 10 < i <= 5:
                p = board[i+1][j]
                if p == 0 or p.color == "r":
                    move.append((j, i + 1))
                if 0 < j < 8:
                    p = board[i][j-1]
                    if p == 0 or p.color == "r":
                        move.append((j - 1, i))
                    p = board[i][j+1]
                    if p == 0 or p.color == "r":
                        move.append((j + 1, i))
        return move




class Charoit(piece):
    image = 5

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        # UP
        for x in range(i - 1, -1, -1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break

        # DOWN
        for x in range(i + 1, 10, 1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color:
                moves.append((j, x))
                break
            else:
                break

        # LEFT
        for x in range(j - 1, -1, -1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.color != self.color:
                moves.append((x, i))
                break
            else:
                break

        # RIGHT
        for x in range(j + 1, 9, 1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.color != self.color:
                moves.append((x, i))
                break
            else:
                break

        return moves

class Canon(piece):
    image = 6

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        # UP
        for x in range(i - 1, -1, -1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color or p.color == self.color:
                for k in range(x - 1, -1, -1):
                    p = board[k][j]
                    if p != 0:
                        if p.color != self.color:
                            moves.append((j, k))
                            break
                break
            else:
                break

        # DOWN
        for x in range(i + 1, 10, 1):
            p = board[x][j]
            if p == 0:
                moves.append((j, x))
            elif p.color != self.color or p.color == self.color:
                for k in range(x + 1, 10, 1):
                    p = board[k][j]
                    if p != 0:
                        if p.color != self.color:
                            moves.append((j, k))
                            break
                break
            else:
                break

        # LEFT
        for x in range(j - 1, -1, -1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.color != self.color or p.color == self.color:
                for k in range(x - 1, -1, -1):
                    p = board[i][k]
                    if p != 0:
                        if p.color != self.color:
                            moves.append((k, i))
                            break
                break
            else:
                break

        # RIGHT
        for x in range(j + 1, 9, 1):
            p = board[i][x]
            if p == 0:
                moves.append((x, i))
            elif p.color != self.color or p.color == self.color:
                for k in range(x + 1, 9, 1):
                    p = board[i][k]
                    if p != 0:
                        if p.color != self.color:
                            moves.append((k, i))
                            break
                break
            else:
                break

        return moves