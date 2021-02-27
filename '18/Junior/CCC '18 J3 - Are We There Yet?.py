distances = input()

temp = distances.split(" ")

list = []

for i in range(len(temp)):
  list.append(int(temp[i]))
  
print(f"{0} {list[0]} {sum(list[0:2])} {sum(list[0:3])} {sum(list)}")

print(f"{list[0]} {0} {list[1]} {sum(list[1:3])} {sum(list[1:])}")

print(f"{sum(list[:2])} {list[1]} {0} {list[2]} {sum(list[2:])}")

print(f"{sum(list[:3])} {sum(list[1:3])} {list[2]} {0} {list[3]}")

print(f"{sum(list)} {sum(list[1:])} {sum(list[2:])} {list[3]} {0}")
