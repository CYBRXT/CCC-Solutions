a = int(input())

for i in range(a):
  code = input()
  list = code.split(" ")
  multiply = int(list[0])
  finalcode= multiply*list[1]
  print(finalcode)
