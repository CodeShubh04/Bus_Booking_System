from tkinter import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=10,padx=w//3)
Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='Arial 14 bold').grid(row=1,column=0,columnspan=10)

def fun1():
    root.destroy()
    import seat_booking_3
root.bind('<KeyPress>',fun1 )

def fun2():
    root.destroy()
    import checkyourbooking_page5
root.bind('<KeyPress>',fun2 )

def fun3():
    root.destroy()
    import AddBusDetails_NewBusButton_page8
root.bind('<KeyPress>',fun3 )

Button(root,text='Seat Booking',bg='Light green',font='Arial 14 bold',command=fun1).grid(row=2,column=4,pady=50)
Button(root,text='Check Booked Seat',bg='Light green',font='Arial 14 bold',command=fun2).grid(row=2,column=5,pady=50)
Button(root,text='Add Bus Details',bg='Light green',font='Arial 14 bold',command=fun3).grid(row=2,column=6,pady=50)
Label(root,text='For Admin Only',fg='red',font='Arial 11 bold').grid(row=3,column=6)

root.mainloop()
