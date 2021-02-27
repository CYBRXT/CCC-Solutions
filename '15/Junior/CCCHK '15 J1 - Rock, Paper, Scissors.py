games = int(input())
alicegame = input()
bobgame = input()
wincounteralice = 0
wincounterbob = 0
alicelist = alicegame.split(" ")
boblist = bobgame.split(" ")

for i in range(games):
  if alicelist[i] == "rock" and boblist[i] == "paper":
    wincounterbob += 1
    
  elif alicelist[i] == "rock" and boblist[i] == "scissors":
    wincounteralice += 1
    
  elif alicelist[i] == "paper" and boblist[i] == "rock":
    wincounteralice += 1
    
  elif alicelist[i] == "paper" and boblist[i] == "scissors":
    wincounterbob += 1
    
  elif alicelist[i] == "scissors" and boblist[i] == "rock":
    wincounterbob += 1
    
  elif alicelist[i] == "scissors" and boblist[i] == "paper":
    wincounteralice += 1
    
  elif boblist[i] == "rock" and alicelist[i] == "paper":
    wincounteralice += 1
    
  elif boblist[i] == "rock" and alicelist[i] == "scissors":
    wincounterbob += 1
    
  elif boblist[i] == "paper" and alicelist[i] == "rock":
    wincounterbob += 1
    
  elif boblist[i] == "paper" and alicelist[i] == "scissors":
    wincounteralice += 1
    
  elif boblist[i] == "scissors" and alicelist[i] == "rock":
    wincounteralice += 1
    
  elif boblist[i] == "scissors" and alicelist[i] == "paper":
    wincounteralice += 1
    
  elif boblist[i] == alicelist[i]:
    pass
  
totalwins = "{} {}"

print(totalwins.format(wincounteralice, wincounterbob)) 
