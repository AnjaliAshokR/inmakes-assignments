def func(x):
    return lambda x:x*((x+5)*(x+5))
a=func(5)
print(a(5))