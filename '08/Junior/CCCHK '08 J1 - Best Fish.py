casper_fish = int(input())

cproduct = []
nproduct = []

for i in range(casper_fish):
  cfishcaught = input()
  split = cfishcaught.split(" ")
  cproduct.append(int(split[0]) * int(split[1]))
  
natalie_fish = int(input())

for j in range(natalie_fish):
  nfishcaught = input()
  split2 = nfishcaught.split(" ")
  nproduct.append(int(split2[0]) * int(split2[1]))
  
if max(cproduct) > max(nproduct):
  print("Casper")
  
elif max(nproduct) > max(cproduct):
  print("Natalie")
  
elif max(cproduct) == max(nproduct):
  print("Tie")
