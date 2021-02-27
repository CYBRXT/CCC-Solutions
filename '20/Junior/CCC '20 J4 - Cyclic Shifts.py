string = input()
check = input()

list = []

for i in range(len(check)):
  check = check[1:] + check[0]
  
  if check in string:
    print("yes")
    break
    
else:
  print("no")
