previous_instruction = ""

while True:
  code = input()
  
  if code == "99999":
    break
    
  list = []
  
  for i in range(5):
    list.append(code[i])
    
  sum = int(list[0]) + int(list[1])
  
  if sum != 0:
    type = sum % 2
    
    if type == 0:
      previous_instruction = ""
      previous_instruction += "right"
      print(f"right {list[2]}{list[3]}{list[4]}")
      
    if type != 0:
      previous_instruction = ""
      previous_instruction += "left"
      print(f"left {list[2]}{list[3]}{list[4]}")
      
  if sum == 0:
    print(f"{previous_instruction} {list[2]}{list[3]}{list[4]}")
