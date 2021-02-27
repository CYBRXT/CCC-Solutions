t = int(input())
s = int(input())
h = int(input())

midsegment = (2 * s) + 3

for i in range(t):
  print("*" + (" " * s) + "*" + (" " * s) + "*")
  
print("*" * midsegment)

for j in range(h):
  print(" " * (s+1) + "*")
