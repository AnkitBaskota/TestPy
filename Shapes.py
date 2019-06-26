from tkinter import *

root = Tk()
root.geometry()
c = Canvas(root, height=250, width=300, bg="white")

baseLine = c.create_line(-100, 100, 50, 80, width=5)


line = c.create_line(0, 0, 0, 100, width=10)


c.pack()

root.mainloop()
