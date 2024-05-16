import pygame.display
import os
import time
import pickle
from Board import Board
from client import Network
pygame.font.init()
background = pygame.image.load(os.path.join("img", "background.png"))
board_image = pygame.image.load(os.path.join("img", "Board.png"))

rect = (216, 10, 650, 700)
# turn = 'r'
def menu_screen(window, name):
    global bo, chessbg
    run = True
    offline = False

    while run:
        window.blit(background, (0, 0))
        small_font = pygame.font.SysFont("comicsans", 50)
        font = pygame.font.SysFont("comicsans", 80)
        txt1 = font.render("Chinese Chess", 1, (255, 255, 255))
        window.blit(txt1, (200, 200))
        txt2 = font.render("Click to join game", 1, (255, 255, 255))
        window.blit(txt2, (200, 400))
        if offline:
            off = small_font.render("Server Offline, Try Again Later...", 1, (255, 0, 0))
            window.blit(off, (WIDTH / 2 - off.get_width() / 2, 500))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                offline = False
                try:
                    bo = connect()
                    run = False
                    main()
                    # break
                except Exception as e:
                    print(e)
                    print("Server Offline")
                    offline = True


def redraw_gameWindow(window,bo,p1,p2,color,ready):
    window.blit(background, (0, 0))
    window.blit(board_image, (216, 0))

    bo.draw(window,color)
    formatTime1 = str(int(p1 // 60)) + ":" + str(int(p1 % 60))
    formatTime2 = str(int(p2 // 60)) + ":" + str(int(p2 % 60))
    if int(p1 % 60) < 10:
        formatTime1 = formatTime1[:-1] + "0" + formatTime1[-1]
    if int(p2 % 60) < 10:
        formatTime2 = formatTime2[:-1] + "0" + formatTime2[-1]

    font = pygame.font.SysFont("comicsans", 20)
    try:
        txt = font.render(bo.p1Name + "\'s Time: " + str(formatTime1), 1, (255, 255, 255))
        txt2 = font.render(bo.p2Name + "\'s Time: " + str(formatTime2), 1, (255, 255, 255))
    except Exception as e:
        print(e)
    window.blit(txt, (870, 550))
    window.blit(txt2, (870, 10))
    if color == "s":
        txt3 = font.render("SPECTATOR MODE", 1, (255, 0, 0))
        window.blit(txt3, (WIDTH / 2 - txt3.get_width() / 2, 10))

    if not ready:
        show = "Waiting for Player"
        if color == "s":
            show = "Waiting for Players"
        font = pygame.font.SysFont("comicsans", 80)
        txt = font.render(show, 1, (255, 0, 0))
        window.blit(txt, (WIDTH / 2 - txt.get_width() / 2, 300))

    if not color == "s":
        font = pygame.font.SysFont("comicsans", 25)
        if color == "r":
            txt3 = font.render("YOU ARE RED", 1, (255, 0, 0))
            window.blit(txt3, (10,10))
        else:
            txt3 = font.render("YOU ARE BLACK", 1, (255, 0, 0))
            window.blit(txt3, (10,10))

        if bo.turn == color:
            txt3 = font.render("YOUR TURN", 1, (255, 0, 0))
            window.blit(txt3, (10, 550))
        else:
            txt3 = font.render("OPPONENT TURN", 1, (255, 0, 0))
            window.blit(txt3, (10, 550))

    pygame.display.update()

def end_screen(window, text):
    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 70)
    txt = font.render(text, 1, (255, 0, 0))
    window.blit(txt,(300,300))
    pygame.display.update()
    pygame.time.set_timer(pygame.USEREVENT+1,3000)


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
    global turn, bo, name

    color = bo.start_user
    count = 0

    bo = n.send("update_moves")
    bo = n.send("name " + name)
    clock = pygame.time.Clock()
    run = True

    while run:
        if not color == "s":
            p1Time = bo.time1
            p2Time = bo.time2
            if count == 60:
                bo = n.send("get")
                count = 0
            else:
                count += 1
            clock.tick(30)

        try:
            redraw_gameWindow(window, bo, p1Time, p2Time, color, bo.ready)
        except Exception as e:
            print(e)
            end_screen(window, "Other player left")
            run = False
            break



        if not color == "s":
            if p2Time <= 0:
                bo = n.send("winner r")
            elif p1Time <= 0:
                bo = n.send("winner b")
        if bo.winner == "r":
            end_screen(window, "Red is the Winner!")
        elif bo.winner == "b":
            end_screen(window, "Black is the winner")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quit()
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and color != "s":
                    # quit game
                    if color == "r":
                        bo = n.send("winner b")
                    else:
                        bo = n.send("winner r")

            if event.type == pygame.MOUSEBUTTONDOWN:
                if color == bo.turn and bo.ready:
                    pos = pygame.mouse.get_pos()
                    bo = n.send("update moves")
                    i, j = click(pos)
                    bo = n.send("select " + str(i) + " " + str(j) + " " + color)
                    if color == 'r':
                        try:
                            bo = n.send("checkmate b")
                        except Exception as e:
                            print(e)
                    else:
                        try:
                            bo = n.send("checkmate r")
                        except Exception as e:
                            print(e)
    n.disconnect()
    bo = 0
    menu_screen(window)

name = input("Please type your name: ")
WIDTH, HEIGHT = 1080, 720
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chinese chess game')
menu_screen(window, name)