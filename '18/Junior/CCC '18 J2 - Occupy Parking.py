a = int(input())
b = input()
c = input()

parkingspacecounter = 0

listb = list(b)
listc = list(c)

for i in range(a):
  if listb[i] == "C" and listc[i] == "C":
    parkingspacecounter += 1
    
  else:
    pass
  
print(parkingspacecounter)
