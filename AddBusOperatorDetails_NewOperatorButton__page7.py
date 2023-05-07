from tkinter import *
from tkinter.messagebox import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=10,padx=w//3)
Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='Arial 14 bold').grid(row=1,column=0,columnspan=15)
Label(root,text='Add Bus Operator Details',bg='white',fg='green',font='Arial 11 bold').grid(row=2,column=0,columnspan=15,pady=20)
Label(root,text='Operator Id').grid(row=3,column=0)
Entry(root).grid(row=3,column=1)
Label(root,text='Name').grid(row=3,column=2)
Entry(root).grid(row=3,column=3)
Label(root,text='Address').grid(row=3,column=4)
Entry(root).grid(row=3,column=5)
Label(root,text='Phone').grid(row=3,column=6)
Entry(root).grid(row=3,column=7)
Label(root,text='Email').grid(row=3,column=8)
Entry(root).grid(row=3,column=9)

def add_button():
    showinfo('operator entry','operator record added')
def edit_button():
    showinfo('operator entry update','operator record updated successfully')

Button(root,text='Add',command=add_button,bg='light green',font='Calibri 11').grid(row=3,column=10,padx=5)
Button(root,text='Edit',command=edit_button,bg='Light green',font='Calibri 11').grid(row=3,column=11,padx=5)

def fun1():
    root.destroy()
    import seatbook_check_book_page2
root.bind('<KeyPress>',fun1)

home=PhotoImage(file='.\\home.png')
Button(root,image=home,command=fun1).grid(row=4,column=8)
