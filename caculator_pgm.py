import parser
from tkinter import *
root=Tk()
root.title("Calculator")
display_box= Entry(root)
p=0
def get_var(n):
   global p
   display_box.insert(p,n)
   p+=1
def clear_display():
    display_box.delete(0,END)
def undo():
    text=display_box.get()
    if len(text):
        new_text=text[:-1]
        clear_display()
        display_box.insert(0,new_text)
    else:
        clear_display()
        display_box.insert(0, "ERROR!")
def get_operator(o):
    global p
    l=len(o)
    display_box.insert(p, o)
    p+=l
def operations():
    text=display_box.get()
    try:
        a= parser.expr(text).compile()
        out=eval(a)
        clear_display()
        display_box(0,out)
    except EXCEPTION:
        clear_display()
        display_box.insert(0,"ERROR!")

display_box.grid(row=0, columnspan=6, sticky=W+E)
# buttons of calculator
Button(root,text="CE",command= lambda :clear_display()).grid(row=1, column=0)
Button(root,text="^2",command=lambda :get_operator('**2')).grid(row=1, column=1)
Button(root,text="x!").grid(row=1, column=2)
Button(root,text="+",command=lambda :get_operator('+')).grid(row=1, column=3)
Button(root,text="7", command= lambda :get_var(7)).grid(row=2, column=0)
Button(root,text="8",command= lambda :get_var(8)).grid(row=2, column=1)
Button(root,text="9", command= lambda :get_var(9)).grid(row=2, column=2)
Button(root,text="-",command=lambda :get_operator('-')).grid(row=2, column=3)
Button(root,text="4", command= lambda :get_var(4)).grid(row=3, column=0)
Button(root,text="5", command= lambda :get_var(5)).grid(row=3, column=1)
Button(root,text="6",command= lambda :get_var(6)).grid(row=3, column=2)
Button(root,text="*",command=lambda :get_operator('*')).grid(row=3, column=3)
Button(root,text="1", command= lambda :get_var(1)).grid(row=4, column=0)
Button(root,text="2",command= lambda :get_var(2)).grid(row=4, column=1)
Button(root,text="3", command= lambda :get_var(3)).grid(row=4, column=2)
Button(root,text="/",command=lambda :get_operator('/')).grid(row=4, column=3)
Button(root,text="%",command=lambda :get_operator('%')).grid(row=5, column=0)
Button(root,text="0", command= lambda :get_var(0)).grid(row=5, column=1)
Button(root,text="(",command=lambda :get_operator('(')).grid(row=5, column=2)
Button(root,text=")",command=lambda :get_operator(')')).grid(row=5, column=3)
Button(root,text="<-",command= lambda :undo()).grid(row=1, column=4)
Button(root,text="exp",command=lambda :get_operator('**')).grid(row=2, column=4)
Button(root,text="pi",command=lambda :get_operator('*3.14')).grid(row=3, column=4)
Button(root,text="1/x").grid(row=4, column=4)
Button(root,text="=",command=lambda : operations()).grid(row=5, column=4)
root.mainloop()