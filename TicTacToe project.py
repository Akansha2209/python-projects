import random

def printboard(board):
   print('   |   |')
   print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
   print('   |   |')
   print('-----------')
   print('   |   |')
   print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
   print('   |   |')
   print('-----------')
   print('   |   |')
   print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
   print('   |   |')

def inputPlayermarker():
    marker = ''
    while not (marker == 'x' or marker == 'o'):
         print("You want to be x or o")
         marker = input()
         if marker == 'x':
               return ['x', 'o']
         else:
               return ['o', 'x']

def whoplay():
   s=int(input("enter your choices"))
   if s==1:
        return 'computer'
   elif s==2:
        return 'player'
   else:
        return 'player2'

def getMove(board, marker, move):
            board[move] = marker

def checkwin(board, le):
    return ((board[7] == le and board[8] == le and board[9] == le) or 
      (board[4] == le and board[5] == le and board[6] == le) or 
      (board[1] == le and board[2] == le and board[3] == le) or 
      (board[7] == le and board[4] == le and board[1] == le) or 
      (board[8] == le and board[5] == le and board[2] == le) or 
      (board[9] == le and board[6] == le and board[3] == le) or
      (board[7] == le and board[5] == le and board[3] == le) or
      (board[9] == le and board[5] == le and board[1] == le)) 

def copyBoard(board):
    copyofboard= []
    for i in board:
          copyofboard.append(i)
    return copyofboard

def isSpace(board, move):
    return board[move] == ' '

def PlayerMove(board):
         move = ' '
         while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpace(board, int(move)):
            print('What is your next move? (1-9)')
            move = input()
         return int(move)

def chooserandom(board, movesList):
     possibleMoves = []
     for i in movesList:
          if isSpace(board, i):
               possibleMoves.append(i)
          if len(possibleMoves) != 0:
             return random.choice(possibleMoves)
          else:
             return None

def player2(board, player2marker):
   if player2marker == 'x':
      playermarker = 'o'
   else:
      playermarker = 'x'
   for i in range(1, 10):
      copy = copyBoard(board)
      if isSpace(copy, i):
         getMove(copy, player2marker, i)

      if checkwin(copy, player2marker):
         return i
   for i in range(1, 10):
      copy = copyBoard(board)
      if isSpace(copy, i):
         getMove(copy, playermarker, i)
      if checkwin(copy, playermarker):
         return i
   move = chooserandom(board, [1, 3, 7, 9])
   if move != None:
      return move
   if isSpace(board, 5):
      return 5
   return chooserandom(board, [2, 4, 6, 8])

def computerMove(board, computerLetter):
   if computerLetter == 'x':
      playermarker = 'o'
   else:
      playermarker = 'x'
   for i in range(1, 10):
      copy = copyBoard(board)
      if isSpace(copy, i):
         getMove(copy, computerLetter, i)

      if checkwin(copy, computerLetter):
         return i
   for i in range(1, 10):
      copy = copyBoard(board)
      if isSpace(copy, i):
         getMove(copy, playermarker, i)
      if checkwin(copy, playermarker):
         return i
   move = chooserandom(board, [1, 3, 7, 9])
   if move != None:
      return move
   if isSpace(board, 5):
      return 5
   return chooserandom(board, [2, 4, 6, 8])


def isboFull(board):
    for i in range(1, 10):
         if isSpace(board, i):
            return False
    return True

      
print("*****************************************Welcome to Tic Tac Toe Game*******************************************")
    
def show():
   board = [' '] * 10
   playermarker, computerLetter = inputPlayermarker()
   turn = whoplay()
   game = True
   while game:
      if turn == 'player':
         printboard(board)
         move = PlayerMove(board)
         getMove(board, playermarker, move)
         
         if checkwin(board, playermarker):
            printboard(board)
            print('You have won the game!')
            game = False

         elif isboFull(board):
            printboard(board)
            print('The game is a tie!')
            break

         else:
            turn = 'computer'
      else:
         move = computerMove(board, computerLetter)
         getMove(board, computerLetter, move)
         if checkwin(board, computerLetter):
            printboard(board)
            print("The computer has won this game")
            game = False

         elif isboFull(board):
            printboard(board)
            print('The game is a tie!')
            break

         else:
                  turn = 'player'




def show2():
   theBoard = [' '] * 10
   playermarker, player2marker = inputPlayermarker()
   turn = whoplay()
   game = True
   while game:
      if turn == 'player':
         printboard(theBoard)
         move = PlayerMove(theBoard)
         getMove(theBoard, playermarker, move)
         
         if checkwin(theBoard, playermarker):
            printboard(theBoard)
            print('You have won the game!')
            game = False

         elif isboFull(theBoard):
            printboard(theBoard)
            print('The game is a tie!')
            break

         else:
            turn = 'player2'
      else:
         move = player2(theBoard, player2marker)
         getMove(theBoard, player2marker, move)
         if checkwin(theBoard, player2marker):
            printboard(theBoard)
            print("The second player has won this game")
            game = False

         elif isboFull(theBoard):
            printboard(theBoard)
            print('The game is a tie!')
            break

         else:
                  turn = 'player'


print("If you want to play as single player  press1 and If you want to play as multiplayer press2")
s=int(input("enter your choice"))
if s==1:
    show()
elif s==2:
    show2()

    
def playagain():
   print("If you want to continue press1 for yes and press2 for no")
   a=int(input("enter your choice"))
   if a==1:
      show()
   elif a==2:
        show2()
   elif a==3:
      print("Thanks for playing this game")
playagain()
