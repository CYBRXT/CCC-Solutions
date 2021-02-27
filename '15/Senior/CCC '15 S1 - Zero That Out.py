number = int(input())
list = []

for i in range(number):
  a = int(input())
  list.append(a)
  
  if a == 0:
    list.pop(-1)
    list.pop(-1)
    
print(sum(list))
