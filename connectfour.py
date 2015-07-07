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

	# def game_over(self):

#write function to check if game is over, method of class connectfour
#get input from user, while loop (while true), switching players

my_board = ConnectFour()
my_board.draw_board()
my_board.add_piece(3, 1)
my_board.draw_board()
my_board.add_piece(3, 2)
my_board.draw_board()

player_a = "A"
player_b = "B"

def play_game():
	print "Player A, you go first! Enter the column you wish to drop your checker, 0 to 5."
	userInput = raw_input(">>> ")
	if userInput.isdigit():
		userInput = int(userInput)










