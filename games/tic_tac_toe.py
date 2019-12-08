# Tic-Tac-Toe Program using 
# random number in Python 

# importing all necessary libraries 
import numpy as np 
import random 
from time import sleep 

# Creates an empty board 
def create_board(): 
	return(np.array([[0, 0, 0], 
					[0, 0, 0], 
					[0, 0, 0]])) 

# Check for empty places on board 
def possibilities(board): 
	l = [] 
	
	for i in range(len(board)): 
		for j in range(len(board)): 
			
			if board[i][j] == 0: 
				l.append((i, j)) 
	return(l) 

# Select a random place for the player 
def random_place(board, player): 
	selection = possibilities(board) 
	current_loc = random.choice(selection) 
	board[current_loc] = player 
	return(board) 

# Checks whether the player has three 
# of their marks in a horizontal row 
def row_win(board, player): 
	for x in range(len(board)): 
		win = True
		
		for y in range(len(board)): 
			if board[x, y] != player: 
				win = False
				continue
				
		if win == True: 
			return(win) 
	return(win) 

# Checks whether the player has three 
# of their marks in a vertical row 
def col_win(board, player): 
	for x in range(len(board)): 
		win = True
		
		for y in range(len(board)): 
			if board[y][x] != player: 
				win = False
				continue
				
		if win == True: 
			return(win) 
	return(win) 

# Checks whether the player has three 
# of their marks in a diagonal row 
def diag_win(board, player): 
	win = True
	
	for x in range(len(board)): 
		if board[x, x] != player: 
			win = False
	return(win) 

# Evaluates whether there is 
# a winner or a tie 
def evaluate(board): 
	winner = 0
	
	for player in [1, 2]: 
		if (row_win(board, player) or
			col_win(board,player) or
			diag_win(board,player)): 
				
			winner = player 
			
	if np.all(board != 0) and winner == 0: 
		winner = -1
	return winner 

# Main function to start the game 
def play_game(): 
	board, winner, counter = create_board(), 0, 1
	print(board) 
	sleep(2) 
	
	while winner == 0: 
		for player in [1, 2]: 
			board = random_place(board, player) 
			print("Board after " + str(counter) + " move") 
			print(board) 
			sleep(2) 
			counter += 1
			winner = evaluate(board) 
			if winner != 0: 
				break
	return(winner) 

# Driver Code 
print("Winner is: " + str(play_game())) 




# Python3 program to check whether a given tic tac toe 
# board is valid or not 

# Returns true if char wins. Char can be either 
# 'X' or 'O' 
def win_check(arr, char): 
	# Check all possible winning combinations 
	matches = [[0, 1, 2], [3, 4, 5], 
			[6, 7, 8], [0, 3, 6], 
			[1, 4, 7], [2, 5, 8], 
			[0, 4, 8], [2, 4, 6]] 

	for i in range(8): 
		if(arr[matches[i][0]] == char and
			arr[matches[i][1]] == char and
			arr[matches[i][2]] == char): 
			return True
	return False

def is_valid(arr): 
	# Count number of 'X' and 'O' in the given board 
	xcount = arr.count('X') 
	ocount = arr.count('O') 
	
	# Board can be valid only if either xcount and ocount 
	# is same or xount is one more than oCount 
	if(xcount == ocount+1 or xcount == ocount): 
		# Check if O wins 
		if win_check(arr, 'O'): 
			# Check if X wins, At a given point only one can win, 
			# if X also wins then return Invalid 
			if win_check(arr, 'X'): 
				return "Invalid"

			# O can only win if xcount == ocount in case where whole 
			# board has values in each position. 
			if xcount == ocount: 
				return "Valid"

		# If X wins then it should be xc == oc + 1, 
		# If not return Invalid	 
		if win_check(arr, 'X') and xcount != ocount+1: 
			return "Invalid"
		
		# if O is not the winner return Valid 
		if not win_check(arr, 'O'): 
			return "Valid"
		
	# If nothing above matches return invalid 
	return "Invalid"


# Driver Code 
arr = ['X', 'X', 'O', 
	'O', 'O', 'X', 
	'X', 'O', 'X'] 
print("Given board is " + is_valid(arr)) 
