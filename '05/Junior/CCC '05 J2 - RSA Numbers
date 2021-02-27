a = int(input())
b = int(input())

RSA = 0

counter = 0

for x in range(a, b):
 for y in range(1, b):
    if x % y == 0:
      counter += 1
      
if counter == 4:
  RSA += 1
  
txt = "The number of RSA numbers between {} and {} is {}"
print(txt.format(a, b, RSA))
