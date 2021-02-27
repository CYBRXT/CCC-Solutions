n = int(input())
m = int(input())

list, list1 = [], []

for i in range(n):
  adjectives = str(input())
  list.append(adjectives)
  
for j in range(m):
  nouns = str(input())
  list1.append(nouns)
  
for k in range(len(list)):
  for l in range(len(list1)):
    print("{} as {}".format(list[k], list1[l]))
