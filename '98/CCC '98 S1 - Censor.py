a = int(input())

for i in range(a):
  d = []
  b = str(input())
  c = b.split(" ")
  
  for j in range(len(c)):
    if len(c[j]) == 4:
      d.append("****")
    if len(c[j]) != 4:
      d.append(c[j])
    x = " ".join(d)
    
  print(x)
