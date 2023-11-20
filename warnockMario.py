height = int(input("Give me an integer for the height of the half-pyramids: "))
while not isinstance(height,int):
  height = int(input("Please give me an integer: "))
for number in range(height):
  for i in range(number):
    print(number, end=" ")
    print(" ")
