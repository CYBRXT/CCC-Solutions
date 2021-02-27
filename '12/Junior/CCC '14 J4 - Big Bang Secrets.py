K = int(input())
code = str(input())
position = 0
list0, list1, list2, list3 = [], [], [], []

for i in range(len(code)):
  list0.append(ord(code[i])-64)
  
for j in range(len(list0)):
  position += 1
  shift = (3*position) + K
  list1.append(shift)
  
for k in range(len(list1)):
  originalvalue = list0[k] - list1[k]
  
  if originalvalue <= 0:
    originalvalue += 26
  list2.append(originalvalue)
  
for l in range(len(list2)):
  final = list2[l] + 64
  list3.append(chr(final))
  
for m in range(len(list3)):
  print(list3[m], end = "")
