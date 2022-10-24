# function for calcualting the simple interest
def simple_interest(p,n,r):
    s=(p*n*r)/100
    print("Simple interest is", s)
a=int(input("Enter the principle amount"))
b=int(input("Enter the interest rate "))
c=int(input("Enter the number of years"))
simple_interest(a,c,b)