def student(x):
    new_p= (x*90)/100
    return new_p;
def normal_discount(y):
    new_price=(y*95)/100
    return new_price;
i=int(input("Enter the price"))
print("price after the student discount is", student(i))
print("price after the discount is", normal_discount(i))
print("price after the combined discount is", normal_discount(student(i)))
