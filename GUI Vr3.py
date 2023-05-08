import mysql.connector
import tkinter  as tk 
from tkinter import * 
my_w = tk.Tk()
#my_w.geometry("800x600") 
my_w.title("VISITOR'S MANAGEMENT SYSTEM: ")
my_w.configure(background="purple")
my_connect = mysql.connector.connect(
  host="localhost",
  user="root", 
  passwd="T21057",
  database="visitorinfo"
)

my_conn = my_connect.cursor()
####### end of connection ####
my_conn.execute("SELECT * FROM visitor limit 0,10")

e=Label(my_w,width=20,text='Id',borderwidth=10, relief='ridge',anchor=CENTER,bg='yellow')
e.grid(row=0,column=0)
e=Label(my_w,width=20,text='Name',borderwidth=10, relief='ridge',anchor=CENTER,bg='yellow')
e.grid(row=0,column=1)
e=Label(my_w,width=20,text='phone NO',borderwidth=10, relief='ridge',anchor=CENTER,bg='yellow')
e.grid(row=0,column=2)
e=Label(my_w,width=20,text='Allow',borderwidth=10, relief='ridge',anchor=CENTER,bg='yellow')
e.grid(row=0,column=3)
e=Label(my_w,width=20,text='Wait',borderwidth=10, relief='ridge',anchor=CENTER,bg='yellow')
e.grid(row=0,column=4)


# b1 = Button(fg="red",text="Allow",width=10,bg="light blue")#need to add Command= to execute any function(backend part)
# b1.grid(row=1,column=4)
# b2 = Button(fg="red",text="Wait",width=10,bg="light blue")#need to add Command= to execute any function(backend part)
# b2.grid(row=1,column=5)

#b3.place(x=200,y=300)
#i=0 

variable = 1
def make_something(value):
    global variable
    variable = value

#b3=Button(fg="white",text="register person",width=20,bg="green")
#b3.grid(row=3,column=5)
#b4=Button(fg="white",text="remove person",width=20,bg="red")
#b4.grid(row=5,column=5)

i=1
for visitor in my_conn: 
    for j in range(len(visitor)):
        e = Label(my_w,width=20, text=visitor[j],borderwidth=2,relief='ridge', anchor=CENTER,bg="orange")  
        e.grid(row=i, column=j) 
        #e.insert(END, visitor[j])
    
    b1 = Button(fg="red",text="Allow",width=10,bg="light blue",command=lambda *args: make_something(j))#need to add Command= to execute any function(backend part)
    b1.grid(row=i,column=j+1)
    b2 = Button(fg="red",text="Wait",width=10,bg="light blue",command=lambda *args: make_something(j))#need to add Command= to execute any function(backend part)
    b2.grid(row=i,column=j+2)
    i=i+1

 
my_w.mainloop()
