x = int(input())
m = int(input())

for i in range(1, m+1):
  value = x * i
  
  if value % m == 1:
    print(i)
    break
  
  if i == m:
    print("No such integer exists.")
