def main():
	round(3)

PLAYER_CHARACTERS = ['X', 'O']

def round(n):
	# -1 = пустое, 0 = игрок 0, 1 = игрок 1
	board = [
		[-1 for _ in range(n)] for _ in range(n)
	]
	to_move = 0

	while not is_finished(board):
		print_board(board)
		r, c = get_move(to_move, board)
		board[r][c] = to_move
		to_move = 1 - to_move

	pass

def print_board(board):
	print(board)

def is_finished(board):
	return False

def get_move(to_move, board):
	print(f"{PLAYER_CHARACTERS[to_move]}'s turn. "
		+ "Enter row and column (e.g. 1 2): ")	
	r, c = map(int, input().split())	
	return r - 1, c - 1


if __name__ == '__main__':
	main()