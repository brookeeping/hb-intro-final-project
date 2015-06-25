player = ('YC','RC')
num_moves_made = 0
placement = range(52)		
# Draw the grid
def draw_board(moves):
	print " %s | %s | %s | %s | %s | %s | %s " % (moves[10], moves[11], moves[12],moves[13],moves[14],moves[15],moves[16])
	print "----------------------------------"
	print " %s | %s | %s | %s | %s | %s | %s " % (moves[17], moves[18], moves[19],moves[20],moves[21],moves[22],moves[23])
	print "----------------------------------"
	print " %s | %s | %s | %s | %s | %s | %s " % (moves[24], moves[25], moves[26],moves[27],moves[28],moves[29],moves[30])
	print "----------------------------------"
	print " %s | %s | %s | %s | %s | %s | %s " % (moves[31], moves[32], moves[33],moves[34],moves[35],moves[36],moves[37])
	print "----------------------------------"
	print " %s | %s | %s | %s | %s | %s | %s " % (moves[38], moves[39], moves[40],moves[41],moves[42],moves[43],moves[44])
	print "----------------------------------"
	print " %s | %s | %s | %s | %s | %s | %s " % (moves[45], moves[46], moves[47],moves[48],moves[49],moves[50],moves[51])

draw_board(placement)
move = int(raw_input("Yellow Checker, where do you want to move? "))
placement[move] = "YC"
draw_board(placement)
move = int(raw_input("Red Checker, where do you want to move? "))
placement[move] = "RC"
draw_board(placement)
move = int(raw_input("Mellow yellow it's your turn! "))
placement[move] = "YC"
draw_board(placement)
move = int(raw_input("Your turn you royal redness! "))
placement[move] = "RC"
draw_board(placement)

while(True):
	move = int(raw_input("Player %s, where do you want to move? " % (player[num_moves_made%2])))
	placement[move] = player[num_moves_made%2]
	num_moves_made += 1
	draw_board(placement)
	if len(num_moves_made)
