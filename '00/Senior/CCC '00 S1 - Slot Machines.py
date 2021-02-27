numberofquarters = int(input())
machine1counter = int(input())
machine2counter = int(input())
machine3counter = int(input())

playcounter = 0

while True:
  machine1counter += 1
  playcounter += 1
  numberofquarters -= 1
  
  if machine1counter == 35:
    numberofquarters += 30
    machine1counter = 0
    
  if numberofquarters == 0:
    break
  machine2counter += 1
  playcounter += 1
  numberofquarters -= 1
  
  if machine2counter == 100:
    numberofquarters += 60
    machine2counter = 0
    
  if numberofquarters == 0:
    break 
  machine3counter += 1
  playcounter += 1
  numberofquarters -= 1
  
  if machine3counter == 10:
    numberofquarters += 9
    machine3counter = 0
    
  if numberofquarters == 0:
    break
    
print("Martha plays {} times before going broke.".format(playcounter))
