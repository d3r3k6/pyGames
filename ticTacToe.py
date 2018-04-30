#Python program for tic tac toe develeoped for my kids
#Game is stored as dictonary values representing the hash shaped board
#The slots are represented as tL - for top left, mC for middle center, bR - for bottom right ect.
#The key-value pairs will consist of the square designator and either 'X', 'O', or ''

#The dictonary below contains the data structure for the board
theBoard = {'tL': ' ', 'tC': ' ', 'tR': ' ',
		 	'mL': ' ', 'mC': ' ', 'mR': ' ',
		 	'bL': ' ', 'bC': ' ', 'bR': ' '}

#Instruction for how the board is set up

print('The board is arrange in a 3 x 3 square')
print('Enter tL for the top-left square, tC for top center-square, and tR for top-right square')
print('The rest of the board follows suite: mL, mC, mR for the middle row and bL, bC, and bR for the bottom row')

#The function below will print the borard when called

def printBoard(board):
	print(board['tL'] + '|' + board['tC'] + '|' + board['tR'])
	print('-+-+-')
	print(board['mL'] + '|' + board['mC'] + '|' + board['mR'])
	print('-+-+-')
	print(board['bL'] + '|' + board['bC'] + '|' + board['bR'])



#The following code is for the user interface

turn = 'X'
for i in range(9):
	printBoard(theBoard)
	print('Turn for ' + turn + '. Move on which space?')
	move = input()
	theBoard[move] = turn
	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'
printBoard(theBoard)
