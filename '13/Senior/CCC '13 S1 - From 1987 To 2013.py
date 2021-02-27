startingyear = int(input())

while True:
  counter = 0 
  rangea = len(str(startingyear))
  startingyear += 1
  finalyear = str(startingyear)
  
  for i in range(rangea):
    for j in range(rangea):
      if finalyear[i] == finalyear[j]:
        counter += 1
        
  if counter == rangea:
    print(finalyear)
    break
