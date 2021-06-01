min = int(input())
max = int(input())

RSA = 0

for i in range(min, max + 1):
  counter = 0
  for j in range(1, max + 1):
    if i % j == 0:
      counter += 1
  if counter == 4:
    RSA += 1

print(f"The number of RSA numbers between {min} and {max} is {RSA}")
