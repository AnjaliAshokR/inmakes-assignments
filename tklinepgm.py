from tkinter import  *
root= Tk()
c= Canvas(root, width=100, height=500)
c.pack()
new_l=c.create_line(0,0,7, 100)
n=c.create_oval(0,3,70,100)
root.mainloop()