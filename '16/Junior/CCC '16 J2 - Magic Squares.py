a = list(map(int,input().split(" ")))
b = list(map(int,input().split(" ")))
c = list(map(int,input().split(" ")))
d = list(map(int,input().split(" ")))

A = sum(a)
B = sum(b)
C = sum(c)
D = sum(d)

VsumA = a[0] + b[0] + c[0] + d[0]
VsumB = a[1] + b[1] + c[1] + d[1]
VsumC = a[2] + b[2] + c[2] + d[2]
VsumD = a[3] + b[3] + c[3] + d[3]

if A == B == C == D == VsumA == VsumB == VsumC == VsumD:
  print("magic")
  
else:
  print("not magic")
