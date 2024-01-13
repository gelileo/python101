# board = [["-", "-", "-"], 
#          ["-", "-", "-"], 
#          ["-", "-", "-"]]

board = [["-" for _ in range(3)] for _ in range(3)]


def printBoard(board):
  for row in board:
    print(f"{row[0]} | {row[1]} | {row[2]}")
    print("-" * 9)


# print(board[0][0])

# for num in [1,2,3]:
#   print(f"({num} -1 / 3)  = {(num - 1) // 3}")

# for num in [4,5,6]:
#   print(f"({num} -1 / 3)  = {(num-1) // 3}")

# for num in [7,8,9]:
#   print(f"({num} - 1 / 3)  = {(num-1) // 3}")

row = [0,0,0]
print(all(row[i] == row[0] for i in range(3)))

