number_of_coordinates = int(input())

x_coordinates, y_coordinates = [], []

for i in range(number_of_coordinates):
  coordinates = input()
  list = coordinates.split(",")
  x_coordinates.append(int(list[0]))
  y_coordinates.append(int(list[1]))
  
print(f"{min(x_coordinates)-1},{min(y_coordinates)-1}")
print(f"{max(x_coordinates)+1},{max(y_coordinates)+1}")
