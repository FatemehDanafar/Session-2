nf = input("Please Enter your Name & your LastName: ")
mark1 = float(input("Enter Your MathMark: "))
mark2 = float(input("Enter Your HistoryMark: "))
mark3 = float(input("Enter Your P.EMark: "))
avg = round((mark1+mark2+mark3)/3,2)
print("Ms/Mr", nf, "your avg is:", avg, "and you are")
if avg < 12:
    print("Fail :( ")
elif avg == 20:
    print("Great :) ")
elif 13 <= avg <= 17:
    print("Normal!")


