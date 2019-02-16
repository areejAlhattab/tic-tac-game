

import random


board = [' ' , ' ', ' ' , ' ', ' ' , ' ', ' ' , ' ' , ' ' , ' ']
def pBoard():
    pboard = print('   |' + '   |'  + '\n'
                   ' ' + board[1] + ' |' + ' ' + board[2] + ' |' + ' ' + board[3] + ' ' + '\n'
                   '   |' + '   |' + '\n'
                   '-----------' + '\n'
                   '   |' + '   |' + '\n'
                   ' ' + board[4] + ' |' + ' '+ board[5] +' |' +' ' + board[6] +' ' + '\n'
                   '   |' + '   |' + '\n'
                   '-----------' + '\n'
                   '   |' + '   |' + '\n'
                   ' ' + board[7] + ' |' + ' ' + board[8] + ' |' + ' ' + board[9] + ' ' + '\n'
                   '   |' + '   |')
    return pboard

NumbersList  = []
player = ''
computure = '' 
theEndNum = []

def isWinner():
    if (board[1] == board[2] == board[3]):
        winner = board[1]
        
        if winner == player :
            theEndNum.append(1)
            print('Congrats! You are the winner')
        if winner == computure :
            theEndNum.append(1)
            print('The computure is the winner ')
            
    if board[4] == board[5] == board[6]:
        winner = board[4]
        
        if winner == player :
            theEndNum.append(1)
            print('Congrats! You are the winner')
        if winner == computure :
            theEndNum.append(1)
            print('The computure is the winner ')
            
    if board[7] == board[8] == board[9]:
        winner =board[7]
        
        if winner == player :
            theEndNum.append(1)
            print('Congrats! You are the winner')
        if winner == computure :
            theEndNum.append(1)
            print('The computure is the winner ')

    if board[3] == board[5] == board[7]:
        winner = board[3]
        
        if winner == player :
            theEndNum.append(1)
            print('Congrats! You are the winner')
        if winner == computure :
            theEndNum.append(1)
            print('The computure is the winner ')

    if board[1] == board[5] == board[9]:
        winner = board[1]
        
        if winner == player :
            theEndNum.append(1)
            print('Congrats! You are the winner')
        if winner == computure :
            theEndNum.append(1)
            print('The computure is the winner ')
            
    if board[1] == board[4] == board[7]:
        winner = board[1]
        
        if winner == player :
            theEndNum.append(1)
            print('Congrats! You are the winner')
        if winner == computure :
            theEndNum.append(1)
            print('The computure is the winner ')
        
    if board[2] == board[5] == board[8]:
        winner = board[2]
        
        if winner == player :
            theEndNum.append(1)
            print('Congrats! You are the winner')
        if winner == computure :
            theEndNum.append(1)
            print('The computure is the winner ')
            
    if board[3] == board[6] == board[9]:
        winner = board[3]
        
        if winner == player :
            theEndNum.append(1)
            print('Congrats! You are the winner')
        if winner == computure :
            theEndNum.append(1)
            print('The computure is the winner ')
            

def theBegginer():
    random1 = random.randrange(0 , 2) 
    if random1 == 0:
        computureTurn()
    if random1 == 1 :
        playerTurn()

def YouTurn():
    turn = ''
    while not (turn == 'O' or turn == 'X'):
        turn = input('do you like to be O or X ? :   ').upper()
        
    if turn == 'X':
        return ['X', 'O']
    if turn == 'O':
        return ['O' , 'X']
    

def playerTurn():
    gameIsPlaying = True
    while gameIsPlaying:
        if len(theEndNum) == 1 :
            gameIsPlaying = False
            return gameIsPlaying
        if player == 'O':
            print_O_Player_Board()        
        if player == 'X':
            print_X_Player_Board()        
        if len(NumbersList) == 5 or len(NumbersList) ==6 or len(NumbersList) == 7 or len(NumbersList) == 8 or len(NumbersList) == 9:
            isWinner()    
        if len(theEndNum) == 1 :
            gameIsPlaying = False
            return gameIsPlaying
        if len(NumbersList) < 9 :    
            computureTurn() 

def computureTurn():
    gameIsPlaying = True
    while gameIsPlaying:
        if len(theEndNum) == 1 :
            gameIsPlaying = False
            return gameIsPlaying
        if computure == 'X':
            print_X_computure_Board()        
        if computure == 'O':
            print_O_computure_Board()        
        if len(NumbersList) == 5 or len(NumbersList) ==6 or len(NumbersList) == 7 or len(NumbersList) == 8 or len(NumbersList) == 9:
            isWinner()        
        if len(theEndNum) == 1 :
            gameIsPlaying = False
            return gameIsPlaying
        if len(NumbersList) < 9 :    
            playerTurn() 


     
def choose_number():
    cn = int(input("Enter a number from range (1 - 9 )  :  "))
    
    return cn

def computure_choose_number():
    ccn = random.randrange(1,10)
    return ccn


def print_X_Player_Board():
    new_input = choose_number()
    
    while new_input in NumbersList :
        new_input = choose_number()
        
    NumbersList.append(new_input)
    
    board[new_input] = 'X'
    new_board = pBoard()
    print('_________________ \n  ')
    return new_board


def print_O_Player_Board():
    new_input = choose_number()
    
    while new_input in NumbersList:
        new_input = choose_number()
        
    NumbersList.append(new_input)
    
    board[new_input] = 'O'
    new_board = pBoard()
    print('_________________ \n ')
    return new_board
    
def print_X_computure_Board():
    new_input = computure_choose_number()
    
    while new_input in NumbersList :
        new_input = computure_choose_number()
        
    NumbersList.append(new_input)
    
    board[new_input] = 'X'
    new_board = pBoard()
    return new_board

def print_O_computure_Board():
    new_input = computure_choose_number()
    
    while new_input in NumbersList:
        new_input = computure_choose_number()
        
    NumbersList.append(new_input)
    
    board[new_input] = 'O'
    new_board = pBoard()
    return new_board

print('welcom to tic tac toi game ! , have fun!')
pBoard()
player,computure = YouTurn()
theBegginer()
     