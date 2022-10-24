
def div_by_two(x,y):
    try:
        print(x/y)
    except:
        print("There is a division by zero error")
a=int(input("enter the first number"))
b=int(input("enter the second number"))
div_by_two(a,b)