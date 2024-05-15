from piece import Advisor
from piece import Horse
from piece import King
from piece import Elephant
from piece import Pawn
from piece import Charoit
from piece import Canon
import time
import pygame

class Board():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.ready = False

        self.last = None

        self.copy = True
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

        self.turn = "r"
        self.time1 = 600
        self.time2 = 600

        self.storedTime1 = 0
        self.storedTime2 = 0
        self.startTime = time.time()
        self.winner = None
    def update_moves(self):
        for i in range(self.cols):
            for j in range(self.rows):
                if self.board[i][j] != 0:
                    self.board[i][j].update_valid_moves(self.board)
    def draw(self,win):
        for i in range(self.cols):
            for j in range(self.rows):
                if self.board[i][j] != 0:
                    self.board[i][j].draw(win,self.board)
    def get_danger_moves(self,color):
        danger_moves = []
        for i in range(self.cols):
            for j in range(self.rows):
                if self.board[i][j] != 0:
                    if self.board[i][j].color != color:
                        danger_moves.append(self.board[i][j].move_list)
        return danger_moves

    def checkMate(self, color):
        danger_moves = self.get_danger_moves(color)
        king_moves = []
        for i in range(self.cols):
            for j in range(self.rows):
                if self.board[i][j] != 0:
                    if self.board[i][j].king and self.board[i][j].color == color:
                        king_moves.append(self.board[i][j].move_list)
        if len(king_moves) == 0:
            return False
        for move in king_moves:
            if move not in danger_moves:
                return False
        return True

    def is_checked(self, color):
        danger_moves = self.get_danger_moves(color)
        king_pos = (-1,-1)
        for i in range(self.cols):
            for j in range(self.rows):
                if self.board[i][j] != 0:
                    if self.board[i][j].color != color:
                        danger_moves.append(self.board[i][j].move_list)
                    else:
                        if self.board[i][j].king and self.board[i][j].color == color:
                            king_pos = (i,j)
        if king_pos not in danger_moves:
            return False
        else:
            return True



    def select(self,col,row,color):
        changed = False
        prev = (-1, -1)
        for i in range(self.cols):
            for j in range(self.rows):
                if self.board[i][j] != 0:
                    if self.board[i][j].selected:
                        prev = (i, j)
        if self.board[row][col] == 0:
            moves = self.board[prev[0]][prev[1]].move_list
            if (col,row) in moves:
                self.move(prev,(col,row))
                changed = True
            self.reset_selected()
        else:
            if self.board[prev[0]][prev[1]].color != self.board[row][col].color:
                moves = self.board[prev[0]][prev[1]].move_list
                if (col, row) in moves:
                    self.move(prev, (col, row))
                    changed = True
                self.reset_selected()
                if self.board[row][col].color == color:
                    self.board[row][col].selected = True
            else:
                self.reset_selected()
                if self.board[row][col].color == color:
                    self.board[row][col].selected = True
        return changed

    def reset_selected(self):
        for i in range(self.cols):
            for j in range(self.rows):
                if self.board[i][j] != 0:
                    self.board[i][j].selected = False

    def move(self, start, end):
        nBoard = self.board[:]
        nBoard[start[0]][start[1]].change_pos((end[1],end[0]))
        nBoard[end[1]][end[0]] = nBoard[start[0]][start[1]]
        nBoard[start[0]][start[1]] = 0
        self.board = nBoard
        self.reset_selected()