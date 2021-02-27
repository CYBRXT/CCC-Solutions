question = int(input())
nparticipants = int(input())

dmoj = list(map(int,input().split(" ")))
peg = list(map(int,input().split(" ")))

total_speed = 0
pair = []

if question == 1:
  for i in range(nparticipants):
    pair = []
    pair.append(max(dmoj))
    pair.append(max(peg))
    dmoj.remove(max(dmoj))
    peg.remove(max(peg))
    total_speed += max(pair)
    
if question == 2:
  for j in range(nparticipants):
    pair = []
    pair.append(max(dmoj))
    pair.append(min(peg))
    dmoj.remove(max(dmoj))
    peg.remove(min(peg))
    total_speed += max(pair)
    
print(total_speed)
