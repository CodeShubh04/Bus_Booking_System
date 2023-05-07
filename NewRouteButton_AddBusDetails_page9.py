from tkinter import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=10,padx=w//3)
Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='Arial 14 bold').grid(row=1,column=0,columnspan=15)
Label(root,text='Add Bus Route Details',bg='white',fg='green',font='Arial 11 bold').grid(row=2,column=0,columnspan=15,pady=20)
Label(root,text='Route Id').grid(row=3,column=1)
Entry(root).grid(row=3,column=2)
Label(root,text='Station Name').grid(row=3,column=3)
Entry(root).grid(row=3,column=4)
Label(root,text='Station Id').grid(row=3,column=5)
Entry(root).grid(row=3,column=6)
Button(root,text='Add Route',bg='light green',font='Calibri 11').grid(row=3,column=8)
Button(root,text='Delete Route',bg='Light green',fg='red',font='Calibri 11').grid(row=3,column=9)

def fun1():
    root.destroy()
    import seatbook_check_book_page2
root.bind('<KeyPress>',fun1)

home=PhotoImage(file='.\\home.png')
Button(root,image=home,command=fun1).grid(row=4,column=7,pady=20)
