# BMI CALCULATOR
#http://mercer-health.com/services/weight-management-center/bmi-calculator#:~:text=body%20mass%20index%2c%20or%20BMI.inches%20x%20height%20in%20inches

#BMI = (weight in pounds x 703 / (height in inches x height in inches)
name = input("Enter your name : ")
weight = int(input("Enter your weight in pounds : "))
height = int(input("Enter your height in inches : "))

BMI = (weight * 703 ) / (height  * height )
print("Your BMI is : ",BMI)

if BMI>0:
    if BMI<18.5:
        print(name+", Your are underweight")
    elif BMI<=24.9:
        print(name+", You are normalweight")
    elif BMI<29.9:
        print(name+", You are overweight")
    elif BMI<34.9:
        print(name+", You are obese")
    elif BMI<39.9:
        print(name+", You are severely obese")
    else:
        print(name+", You are morbidly obese")
else:
    print("Enter valid input")



# Enter your name : Tanishq
# Enter your weight in pounds : 170
# Enter your height in inches : 69
# Your BMI is :  25.101869355177485
# Tanishq, You are overweight