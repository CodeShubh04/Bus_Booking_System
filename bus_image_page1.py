from tkinter import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
bus=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=bus).grid(row=0,column=0,columnspan=10,padx=w//3)
Label(root,text='Online Bus Booking System',bg='light blue',fg='red',font='Arial 14 bold').grid(row=1,column=0,columnspan=10,pady=40)
Label(root,text='Name: Shubhanshi Verma',fg='blue',font='Arial 11 bold').grid(row=2,column=0,padx=600,pady=10)
Label(root,text='Er: 211B385',fg='blue',font='Arial 11 bold').grid(row=3,column=0,padx=600,pady=10)
Label(root,text='Mobile: 8269355790',fg='blue',font='Arial 11 bold').grid(row=4,column=0,padx=600,pady=10)
Label(root,text='Submitted To: Dr. Mahesh Kumar Sir',bg='light blue',fg='red',font='Arial 14 bold').grid(row=5,column=0,columnspan=10,pady=20)
Label(root,text='Project Based Learning',fg='red',font='Calibria 11 bold').grid(row=6,column=0)
def fun(self):
    root.destroy()
    import seatbook_check_book_page2
root.bind('<KeyPress>',fun )


root.mainloop()
