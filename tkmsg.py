from tkinter import  *
class student:
    def __init__(self, root):
        Label(root, text="Student Portal").pack()
        frame = Frame(root)
        frame.pack()
        self.ebutton=Button(frame,text="Log in", command=self.emsg)
        self.ebutton.pack()
        self.exbutton=Button(frame,text="Exit", command=self.exmsg)
        self.exbutton.pack()
        self.qbutton=Button(frame, text="Quit", command=frame.quit)
        self.qbutton.pack()
    def emsg(self):
        print("Welcome to the account")
    def exmsg(self):
        print("You are exiting the account")

root_new=Tk()
ob=student(root_new)
root_new.mainloop()