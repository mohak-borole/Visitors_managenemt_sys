import mysql.connector
import tkinter  as tk 
from tkinter import * 
my_w = tk.Tk()
my_w.geometry("800x600") 
my_connect = mysql.connector.connect(
  host="localhost",
  user="root", 
  passwd="T21057",
  database="visitorinfo"
)

my_conn = my_connect.cursor()
####### end of connection ####
my_conn.execute("SELECT * FROM visitor limit 0,10")

e=Label(my_w,width=10,text='Id',borderwidth=2, relief='ridge',anchor=CENTER,bg='yellow')
e.grid(row=0,column=0)
e=Label(my_w,width=10,text='Name',borderwidth=2, relief='ridge',anchor=CENTER,bg='yellow')
e.grid(row=0,column=1)
e=Label(my_w,width=10,text='phone NO',borderwidth=2, relief='ridge',anchor=CENTER,bg='yellow')
e.grid(row=0,column=2)
i=1
b3 = Button(fg="red",text="Not Available",width=40, font=("arial",25),bg="light blue")  #need to add Command= to execute any function(backend part)
b3.place(x=200,y=300)
#i=0 
for visitor in my_conn: 
    for j in range(len(visitor)):
        e = Label(my_w,width=10, text=visitor[j],borderwidth=2,relief='ridge', anchor=CENTER)  
        e.grid(row=i, column=j) 
        #e.insert(END, visitor[j])
    i=i+1
 
my_w.mainloop()