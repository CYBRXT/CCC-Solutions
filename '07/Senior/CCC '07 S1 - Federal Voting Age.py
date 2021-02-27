a = int(input())

for i in range(a):
  b = str(input())
  c = b.split(" ")
  
  year = int(c[0])
  month = int(c[1])
  day = int(c[2])
  
  if year < 1989:
    print("Yes")
    
  elif year == 1989:
    pass
    
    if month == 2:
      pass
      
      if day <= 27:
        print("Yes")
        
      if day > 27:
        print("No")
        
    elif month < 2:
      print("Yes")
      
    elif month > 2:
      print("No")
      
  elif year > 1989:
    print("No")
