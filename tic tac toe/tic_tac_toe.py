
import pygame as pygame,sys
from pygame.locals import *
import time

#initialization
piece = 'x'
winner = None
draw = False
width = 400
height = 400
white = (255, 255, 255)
line_color = (10,10,10)

#TicTacToe 3x3 board
game = [[None]*3,[None]*3,[None]*3]

#initializing pygame window
pygame.init()
delay = 30
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((width, height+100),0,32)
pygame.display.set_caption("Tic Tac Toe")

#loading the images
frontPage = pygame.image.load('tic tac opening.jpg')
x_img = pygame.image.load('x.jpg')
o_img = pygame.image.load('o.jpg')

#resizing images
x_img = pygame.transform.scale(x_img, (80,80))
o_img = pygame.transform.scale(o_img, (80,80))
frontPage = pygame.transform.scale(frontPage, (width, height+100))


def game_opening():
    screen.blit(frontPage,(0,0))
    pygame.display.update()
    time.sleep(1)
    screen.fill(white)
    
    # Drawing vertical lines
    pygame.draw.line(screen,line_color,(int(width/3),0),(int(width/3), height),7)
    pygame.draw.line(screen,line_color,(int(width/3*2),0),(int(width/3*2), height),7)
    # Drawing horizontal lines
    pygame.draw.line(screen,line_color,(0,int(height/3)),(width, int(height/3)),7)
    pygame.draw.line(screen,line_color,(0,int(height/3*2)),(width, int(height/3*2)),7)
    draw_status()
    

def draw_status():
    if winner is None:
        message = piece.upper() + "'s Turn"
    else:
        message = winner.upper() + " won!"
    if draw:
        message = 'Game Draw!'

    font = pygame.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))

    # copy the rendered message onto the board
    screen.fill ((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width/2, 500-50))
    screen.blit(text, text_rect)
    pygame.display.update()
    CLOCK.tick(delay)


def check_win():
    global game, winner,draw

    # check for winning by row
    for row in range (0,3):
        if ((game [row][0] == game[row][1] == game[row][2]) and(game [row][0] is not None)):
            # this row won
            winner = game[row][0]
            pygame.draw.line(screen, (250,0,0), (0, (row + 1)*height/3 -height/6),\
                              (width, (row + 1)*height/3 - height/6 ), 4)
            break

    # check for winning by columns
    for column in range (0, 3):
        if (game[0][column] == game[1][column] == game[2][column]) and (game[0][column] is not None):
            # this column won
            winner = game[0][column]
            #draw winning line
            pygame.draw.line (screen, (250,0,0),((column + 1)* width/3 - width/6, 0),((column + 1)* width/3 - width/6, height), 4)
            break

    # check for winning by diagonals
    if (game[0][0] == game[1][1] == game[2][2]) and (game[0][0] is not None):
        # left to right
        winner = game[0][0]
        pygame.draw.line (screen, (250,70,70), (50, 50), (350, 350), 4)
       

    if (game[0][2] == game[1][1] == game[2][0]) and (game[0][2] is not None):
        # right to left
        winner = game[0][2]
        pygame.draw.line (screen, (250,70,70), (350, 50), (50, 350), 4)
    
    #check for draw
    if(all([all(row) for row in game]) and winner is None ):
        draw = True
    draw_status()


def drawXO(row,column):
    global game,piece
    if row==1:
        posx = 30
    if row==2:
        posx = width/3 + 30
    if row==3:
        posx = width/3*2 + 30

    if column==1:
        posy = 30
    if column==2:
        posy = height/3 + 30
    if column==3:
        posy = height/3*2 + 30
    game[row-1][column-1] = piece
    if(piece == 'x'):
        screen.blit(x_img,(posy,posx))
        piece= 'o'
    else:
        screen.blit(o_img,(posy,posx))
        piece= 'x'
    pygame.display.update()

   
    

def userClick():
    #get coordinates of mouse click
    x,y = pygame.mouse.get_pos()

    #get column of click
    if(x<width/3):
        column = 1
    elif (x<width/3*2):
        column = 2
    elif(x<width):
        column = 3
    else:
        column = None
        
    #get row of click
    if(y<height/3):
        row = 1
    elif (y<height/3*2):
        row = 2
    elif(y<height):
        row = 3
    else:
        row = None
    

    if(row and column and game[row-1][column-1] is None):
        global piece
        
        #draw piece on screen
        drawXO(row,column)
        check_win()
        
        

def reset_game():
    global game, winner,piece, draw
    time.sleep(3)
    piece = 'x'
    draw = False
    game_opening()

    font = pygame.font.Font(None, 30)
    text = font.render("New Game: X's turn", 1, (255, 255, 255))

    # update message
    screen.fill ((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center=(width/2, 500-50))
    screen.blit(text, text_rect)
    winner=None
    game = [[None]*3,[None]*3,[None]*3]
    pygame.display.update()
    

game_opening()

# run the game loop forever
while(True):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type is MOUSEBUTTONDOWN:
            # user has clicked
            userClick()
            if(winner or draw):
                reset_game()

            
    pygame.display.update()
    CLOCK.tick(delay)

""" credit to https://www.youtube.com/watch?v=1I1CdUEOSPk for using as reference"""