a = float(input("Enter your Weight(kg): "))
b = float(input("Enter your Height(m): "))
Bmi = a/(b*b)
print("Your Bmi is: ", Bmi)
if Bmi < 18.5:
    print("Under weight!")
elif 18.5 < Bmi < 24.5:
    print("You Are Healthy :)")
elif 25 < Bmi < 29.9:
    print("Over Weight!")
elif Bmi > 30:
    print("You Are Over Weight :(")