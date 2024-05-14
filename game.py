import pygame.display
import os
from piece import Advisor
from Board import Board
background = pygame.image.load(os.path.join("img", "background.png"))
board_image = pygame.image.load("assets/image/Board.png")

rect = (216, 10, 650, 700)
def redraw_gamewindow():
    global window,bo
    window.blit(background, (0, 0))
    window.blit(board_image, (216, 0))
    bo.draw(window)
    pygame.display.update()


def click(pos):
    x = pos[0] // 71 - 3
    y = pos[1] // 71
    return x,y
def main():
    global bo
    bo = Board(9,10)
    clock = pygame.time.Clock()
    run = True
    while run:
        redraw_gamewindow()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                pygame.quit()

            if event.type == pygame.MOUSEMOTION:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                bo.update_moves(bo.board)
                i, j = click(pos)
                bo.select(i,j)

WIDTH, HEIGHT = 1080, 720
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chinese chess game')
main()