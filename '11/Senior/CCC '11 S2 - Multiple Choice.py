N = int(input())

counter = 0

list0 = []
list1 = []

for i in range(N):
  a = str(input())
  list0.append(a)
  
for j in range(N):
  b = str(input())
  list1.append(b)
  
for k in range(len(list0)):
    if list0[k] == list1[k]:
      counter += 1
      
print(counter)
