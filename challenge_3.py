#function for calculating BMI
def bmi_calculator(x,y):
    b=x/(y*y)
    return b;
a=float(input("enter your weight in Kg"))
b=float(input("enter your height in meters"))
bmi=bmi_calculator(a,b)
print("Your BMI is",bmi)