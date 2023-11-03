
def timeTable(num):
  for i in range(1,num+1):
    for j in range(1,num+1):
      if i != j:
        print(f"{i}x{j}={i*j}" , end=', ')
      else:
        print(f"{i}x{j}={i*j}")
        break

#for i in range(1,10):
#  timeTable(i)
#  print()
  
def timeTable2(num):
  for i in range(1 , num+1):
    for j in range(1 , i):
      print(f"{i}x{j}={i*j}" , end=', ')
    print(f"{i}x{i}={i*i}")
    
# timeTable2(8)

