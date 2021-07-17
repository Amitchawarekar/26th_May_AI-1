import tkinter as tk    #it is aliaas
app=tk.Tk()
app.title("My registration form")
app.geometry('500x300')

def register():
     f =open('data1.csv','w')
     data=[f_name.get(),email.get(),u_name.get(),pwd.get(),age.get(),mobile.get()]
     f.write(','.join(data)+'\n')
     f.close()
     f_name.set('')
     email.set('')
     u_name.set('')
     pwd.set('')
     age.set('')
     mobile.set('')
     
   


f_name=tk.Variable(app)
email=tk.Variable(app)
u_name=tk.Variable(app)
pwd=tk.Variable(app)
age=tk.Variable(app)
mobile=tk.Variable(app)


tk.Label(app,text="Full Name").place(x=20,y=30)

tk.Label(app,text="Email ID").place(x=20,y=60)
tk.Label(app,text="User Name").place(x=20,y=90)
tk.Label(app,text="Password").place(x=20,y=120)
tk.Label(app,text="Age").place(x=20,y=150)
tk.Label(app,text="Mobile").place(x=20,y=180)

tk.Entry(app,textvariable=f_name,width=20,bg='#ffffff').place(x=100,y=30)
tk.Entry(app,textvariable=email,width=20,bg='#ffffff').place(x=100,y=60)
tk.Entry(app,textvariable=u_name,width=20,bg='#ffffff').place(x=100,y=90)
tk.Entry(app,textvariable=pwd,width=20,bg='#ffffff').place(x=100,y=120)
tk.Entry(app,textvariable=age,width=20,bg='#ffffff').place(x=100,y=150)
tk.Entry(app,textvariable=mobile,width=20,bg='#ffffff').place(x=100,y=180)

tk.Button(app,text="Submit",bg='#ffffff',command=register).place(x=100,y=200)

app.mainloop()

