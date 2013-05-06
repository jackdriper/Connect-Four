import random

def getMove():
# Read input as move, check for validity. Return column number
  while True:
		print('Choose a column.')
		mv = raw_input()
		try:
			move = int(mv)
			if move not in range(8) or move == 0:
				print('Please enter valid column number2 (1-7).')
			elif board[5][move-1] != 0:
				print('That column is full.')
			else:
				return move - 1
		except ValueError:
			print('Please enter valid number1 (1-7).')

def movePiece(move, player):
# Puts the piece in the appropriate location on the board
	done = False
	for i in range(6):
		if board[i][move] ==0 and not done:
			board[i][move] = player
			done = True


def checkWin():
# Check board for wins. Return 0 for no winner. Return player for winner
	player = 1
	for k in range(2):
		# Check veritcal win
		for j in range(6):
			Count = 0
			for i in range(7):
				if board[j][i] == player:
					Count += 1
				else:
					Count = 0
				if Count >= 4:
					return player
		# Check horizontal win
		for i in range(7):
			Count = 0
			for j in range(6):
				if board[j][i] == player:
					Count += 1
				else:
					Count = 0
				if Count >= 4:
					return player
		
		# Check diagonal up
		for i in range(4):
			Count = 0
			for j in range(3):
				for k in range(4):
					if board[j+k][i+k] == player:
						Count += 1
				if Count >= 4:
					return player
		# Check diagonal down
		for i in range(4):
			Count = 0
			for j in range(3):
				for k in range(4):
					if board[5-j-k][i+k] == player:
						Count += 1
				if Count >= 4:
					return player
					
		# Check player 2
		player = 2
	
	return 0

def displayBoard():
	# Draws the board
	print('\n')
	for i in range(6):
		print('|' + '|'.join(map(str, board[5-i])) + '|')
		print('---------------')
	print(" 1 2 3 4 5 6 7 ")
	print('\n')

def newBoard():
# Initialize no pieces in each row
	for i in range(6):
		board[i] = [0,0,0,0,0,0,0]


def newGame():
# Play a new game
	newBoard()
	while True:
		print('Player 1''s turn:')
		movePiece(getMove(), 1)
		displayBoard()
		if checkWin():
			print('Player 1 wins!')
			break
	
		print('Player 2''s turn:')
		movePiece(getMove(), 2)
		displayBoard()
		if checkWin():
			print('Player 2 wins!')
			break
			
# Initialize board
board = [0,0,0,0,0,0]

while True:
	newGame()
	print('Would you like to play again? (y/n)')
	again = raw_input().lower().startswith('y')
	if not again:
		break
