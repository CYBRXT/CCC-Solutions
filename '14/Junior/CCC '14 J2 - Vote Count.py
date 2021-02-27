a = int(input())
b = str(input())

VotesA = b.count("A")
VotesB = b.count("B")

if VotesA > VotesB:
  print("A")
  
elif VotesA < VotesB:
  print("B")
  
elif VotesA == VotesB:
  print("Tie")
