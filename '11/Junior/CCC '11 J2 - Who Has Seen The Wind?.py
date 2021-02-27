h = int(input())
M = int(input())
t = 1

while True:
  A = (-6 * (t ** 4)) + (h * (t ** 3)) + (2 * (t ** 2) + t
  
  if A <= 0:
    print("The balloon first touches ground at hour:")
    print(t)
    break
    
  elif t == M:
    print("The balloon does not touch ground in the given time.")
    break
    
  elif A != 0:
    t += 1
