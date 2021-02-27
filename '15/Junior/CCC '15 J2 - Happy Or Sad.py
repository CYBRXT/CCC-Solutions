a = str(input())
a.count(":-)")
a.count(":-(")

if a.count(":-)") == a.count(":-(") and ":-)" and ":-(" in a:
  print("unsure")
  
elif a.count(":-)") > a.count(":-("):
  print("happy")
  
elif a.count(":-)") < a.count(":-("):
  print("sad")
  
else:
  print("none")
