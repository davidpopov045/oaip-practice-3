import random
import os
from datetime import datetime


def main():
	done = False
	while not done:
		n = get_board_size()
		round(n)


		print('play once again? (type no to exit)', end=' ')
		s = input()
		if s == 'no':
			done = True
	print('bye!')



PLAYER_CHARACTERS = ['X', 'O']
TO_WIN = 3

def save_stats(n, status, move_no):	
	os.makedirs("stats", exist_ok=True)

	with open('stats/log.txt', 'a') as f:
		date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		if status == -1:
			res = 'draw'
		else:
			res = f'{PLAYER_CHARACTERS[status]} won'

		print(f'{date} {n=} {res} in {move_no} moves.', file=f)



def get_board_size():
	print('Enter the size of the board (3-9): ',
		end='')

	ok = False
	while not ok:	
		try:
			n = int(input())			
			if n < 3 or n > 9:				
				print(f'от 3 до 9!!!')			
			else:
				ok = True
		except ValueError:
			print('введите целое число')
	return n




def round(n):	
	# -1 = пустое, 0 = игрок 0, 1 = игрок 1
	board = [
		[-1 for _ in range(n)] for _ in range(n)
	]
	to_move = random.randint(0, 1)
	move_no = 0

	# -1 = draw, 0 = 0 won, 1 = 1 won
	status = -1

	while True:
		print_board(board)
		r, c = get_move(to_move, board)
		board[r][c] = to_move

		move_no += 1

		if is_finished(to_move, board, r, c):
			status = to_move
			break
		if move_no == n * n:
			break

		to_move = 1 - to_move

	print_board(board)
	if status == -1:
		print("draw")
	else:
		print(f"{PLAYER_CHARACTERS[status]} won")
	save_stats(n, status, move_no)

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

def is_finished(to_move, board, r, c):
	n = len(board)
	
	directions = [
		(0, 1), (1, 0),
		(-1, 1), (1, 1)
	]
	for dr, dc in directions:
		back = 0
		while True:
			r2 = r - (back + 1) * dr
			c2 = c - (back + 1) * dc
			if not valid_square(n, r2, c2):
				break
			if board[r2][c2] != to_move:
				break
			if back == TO_WIN:
				break
			back += 1

		forward = 0
		while True:
			r2 = r + (forward + 1) * dr
			c2 = c + (forward + 1) * dc
			if not valid_square(n, r2, c2):
				break
			if board[r2][c2] != to_move:
				break
			if back == TO_WIN:
				break
			forward += 1

		if forward + back + 1 >= TO_WIN:
			return True

	return False

def valid_square(n, r, c):
	return (r >= 0 and r < n
		and c >= 0 and c < n)


def get_move(to_move, board):
	n = len(board)
	print(f"{PLAYER_CHARACTERS[to_move]}'s turn. "
		+ "Enter row and column (e.g. 1 2): ",
		end=" ")

	ok = False
	while not ok:	
		try:
			r, c = map(int, input().split())
			r -= 1
			c -= 1
			if not valid_square(n, r, c):
				print(f'числа в пределах от 1 до {n}')
			elif board[r][c] != -1:
				print('клетка занята!')
			else:
				ok = True
		except ValueError:
			print('введите два числа через пробел')


	return r, c


if __name__ == '__main__':
	main()