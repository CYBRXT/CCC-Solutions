a = str(input())
b = str(input())
c = str(input())
d = str(input())
e = str(input())
f = str(input())

group = [a, b, c, d, e, f]
group.count("W")

if group.count("W") == 5 or group.count("W") == 6:
  print("1")
  
elif group.count("W") == 3 or group.count("W") == 4:
  print("2")
  
elif group.count("W") == 1 or group.count("W") == 2:
  print("3")
  
elif group.count("W") == 0:
  print("-1")
