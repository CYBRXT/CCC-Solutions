first_number = int(input())
second_number = int(input())

list = []
list.append(first_number)
list.append(second_number)

while True:
  for i in range(len(list)):
    next_number = list[-2] - list[-1]
    
  if next_number > list[-1]:
    list.append(next_number)
    break
    
  else:
    list.append(next_number)
    
print(len(list))
