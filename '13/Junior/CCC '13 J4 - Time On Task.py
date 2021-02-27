max_time = int(input())
number_of_chores = int(input())
list = []
max_chores = 0

for i in range(number_of_chores):
  chores = int(input())
  list.append(chores)
  
list.sort()

while True:
  max_time -= min(list)
  
  if max_time < 0:
    break
    
  else:
    max_chores += 1
    list.remove(min(list))
    
print(max_chores)
