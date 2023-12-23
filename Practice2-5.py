count = int(input("Enter the Number of Students: "))
sum = 0
min = 20
max = 0
for i in range(count):
    pMark = float(input("Enter the {0} Programing Mark: ".format(i+1)))
    sum += pMark
    if pMark > max:
       max = pMark
       if pMark < min:
            min = pMark
print("\nThe Highest Score: ", max, "\nThe Lowest Score: ", min,
      "\nClass Avg: ", sum/count)