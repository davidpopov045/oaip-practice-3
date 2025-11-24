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
	n = len(board)
	print("  "
		+ ' '.join(
			map(str, 
				range(1, n + 1))))
	for i, r in enumerate(board):
		print(f'{i + 1} '
			+ ' '.join(map(				
				lambda x: 
				'.' if x == -1 
				else PLAYER_CHARACTERS[x], 
				r)))

def is_finished(board):
	return False

def get_move(to_move, board):
	print(f"{PLAYER_CHARACTERS[to_move]}'s turn. "
		+ "Enter row and column (e.g. 1 2): ")	
	r, c = map(int, input().split())	
	return r - 1, c - 1


if __name__ == '__main__':
	main()