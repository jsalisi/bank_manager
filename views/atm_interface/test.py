from tkinter import *

root = Tk()

photo = PhotoImage(file='ad.png')
label = Label(root, image=photo)
label.pack()
root.mainloop()