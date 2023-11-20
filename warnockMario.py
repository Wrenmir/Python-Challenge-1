def draw(ctype, times):
  """
  draw(ctype, times)
    input:
      ctype - char or string to draw
      times - number of times to draw
    output:
      prints type n times with no "\n" appended at the end
  """
  print(ctype * times, end="")
  
def main():
  while True:
    height = int(input("Height: "))
    if height >= 1 and height <= 8:
      break
  nhash = 1
  for i in range(height):
    draw(" ", height - i - 1)
    draw("#", nhash + 1)
    draw(" ", 2)
    draw("#", nhash + i)
    print()

if __name__ == "__main__":
  main()

#credits: https://github.com/tektite00/cs50/blob/master/pset6/sentimental/mario/more/mario.py
