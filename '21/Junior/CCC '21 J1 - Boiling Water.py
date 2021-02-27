B = int(input())
P = (5 * B) - 400

print(P)

if P == 100 and B == 100:
  print("0")
  
if P < 100 and B < 100:
  print("1")
  
if P > 100 and B > 100:
  print("-1")
