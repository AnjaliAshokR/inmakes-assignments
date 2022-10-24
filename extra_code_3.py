t = ("apple", "orange", "cherry", "pine apple", "grapes")
print(t)
n=("berry",)
t+=n
print(t)
l=list(t)
l.insert(0,"banana")
print(l)
l.append("starwberry")
t=tuple(l)
print(t)
# index of the second element from the last
print(t[len(t)-2])
