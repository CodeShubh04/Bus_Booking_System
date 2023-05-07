from tkinter import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=10,padx=w//3)
Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='Arial 14 bold').grid(row=1,column=0,columnspan=10)
Label(root,text='Add New Details To Database',bg='white',fg='green',font='Arial 11 bold').grid(row=2,column=0,columnspan=10,pady=20)

def fun1():
    root.destroy()
    import AddBusOperatorDetails_NewOperatorButton__page7
root.bind('<KeyPress>',fun1 )

def fun2():
    root.destroy()
    import AddBusDetails_NewBusButton_page8
root.bind('<KeyPress>',fun2)

def fun3():
    root.destroy()
    import NewRouteButton_AddBusDetails_page9
root.bind('<KeyPress>',fun3)

def fun4():
    root.destroy()
    import NewRunButton_AddBusRunningDetails_pg10
root.bind('<KeyPress>',fun4)

Button(root,text='New Operator',bg='light green',font='Calibri 11',command=fun1).grid(row=3,column=3)
Button(root,text='New Bus',bg='Tan',font='Calibri 11',command=fun2).grid(row=3,column=4)
Button(root,text='New Route',bg='teal',font='Calibri 11',command=fun3).grid(row=3,column=5)
Button(root,text='New Run',bg='Salmon',font='Calibri 11',command=fun4).grid(row=3,column=6)

