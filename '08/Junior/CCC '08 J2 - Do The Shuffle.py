playlist = ["A", "B", "C", "D", "E"]

while True:
  b = int(input())
  n = int(input())
  for x in range(n):
    if b == 1:
      playlist.extend(playlist[0])
      playlist.remove(playlist[0])
    elif b == 2:
      playlist.insert(0, playlist[4])
      playlist.pop()
    elif b == 3:
      playlist2 = playlist.copy()
      playlist[0] = playlist2[1]
      playlist[1] = playlist2[0]
    elif b == 4:
      print(playlist[0], end = " ")
      print(playlist[1], end = " ")
      print(playlist[2], end = " ")
      print(playlist[3], end = " ")
      print(playlist[4])
      break
