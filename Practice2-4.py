import random
while True:
  a = (random.randint(1, 6))
  print("The Number is:", a)
  if a == 6:
    print("Nice! One more time for your gift")
    b = (random.randint(1, 6))
    print("your gift:", b)
    break


