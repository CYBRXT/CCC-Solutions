aromatic_number = input()
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
sum = 0
next_base_value = 0
total = []
A, R = [], []

for i in range(len(aromatic_number)):
  if aromatic_number[i] in numbers:
    A.append(int(aromatic_number[i]))
  if aromatic_number[i] not in numbers:
    R.append(aromatic_number[i])
    
for j in range(len(R)):
  if R[j] == "I":
    R.remove(R[j])
    R.insert(j, 1)
    
  if R[j] == "V":
    R.remove(R[j])
    R.insert(j, 5)
    
  if R[j] == "X":
    R.remove(R[j])
    R.insert(j, 10)
    
  if R[j] == "L":
    R.remove(R[j])
    R.insert(j, 50)
    
  if R[j] == "C":
    R.remove(R[j])
    R.insert(j, 100)
    
  if R[j] == "D":
    R.remove(R[j])
    R.insert(j, 500)
    
  if R[j] == "M":
    R.remove(R[j])
    R.insert(j, 1000)
    
for k in range(len(R) - 1):
  product = A[k] * R[k]
  total.append(product)
  next_base_value = 0
  next_base_value += R[k+1]
  
  if next_base_value > R[k]:
    total[k] *= -1
    
for l in range(1):
  product = A[-1] * R[-1]
  total.append(product)
  
for m in range(len(total)):
  sum += total[m]
  
print(sum)
