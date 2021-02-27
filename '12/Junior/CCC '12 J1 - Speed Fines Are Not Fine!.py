a = int(input())
b = int(input())

if b <= a:
 print("Congratulations, you are within the speed limit!")
 
elif b in (range(a+1, a+21)):
 print("You are speeding and your fine is $100.")
 
elif b in (range(a+21, a+31)):
 print("You are speeding and your fine is $270.")
 
elif b >= a+31:
  print("You are speeding and your fine is $500.")
