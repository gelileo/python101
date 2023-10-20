from TimeTable import timeTable

white_block = "️⬜"
black_block = "🟧"
# black_block = " "

def printRow():
  print((white_block+black_block)*4)
  
def printBoard():
  for i in range(8):
    printRow()

# printBoard()
timeTable(5)
