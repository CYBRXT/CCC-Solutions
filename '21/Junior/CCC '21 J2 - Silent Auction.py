N = int(input())

name, value = [], []

for i in range(N):
  a = input()
  b = int(input())
  name.append(a)
  value.append(b)
  
x = value.index(max(value))

print(name[x])
