from tkinter import *
from  tkinter import ttk
from PIL import ImageTk,Image

win=Tk()

# Set the size of the window
win.geometry("700x350")

l = Label(win,text='VISITOR MANAGEMENT SYSTEM')
l.config(font=("Eczar semibold",30),pady=10,bg="purple",fg="gold")
l.pack()

#b3.pack(anchor=CENTER)

frame = Frame(win,borderwidth=3,background="purple",relief=SUNKEN)
frame.pack(side=TOP,pady=20,anchor="nw")

tree = ttk.Treeview(win, column=("ID", "Name", "Contact No."), show='headings', height=20)
tree.pack(side=BOTTOM,anchor="sw",padx=10,pady=10)

tree.column("# 1",anchor=CENTER)
tree.heading("# 1", text="ID")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Name")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="Contact No")

tree.insert('', 'end', text="10", values=('111', 'Chinmay', '789342394'))
tree.insert('', 'end', text="10", values=('112', 'Mahadev', '984375473'))
tree.insert('', 'end', text="10", values=('113', 'Omkar', '177033434'))
tree.insert('', 'end', text="10", values=('114', 'Mohak', '732498723'))

b1 = Button(fg="red",text="Available",width=40, font=("arial",25),bg="light blue")  #need to add Command= to execute any function(backend part)
b1.pack(side=LEFT,anchor='n',fill=X)

b2 = Button(fg="red",text="Not Available",width=40, font=("arial",25),bg="light blue")  #need to add Command= to execute any function(backend part)
b2.pack(side=RIGHT,anchor='n',fill=X)



tree = ttk.Treeview(win, column=("ID", "Name", "Contact No."), show='headings', height=20)
tree.pack(side=BOTTOM,anchor="sw",padx=10,pady=10)

tree.column("# 1",anchor=CENTER)
tree.heading("# 1", text="ID")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Name")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="Contact No")

tree.insert('', 'end', text="10", values=('111', 'Chinmay', '789342394'))
tree.insert('', 'end', text="10", values=('112', 'Mahadev', '984375473'))
tree.insert('', 'end', text="10", values=('113', 'Omkar', '177033434'))
tree.insert('', 'end', text="10", values=('114', 'Mohak', '732498723'))



win.mainloop()