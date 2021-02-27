a = int(input())
b = int(input())
c = int(input())

daycostA = (a - 100) * 0.25

if daycostA < 0:
  daycostA = 0
  
eveningcostA = b * 0.15
weekendcostA = c * 0.2

daycostB = (a - 250) * 0.45

if daycostB < 0:
  daycostB = 0
  
eveningcostB = b * 0.35
weekendcostB = c * 0.25

costplanA = daycostA + eveningcostA + weekendcostA

costA = round(costplanA, 2)

costplanB = daycostB + eveningcostB + weekendcostB

costB = round(costplanB, 2)

txtA = ("Plan A costs {}")
txtB = ("Plan B costs {}")

print(txtA.format(costA))
print(txtB.format(costB))

if costA < costB:
  print("Plan A is cheapest.")
  
elif costA > costB:
  print("Plan B is cheapest.")
  
elif costA == costB:
  print("Plan A and B are the same price.")
