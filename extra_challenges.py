months=["January","February","March","April","May","June","July","August","September","October","Nonember","December"]
def month_check(x):
    try:
        if x!=0:
            x=x-1
            print(months[x])
        else:
            print("Enter a value between 1 and 12")
    except:
            print("this is not the correct number try using a number between 1 and 12")
v=int(input("enter the value"))
month_check(v)
