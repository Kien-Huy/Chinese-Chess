from piece import Advisor
from piece import Horse
from piece import King
from piece import Elephant
from piece import Pawn
from piece import Charoit
from piece import Canon
class Board():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.board = [[0 for x in range(rows)] for _ in range(cols)]

        self.board[0][0] = Charoit(0,0,'b')
        self.board[0][1] = Horse(0,1,'b')
        self.board[0][2] = Elephant(0,2,'b')
        self.board[0][3] = Advisor(0,3,'b')
        self.board[0][4] = King(0,4,'b')
        self.board[0][5] = Advisor(0,5,'b')
        self.board[0][6] = Elephant(0,6,'b')
        self.board[0][7] = Horse(0,7,'b')
        self.board[0][8] = Charoit(0,8,'b')

        self.board[2][1] = Canon(2,1,'b')
        self.board[2][7] = Canon(2,7,'b')

        self.board[3][0] = Pawn(3,0,'b')
        self.board[3][2] = Pawn(3,2,'b')
        self.board[3][4] = Pawn(3,4,'b')
        self.board[3][6] = Pawn(3,6,'b')
        self.board[3][8] = Pawn(3,8,'b')

        self.board[7][1] = Canon(7,1,'r')
        self.board[7][7] = Canon(7,7,'r')

        self.board[6][0] = Pawn(6,0,'r')
        self.board[6][2] = Pawn(6,2,'r')
        self.board[6][4] = Pawn(6,4,'r')
        self.board[6][6] = Pawn(6,6,'r')
        self.board[6][8] = Pawn(6,8,'r')

        self.board[9][0] = Charoit(9,0,'r')
        self.board[9][1] = Horse(9,1,'r')
        self.board[9][2] = Elephant(9,2,'r')
        self.board[9][3] = Advisor(9,3,'r')
        self.board[9][4] = King(9,4,'r')
        self.board[9][5] = Advisor(9,5,'r')
        self.board[9][6] = Elephant(9,6,'r')
        self.board[9][7] = Horse(9,7,'r')
        self.board[9][8] = Charoit(9,8,'r')

    def update_moves(self,board):
        for i in range(self.cols):
            for j in range(self.rows):
                if self.board[i][j] != 0 :
                    self.board[i][j].update_valid_moves(board)
    def draw(self,win):
        for i in range(self.cols):
            for j in range(self.rows):
                if self.board[i][j] != 0:
                    self.board[i][j].draw(win)

    def select(self,col,row):
        for i in range(self.cols):
            for j in range(self.rows):
                if self.board[i][j] != 0:
                    self.board[i][j].selected = False
        if self.board[row][col] != 0:
            self.board[row][col].selected = True

    def move(self, start, end):
        removed = self.board[end[1]][end[0]]
        self.board[end[1]][end[0]] = self.board[start[1]][start[0]]
        self.board[start[1]][start[0]] = 0
        return removed