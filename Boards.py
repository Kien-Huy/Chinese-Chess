import pygame
import time
import random
import Piece

WIDTH, HEIGHT = 1080, 720
FPS = 60
timer = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess game")
background = pygame.image.load("assets/image/background.png")
board = pygame.image.load("assets/image/Board.png")
# load in game pieces images
Black_King = pygame.image.load("assets/icon/King_Black.png")
Black_Advisor = pygame.image.load("assets/icon/Advisor_Black.png")
Black_Elephant = pygame.image.load("assets/icon/Elephant_Black.png")
Black_Horse = pygame.image.load("assets/icon/Horse_Black.png")
Black_Chariot = pygame.image.load("assets/icon/Chariot_Black.png")
Black_Canon = pygame.image.load("assets/icon/Canon_Black.png")
Black_Pawn = pygame.image.load("assets/icon/Pawn_Black.png")

Red_King = pygame.image.load("assets/icon/King_Red.png")
Red_Advisor = pygame.image.load("assets/icon/Advisor_Red.png")
Red_Elephant = pygame.image.load("assets/icon/Elephant_Red.png")
Red_Horse = pygame.image.load("assets/icon/Horse_Red.png")
Red_Chariot = pygame.image.load("assets/icon/Chariot_Red.png")
Red_Canon = pygame.image.load("assets/icon/Canon_Red.png")
Red_Pawn = pygame.image.load("assets/icon/Pawn_Red.png")
selected=pygame.image.load("assets/icon/Select.png")
captured=pygame.image.load("assets/icon/Capture.png")
black_pieces= [
    Piece.Piece("X",(3,0),Black_Chariot,selected,captured,screen),
    Piece.Piece("M",(4,0),Black_Horse,selected,captured,screen),
    Piece.Piece("Tg",(5,0),Black_Elephant,selected,captured,screen),
    Piece.Piece("S",(6,0),Black_Advisor,selected,captured,screen),
    Piece.Piece("T",(7,0),Black_King,selected,captured,screen),
    Piece.Piece("S",(8,0),Black_Advisor,selected,captured,screen),
    Piece.Piece("Tg",(9,0),Black_Elephant,selected,captured,screen),
    Piece.Piece("M",(10,0),Black_Horse,selected,captured,screen),
    Piece.Piece("X",(11,0),Black_Chariot,selected,captured,screen),
    Piece.Piece("P",(4,2),Black_Canon,selected,captured,screen),
    Piece.Piece("P",(10,2),Black_Canon,selected,captured,screen),
    Piece.Piece("B",(3,3),Black_Pawn,selected,captured,screen),
    Piece.Piece("B",(5,3),Black_Pawn,selected,captured,screen),
    Piece.Piece("B",(7,3),Black_Pawn,selected,captured,screen),
    Piece.Piece("B",(9,3),Black_Pawn,selected,captured,screen),
    Piece.Piece("B",(11,3),Black_Pawn,selected,captured,screen)
]


red_pieces= [
    Piece.Piece("X",(3,9),Red_Chariot,selected,captured,screen),
    Piece.Piece("M",(4,9),Red_Horse,selected,captured,screen),
    Piece.Piece("Tg",(5,9),Red_Elephant,selected,captured,screen),
    Piece.Piece("S",(6,9),Red_Advisor,selected,captured,screen),
    Piece.Piece("T",(7,9),Red_King,selected,captured,screen),
    Piece.Piece("S",(8,9),Red_Advisor,selected,captured,screen),
    Piece.Piece("Tg",(9,9),Red_Elephant,selected,captured,screen),
    Piece.Piece("M",(10,9),Red_Horse,selected,captured,screen),
    Piece.Piece("X",(11,9),Red_Chariot,selected,captured,screen),
    Piece.Piece("P",(4,7),Red_Canon,selected,captured,screen),
    Piece.Piece("P",(10,7),Red_Canon,selected,captured,screen),
    Piece.Piece("B",(3,6),Red_Pawn,selected,captured,screen),
    Piece.Piece("B",(5,6),Red_Pawn,selected,captured,screen),
    Piece.Piece("B",(7,6),Red_Pawn,selected,captured,screen),
    Piece.Piece("B",(9,6),Red_Pawn,selected,captured,screen),
    Piece.Piece("B",(11,6),Red_Pawn,selected,captured,screen)
]
Piece_List = ["T", "S", "Tg", "M", "X", "P", "B"]

def getLocationRed(red):
    location= []
    for piece in red:
        location.append(piece.location)
    return location

def getLocationBlack(black):
    location= []
    for piece in black:
        location.append(piece.location)
    return location

def showBackground():
    screen.blit(background, (0, 0))

def showBoard():
    screen.blit(board, (216, 0))

def showPieces():

    # Render Black Pieces
    for i in range(len(black_pieces)):
        black_pieces[i].drawPiece()
    # Render Red Pieces
    for i in range(len(red_pieces)):
        red_pieces[i].drawPiece()

def check_options(pieces,turn):
    moves_list = []
    all_moves_list = []
    for piece in pieces:
        location = piece.location
        piece_name = piece.name
        if piece_name == 'B':
            moves_list = check_B(location,turn)
        elif piece_name == 'P':
            moves_list = check_P(location,turn)
        elif piece_name == 'X': 
            moves_list = check_X(location,turn)
        elif piece_name == 'M':
            moves_list = check_M(location,turn)
        elif piece_name == 'Tg':
            moves_list = check_Tg(location,turn)
        elif piece_name == 'S':
            moves_list = check_S(location,turn)
        elif piece_name == 'T':
            moves_list = check_T(location,turn)
        all_moves_list.append(moves_list)
    return all_moves_list

def check_B(position,color):
    moves_list = []
    red_location=getLocationRed(red_pieces)
    black_location=getLocationRed(black_pieces)
    if color == 'red':
        if (position[0],position[1]-1) not in red_location and position[1] > 0:
            moves_list.append((position[0],position[1]-1))
        if  0 < position[1]-1 <= 4 and 11 > position[0] > 2 and ((position[0],position[1]-1)) not in red_location:
            moves_list.append((position[0],position[1]-1))
        if  0 < position[1] <= 4 and 11 > position[0]-1 > 2 and ((position[0]-1,position[1])) not in red_location:
            moves_list.append((position[0]-1,position[1]))
        if  0 < position[1] <= 4 and 12 > position[0]+1 > 3 and ((position[0]+1,position[1])) not in red_location:
            moves_list.append((position[0]+1,position[1]))
    else:
        if  (position[0],position[1]+1) not in black_location and position[1]+1 <= 9:
            moves_list.append((position[0],position[1]+1))
        if  5 < position[1]+1 < 9 and 11 > position[0] > 2 and ((position[0],position[1]+1)) not in black_location:
            moves_list.append((position[0],position[1]+1))
        if  4 < position[1] < 9 and 11 > position[0]-1 > 2 and ((position[0]-1,position[1])) not in black_location:
            moves_list.append((position[0]-1,position[1]))
        if  4 < position[1] < 9 and 12 > position[0]+1 > 3 and ((position[0]+1,position[1])) not in black_location:
            moves_list.append((position[0]+1,position[1]))
    return moves_list
def check_P(position,color):
    moves_list = []
    red_location=getLocationRed(red_pieces)
    black_location=getLocationRed(black_pieces)
    if color == 'red':
        enemies_list = black_location
        friends_list = red_location
        enemy = 'black'
    else:
        enemies_list = red_location
        friends_list = black_location
        enemy = 'red'
    for i in range(4):
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        elif i == 3:
            x = -1
            y = 0
        while(path):
            if (position[0] + (chain*x), position[1]+ (chain*y)) not in friends_list and \
            3 <=position[0] + (chain*x) <=11  and 0 <=position[1] + (chain*y) <=9 and \
                (position[0] + (chain*x), position[1]+ (chain*y)) not in enemies_list:
                moves_list.append((position[0] + (chain*x), position[1]+ (chain*y)))
                chain+=1
            elif ((position[0] + (chain*x), position[1]+ (chain*y)) in enemies_list or \
                    (position[0] + (chain*x), position[1]+ (chain*y)) in friends_list) and \
                        3 <=position[0] + (chain*x) <=11  and 0 <=position[1] + (chain*y) <=9 :
                place= chain+1
                flag = True
                while(flag):
                    if (position[0] + (place*x), position[1]+ (place*y)) in friends_list and \
                        3 <=position[0] + (place*x) <=11  and 0 <=position[1] + (place*y) <=9:
                        flag=False
                    elif (position[0] + (place*x), position[1]+ (place*y)) in enemies_list and \
                        3 <=position[0] + (place*x) <=11  and 0 <=position[1] + (place*y) <=9:
                        moves_list.append((position[0] + (place*x), position[1]+ (place*y)))
                        flag=False
                    elif (position[0] + (place*x), position[1]+ (place*y)) not in enemies_list and \
                        (position[0] + (place*x), position[1]+ (place*y)) not in friends_list and \
                        3 <=position[0] + (place*x) <=11  and 0 <=position[1] + (place*y) <=9:
                        place+=1
                    else: 
                        flag=False
                path=False
            else:
                path=False
    return moves_list
def check_X(position,color):
    red_location=getLocationRed(red_pieces)
    black_location=getLocationRed(black_pieces)
    moves_list = []
    if color == 'red':
        enemy = 'black'
        enemies_list = black_location
        friends_list = red_location
    else:
        enemy = 'red'
        enemies_list = red_location
        friends_list = black_location
    for i in range(4):
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        elif i == 3:
            x = -1
            y = 0
        while(path):
            if (position[0] + (chain*x), position[1]+ (chain*y)) not in friends_list and \
            3 <=position[0] + (chain*x) <=11  and 0 <=position[1] + (chain*y) <=9:
                moves_list.append((position[0] + (chain*x), position[1]+ (chain*y)))
                if (position[0] + (chain*x), position[1]+ (chain*y)) in enemies_list:
                    path=False
                chain+=1
            else:
                path=False
    return moves_list
def check_M(position,color):
    red_location=getLocationRed(red_pieces)
    black_location=getLocationRed(black_pieces)
    moves_list = []
    if color == 'red':
        enemies_list = black_location
        friends_list = red_location
    else:
        enemies_list = red_location
        friends_list = black_location
    targets = [(1,2),(1,-2),(2,1),(2,-1),(-1,2),(-1,-2),(-2,1),(-2,-1)]
    for i in range(8):
        flag = False
        pieces = [(0,1),(0,-1),(1,0),(1,0),(0,1),(0,-1),(-1,0),(-1,0)]
        for j in range(8):
            piece = (position[0]+pieces[i][0],position[1]+pieces[i][1])
            if piece in red_location or piece in black_location:
                flag= True
        if flag == False:
            target= (position[0]+targets[i][0],position[1]+targets[i][1])
            if target not in friends_list and 3 <= target[0] <= 11 and 0 <= target[1] <= 9:
                moves_list.append(target)
    return moves_list
def check_T(position,color):
    red_location=getLocationRed(red_pieces)
    black_location=getLocationRed(black_pieces)
    moves_list = []
    targets = [(1,0),(-1,0),(0,-1),(0,1)]
    if color == 'red':
        for i in range(4):
            target = (position[0]+targets[i][0],position[1]+targets[i][1])
            if target not in red_location and 6 <= target[0] <= 8 and 7 <= target[1] <= 9:
                moves_list.append(target)
    else:
        for i in range(4):
            target = (position[0]+targets[i][0],position[1]+targets[i][1])
            if target not in black_location and 6 <= target[0] <= 8 and 0 <= target[1] <= 2:
                moves_list.append(target)
    return moves_list
    pass
def check_S(position,color):
    red_location=getLocationRed(red_pieces)
    black_location=getLocationRed(black_pieces)
    moves_list = []
    targets = [(1,1),(-1,1),(-1,-1),(1,-1)]
    if color == 'red':
        for i in range(4):
            target = (position[0]+targets[i][0],position[1]+targets[i][1])
            if target not in red_location and 6 <= target[0] <= 8 and 7 <= target[1] <= 9:
                moves_list.append(target)
    else:
        for i in range(4):
            target = (position[0]+targets[i][0],position[1]+targets[i][1])
            if target not in black_location and 6 <= target[0] <= 8 and 0 <= target[1] <= 2:
                moves_list.append(target)
    return moves_list
def check_Tg(position,color):
    red_location=getLocationRed(red_pieces)
    black_location=getLocationRed(black_pieces)
    moves_list = []
    targets = [(2,2),(-2,2),(-2,-2),(2,-2)]
    if color == 'red':
        for i in range(4):
            flag = False
            pieces = [(1,1),(-1,1),(-1,-1),(1,-1)]
            piece = (position[0]+pieces[i][0],position[1]+pieces[i][1])
            if piece in red_location or piece in black_location:
                flag= True
            if flag == False:
                target= (position[0]+targets[i][0],position[1]+targets[i][1])
                if target not in red_location and 3 <= target[0] <= 11 and 9 >= target[1] >=4:
                    moves_list.append(target)
    else:
        for i in range(4):
            flag = False
            pieces = [(1,1),(-1,1),(-1,-1),(1,-1)]
            piece = (position[0]+pieces[i][0],position[1]+pieces[i][1])
            if piece in red_location or piece in black_location:
                flag= True
            if flag == False:
                target= (position[0]+targets[i][0],position[1]+targets[i][1])
                if target not in black_location and 3 <= target[0] <= 11 and 0 <= target[1] <= 4:
                    moves_list.append(target)
    return moves_list
def check_valid_moves():
    if turn_step < 2:
        options_list = red_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options
#hiện thi giao diện nước đi:
def draw_valid(moves,player):
    if player == 'red':
        enemies_list = black_pieces
    else:
        enemies_list = red_pieces
    for i in range(len(moves)):
        piece,index = getPieceFromList(moves[i],enemies_list)
        if piece == None:
            move=pygame.image.load("assets/icon/Move.png")
            screen.blit(move, [moves[i][0]*71 +15 ,moves[i][1]*71 + 13])
        else:
            enemies_list[index].status=2


def getPieceFromList(move,list):
    for piece in list:
        if move == piece.location:
            return piece, list.index(piece)
    return None, 0

def clickPieceFirst(click,color):
    if color == 'red':
        for piece in red_pieces:
            if click == piece.location:
                return piece
        return None
    if color == 'black':
        for piece in black_pieces:
            if click == piece.location:
                return piece
        return None
 
def IsInLocation(clickcroods,list):
    for piece in list:
        if clickcroods == piece.location:
            return True,list.index(piece)
    return False,0
#Hàm thực hiện nước đi
def PieceStep(name,lastlocation,location,player):
    global red_pieces
    global black_pieces
    if player == 'red':
        red_pieces[selection].location=location
        IsinBlack,black_piece=IsInLocation(location,black_pieces)
        if IsinBlack:
            captured_pieces_red.append(black_pieces[black_piece])
            black_pieces.pop(black_piece)
    else:
        black_pieces[selection].location=location
        IsinRed,red_piece=IsInLocation(location,red_pieces)
        if IsinRed:
            captured_pieces_black.append(red_pieces[red_piece])
            red_pieces.pop(red_piece)
    ##code hiển thị nút sau khi đi 
    lastmove=pygame.image.load("assets/icon/Move.png")
    screen.blit(lastmove, [lastlocation[0]*71 +15 ,lastlocation[1]*71 + 13])

def renderLastmove(lastlocation):
    lastmove=pygame.image.load("assets/icon/Move.png")
    screen.blit(lastmove, [lastlocation[0]*71 +15 ,lastlocation[1]*71 + 13])

def draw_check(turn):
    if turn == 'red':
        piece_tuong = [piece for piece in black_pieces if piece.name == "T"]
        if len(piece_tuong) > 0:
            for i in range(len(red_options)):
                if piece_tuong[0].location in red_options[i]:
                    return True, turn
    else:
        piece_tuong = [piece for piece in red_pieces if piece.name == "T"]
        if len(piece_tuong) > 0:
            for i in range(len(black_options)):
                if piece_tuong[0].location in black_options[i]:
                    return True, turn
    return False, turn


def draw_check_step(turn,red_list,black_list):
    if turn == 'red':
        red_option = check_options(red_list,'red')
        piece_tuong = [piece for piece in black_list if piece.name == "T"]
        for i in range(len(red_option)):
            if piece_tuong[0].location in red_option[i]:
                return True
    else:
        black_option = check_options(black_list,'black')
        piece_tuong = [piece for piece in red_list if piece.name == "T"]
        for i in range(len(black_option)):
            if piece_tuong[0].location in black_option[i]:
                return True
    return False
def CheckPieceStep(location,player,piece_list,enemy_list):
    lastlocation= piece_list[selection].location
    if player == 'red':
        piece_list[selection].location=location
        IsinBlack,black_piece=IsInLocation(location,enemy_list)
        if IsinBlack:
            captured_pieces_red.append(enemy_list[black_piece])
            enemy_list.pop(black_piece)
        return piece_list,lastlocation,selection,IsinBlack
    else:
        piece_list[selection].location=location
        IsinRed,red_piece=IsInLocation(location,enemy_list)
        if IsinRed:
            captured_pieces_black.append(enemy_list[red_piece])
            enemy_list.pop(red_piece)
        return piece_list,lastlocation,selection,IsinRed
#kiểm tra nước đi tiếp theo có bị chiếu hay không
def check_capture_T(turn,location):
    black_list = black_pieces.copy()
    red_list = red_pieces.copy()
    if turn == 'red':
        red_list,lastlocation,index,IsinBlack=CheckPieceStep(location,turn,red_list,black_list)
        flag = draw_check_step('black',red_list,black_list)
        red_list[index].location=lastlocation
        if IsinBlack:
            black_list.insert(selection,captured_pieces_red[len(captured_pieces_red)-1])
            captured_pieces_red.pop(len(captured_pieces_red)-1)
    else:        
        black_list,lastlocation,index,IsinRed=CheckPieceStep(location,turn,black_list,red_list)
        flag = draw_check_step('red',red_list,black_list)
        black_list[index].location=lastlocation
        if IsinRed:
            red_list.insert(selection,captured_pieces_black[len(captured_pieces_black)-1])
            captured_pieces_black.pop(len(captured_pieces_black)-1)
    return flag

def draw_capture_T(turn):
    check, color = draw_check(turn)
    if check == True:
        if color == "red":
            for piece in black_pieces:
                if piece.name == "T":
                    piece.status = 2
                    break
        else:
            for piece in red_pieces:
                if piece.name == "T":
                    piece.status = 2
                    break
        return True
    else:
        for piece in black_pieces:
            if piece.name == "T":
                piece.status = 0
                break
        for piece in red_pieces:
            if piece.name == "T":
                piece.status = 0
                break
        return False
#Hàm kiểm tra chiếu bí, trả về true khi bị chiếu bí
def checkmate(turn):
    count = 0
    if turn == 'red':
        for index,piece in enumerate(red_pieces):
            for move in red_options[index]:
                lastlocation = piece.location
                piece.location = move
                IsinBlack,black_piece=IsInLocation(move,black_pieces)
                if IsinBlack:
                    captured_pieces_red.append(black_pieces[black_piece])
                    black_pieces.pop(black_piece)
                if draw_check_step("black",red_pieces,black_pieces) == False:
                    if IsinBlack:
                        black_pieces.insert(index,captured_pieces_red[len(captured_pieces_red)-1])
                        captured_pieces_red.pop(len(captured_pieces_red)-1)
                    piece.location=lastlocation
                    return False
                piece.location=lastlocation
            count+=1
        if count == len(red_pieces):
            return True
    else:
        for index,piece in enumerate(black_pieces):
            for move in black_options[index]:
                lastlocation = piece.location
                piece.location = move
                IsinRed,red_piece=IsInLocation(move,red_pieces)
                if IsinRed:
                    captured_pieces_black.append(red_pieces[red_piece])
                    red_pieces.pop(red_piece)
                if draw_check_step("red",red_pieces,black_pieces) == False:
                    if IsinRed:
                        red_pieces.insert(index,captured_pieces_black[len(captured_pieces_black)-1])
                        captured_pieces_black.pop(len(captured_pieces_black)-1)
                    piece.location=lastlocation
                    return False
                piece.location=lastlocation
            count+=1
        if count == len(black_pieces):
            return True

def setStatusRedPiece():
    for piece in red_pieces:
        if piece.name != "T":
            piece.status = 0
def setStatusBlackPiece():
    for piece in black_pieces:
        if piece.name != "T":
            piece.status = 0

# def inputMovePiece():
#     global selection
#     print("lastlocation:")
#     lastlocation = input()
#     x_str, y_str = lastlocation.split(",")
#     lastlocation= ( int(x_str),int(y_str))
#     print("location:")
#     location = input()
#     x_str, y_str = location.split(",")
#     location = ( int(x_str), int(y_str))
#     print("Player:")
#     player = input()
#     if player == 'red':
#         Isin, index= IsInLocation(lastlocation,red_pieces)
#     else: 
#         Isin, index= IsInLocation(lastlocation,black_pieces)
#     if Isin:
#         selection = index
#         print(Isin)
#         PieceStep("",lastlocation,location,player)
#     print(selection)
Mouse_click=0
last_move = None
IsCapture_T_red = False
IsCapture_T_black = False
captured_pieces_red = []
captured_pieces_black = []
# 0 - white turn, 1 - black turn
turn_step = 0
selection = 100
valid_moves = []
isRunningGame = True
lastSelection = 100
red_options=check_options(red_pieces,"red")
black_options=check_options(black_pieces,"black")  
while(isRunningGame):
    showBackground()
    showBoard()
    showPieces()
    if selection != 100:
        if turn_step <= 1:
            valid_moves = check_valid_moves()
            draw_valid(valid_moves,'red')
        else:
            valid_moves = check_valid_moves()
            draw_valid(valid_moves,'black')
    elif selection == 100 and last_move != None:
        renderLastmove(last_move)
        setStatusRedPiece()
        setStatusBlackPiece()
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            isRunningGame = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # a=0
            # while a < 4:
            #     inputMovePiece()
            #     a+=1
            Mouse_click +=1
            x_coord = event.pos[0] // 71
            y_coord = event.pos[1] // 71
            click_coords= (x_coord, y_coord)
            if turn_step <= 1:
                IsinRed, index = IsInLocation(click_coords,red_pieces)
                if IsinRed:
                        #lấy vị trí quân cờ khi người dùng bấm
                    selection= index
                    red_pieces[selection].status=1
                    if turn_step == 0:
                        turn_step == 1
                #Kiểm tra khi click lần 2 vào quân cờ thì sẽ tắt hiển thị nước đi
                if IsinRed and lastSelection == selection:
                    red_pieces[selection].status = 0
                    selection = 100
                    setStatusBlackPiece()
                if IsinRed and lastSelection != 100:
                    red_pieces[lastSelection].status = 0
                    setStatusBlackPiece()
                    #Thực hiện nước đi
                    #Kiểm tra xem vị trí người dùng bấm có nằm trong vị trí quân cờ có thể đi hay không
                    #Kiểm tra thêm click lần đầu tiên có phải là quân cờ hay không
                if click_coords in valid_moves and selection != 100:
                    if check_capture_T('red',click_coords) == False:
                        lastmove = red_pieces[selection].location
                        last_move = lastmove
                        PieceStep("",lastmove,click_coords,"red")
                        red_options=check_options(red_pieces,"red")
                        black_options=check_options(black_pieces,"black")
                        IsCapture_T_red=draw_capture_T("red")
                        turn_step = 2
                        click_coords= None
                        Mouse_click = 0
                        selection = 100
                        valid_moves = []
                        Ischeckmate=checkmate('black')
                        if Ischeckmate:
                            print("Chiếu bí")
                    else:
                        turn_step = 1
                        click_coords= None
                        Mouse_click = 0
                        selection = 100
                        valid_moves = []
                lastSelection=selection
            if turn_step > 1:
                Isinblack, index = IsInLocation(click_coords,black_pieces)
                if Isinblack:
                    selection= index
                    black_pieces[selection].status=1
                    if turn_step == 2:
                        turn_step == 3
                if Isinblack and lastSelection == selection:
                    black_pieces[selection].status = 0
                    selection = 100
                    setStatusRedPiece()
                if Isinblack and lastSelection != 100:
                    black_pieces[lastSelection].status = 0
                    setStatusRedPiece()
                if click_coords in valid_moves and selection != 100:
                    if check_capture_T('black',click_coords) == False:
                        lastmove = black_pieces[selection].location
                        last_move = lastmove
                        PieceStep("",lastmove,click_coords,"black")
                        red_options=check_options(red_pieces,"red")
                        black_options=check_options(black_pieces,"black")
                        IsCapture_T_black=draw_capture_T("black")
                        turn_step = 0
                        click_coords= None
                        selection = 100
                        Mouse_click = 0
                        valid_moves = []
                        Ischeckmate=checkmate('red')
                        if Ischeckmate:
                            print("Chiếu bí")
                    else:
                        turn_step = 2
                        click_coords= None
                        selection = 100
                        Mouse_click = 0
                        valid_moves = []
                lastSelection=selection
    pygame.display.update()
pygame.quit()



# 