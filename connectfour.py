class ConnectFour(object):	
	def __init__(self):
		self.board = [[" "," "," "," "," "," "],
						[" "," "," "," "," "," "],
						[" "," "," "," "," "," "],
						[" "," "," "," "," "," "],
						[" "," "," "," "," "," "],
						[" "," "," "," "," "," "],
						[" "," "," "," "," "," "]]

	def draw_board(self):
		print "| %s | %s | %s | %s | %s | %s | %s |" % (self.board[0][0], self.board[1][0], self.board[2][0], self.board[3][0], self.board[4][0], self.board[5][0], self.board[6][0])
		print "| %s | %s | %s | %s | %s | %s | %s |" % (self.board[0][1], self.board[1][1], self.board[2][1], self.board[3][1], self.board[4][1], self.board[5][1], self.board[6][1])
		print "| %s | %s | %s | %s | %s | %s | %s |" % (self.board[0][2], self.board[1][2], self.board[2][2], self.board[3][2], self.board[4][2], self.board[5][2], self.board[6][2])
		print "| %s | %s | %s | %s | %s | %s | %s |" % (self.board[0][3], self.board[1][3], self.board[2][3], self.board[3][3], self.board[4][3], self.board[5][3], self.board[6][3])
		print "| %s | %s | %s | %s | %s | %s | %s |" % (self.board[0][4], self.board[1][4], self.board[2][4], self.board[3][4], self.board[4][4], self.board[5][4], self.board[6][4])
		print "| %s | %s | %s | %s | %s | %s | %s |" % (self.board[0][5], self.board[1][5], self.board[2][5], self.board[3][5], self.board[4][5], self.board[5][5], self.board[6][5])
		print "-----------------------------"
		print "  0 | 1 | 2 | 3 | 4 | 5 | 6  " 

	def add_piece(self, column,player):
		rowPos = 0
		while rowPos < 6:
			if self.board[column][rowPos] != " ":
				break
			rowPos+=1    	
		self.board[column][rowPos-1] = player

	def is_column_full(self, column):
		if self.board[column][0] != " ":
			return True
		return False
	# def has_winner(self, current_player):
	# 	haswinner = False
	# 	for row in self.board:
	# 		if row.count(current_player) == 4: #this doesnt count for 4 in a row, just counts 4 in the column 
	# 			haswinner = True 
	# 	return haswinner
	def isWinner(self, tile):
		BOARDWIDTH = 7  # how many spaces wide the board is
		BOARDHEIGHT = 6 # how many spaces tall the board is

		for x in range(BOARDWIDTH - 3): 
			for y in range(BOARDHEIGHT):
				if self.board[x][y] == tile and self.board[x+1][y] == tile and self.board[x+2][y] == tile and self.board[x+3][y] == tile:
					return True
		# check vertical spaces
		for x in range(BOARDWIDTH):
			for y in range(BOARDHEIGHT - 3):
				if self.board[x][y] == tile and self.board[x][y+1] == tile and self.board[x][y+2] == tile and self.board[x][y+3] == tile:
					return True
		# check / diagonal spaces
		for x in range(BOARDWIDTH - 3):
			for y in range(3, BOARDHEIGHT):
				if self.board[x][y] == tile and self.board[x+1][y-1] == tile and self.board[x+2][y-2] == tile and self.board[x+3][y-3] == tile:
					return True
		# check \ diagonal spaces
		for x in range(BOARDWIDTH - 3):
			for y in range(BOARDHEIGHT - 3):
				if self.board[x][y] == tile and self.board[x+1][y+1] == tile and self.board[x+2][y+2] == tile and self.board[x+3][y+3] == tile:
					return True
		return False

	# def game_over(self):

#write function to check if game is over, method of class connectfour
#get input from user, while loop (while true), switching players() 
def play_game():
	while True:
		global current_player
		my_board.draw_board()
		print "Player %s's turn! Enter the column you wish to drop your checker, 0 to 6." % (current_player)
		userInput = raw_input(">>> ")
		if userInput.isdigit():
			userInput = int(userInput)
			if not my_board.is_column_full(userInput):
				my_board.add_piece(userInput, current_player)
				break
			else:
				print "Column %i is full" % userInput
				

current_player = "A"
my_board = ConnectFour()
while True:
	play_game()
	if my_board.isWinner(current_player):
		my_board.draw_board()
		print "%s is the winner!!" % current_player
		# Ask if they want to resart if yes the
		input = raw_input("Do you want to play again? Y or N ")
		if input == "Y":
			current_player = "A"
			my_board = ConnectFour()
			continue
		else:
			break
	if current_player == "A":
		current_player = "B"
	else:
		current_player = "A"







