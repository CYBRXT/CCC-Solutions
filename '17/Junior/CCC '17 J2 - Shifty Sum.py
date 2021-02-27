N = int(input())
k = int(input())

ssum = N

for i in range(1,k+1):
  ssum += (N * (10 ** i))
  
print(ssum)
