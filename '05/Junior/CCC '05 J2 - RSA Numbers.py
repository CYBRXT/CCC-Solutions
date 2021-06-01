min = int(input())
max = int(input())

RSA = 0

counter = 0

for x in range(min, max):
 for y in range(1, max):
    if x % y == 0:
      counter += 1
      
if counter == 4:
  RSA += 1
  
print(f"The number of RSA numbers between {min} and {max} is {RSA}")
