import pygame.display
import os
import time
from Board import Board
from client import Network
pygame.font.init()
background = pygame.image.load(os.path.join("img", "background.png"))
board_image = pygame.image.load("assets/image/Board.png")

rect = (216, 10, 650, 700)
# turn = 'r'
def menu_screen(window):
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
def redraw_gamewindow(window,bo,p1,p2):
    window.blit(background, (0, 0))
    window.blit(board_image, (216, 0))
    bo.draw(window)
    formatTime1 = str(int(p1 // 60)) + ":" + str(int(p1 % 60))
    formatTime2 = str(int(p2 // 60)) + ":" + str(int(p2 % 60))

    font = pygame.font.SysFont("Arial", 20)
    txt1 = font.render("Player 1 Time: " + str(formatTime1), 1, (255, 255, 255))
    txt2 = font.render("Player 2 Time: " + str(formatTime2), 1, (255, 255, 255))
    window.blit(txt2, (900,20))
    window.blit(txt1, (900,400))

    pygame.display.update()

def end_screen(window, text):
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 40)
    txt = font.render(text, 1, (255, 255, 255))
    window.blit(txt, (WIDTH / 2 - txt.get_width() / 2, 300))
    pygame.display.update()

    pygame.time.set_timer(pygame.USEREVENT+1,5000)


    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                run = False
            elif event.type == pygame.KEYDOWN:
                run = False
            elif event.type == pygame.USEREVENT+1:
                run = False



def click(pos):
    if pos != None:
        x = pos[0] // 71 - 3
        y = pos[1] // 71
        return x,y
    else:
        return -1,-1
def connect():
    global n,bo
    n = Network()
    return n.board
def main():
    p1Time = 60*10
    p2Time = 60*10
    # global turn
    turn = 'r'
    color = 'r'

    clock = pygame.time.Clock()
    start_time = time.time()
    run = True
    while run:
        if bo.turn != color:
            bo = n.send(str.encode("get"))
        try:
            b.board
            bo = b
        except:
            pass
        clock.tick(10)
        if turn == "r":
            p1Time -= (time.time()- start_time)
        else:
            p2Time -= (time.time()- start_time)

        start_time = time.time()
        redraw_gamewindow(window,bo, int(p1Time),int(p2Time))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if bo.turn == color:
                    pos = pygame.mouse.get_pos()
                    bo.update_moves()
                    i, j = click(pos)
                    change = bo.select(i,j,bo.turn)
                    if change:
                        if bo.turn == "r":
                            bo.turn = "b"
                            bo.reset_selected()
                        else:
                            bo.turn = "r"
                        bo.reset_selected()
                    bo.update_moves()
        # if bo.checkMate("r"):
        #     end_screen(window,"Red wins")
        # if bo.checkMate("b"):
        #     end_screen(window,"Black wins")

WIDTH, HEIGHT = 1080, 720
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chinese chess game')
bo = connect()
main()