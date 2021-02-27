two = ["A", "B", "C"]
three = ["D", "E", "F"]
four = ["G", "H", "I"]
five = ["J", "K", "L"]
six = ["M", "N", "O"]
seven = ["P", "Q", "R", "S"]
eight = ["T", "U", "V"]
nine = ["W", "X", "Y", "Z"]

t = int(input())

for i in range(t):
  list = []
  phone_number = input()
  
  for j in range(len(phone_number)):
    list.append(phone_number[j])
  
  for k in range(len(list)):
    if list[k] in two:
      list.remove(list[k])
      list.insert(k, "2")
      
    if list[k] in three:
      list.remove(list[k])
      list.insert(k, "3")
      
    if list[k] in four:
      list.remove(list[k])
      list.insert(k, "4")
      
    if list[k] in five:
      list.remove(list[k])
      list.insert(k, "5")
      
    if list[k] in six:
      list.remove(list[k])
      list.insert(k, "6")
      
    if list[k] in seven:
      list.remove(list[k])
      list.insert(k, "7")
      
    if list[k] in eight:
      list.remove(list[k])
      list.insert(k, "8")
      
    if list[k] in nine:
      list.remove(list[k])
      list.insert(k, "9")
      
  if "-" in list:
    while "-" in list:
      list.remove("-")
      
  print(f"{list[0]}{list[1]}{list[2]}-{list[3]}{list[4]}{list[5]}-{list[6]}{list[7]}{list[8]}{list[9]}")
