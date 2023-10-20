def timeTable(n):
  for i in range(1,n+1):
    for j in range(1, i+1):
      print(f'{i}x{j}={i*j}', end=", ")
    print()