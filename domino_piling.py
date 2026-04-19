board = input().split()
board = [int(b) for b in board]

board = board[0] * board[1]

possible = board // 2
print(possible)
