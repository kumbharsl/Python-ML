from tkinter import  *
from tkinter import ttk, filedialog
from tkinter import  messagebox
import csv
import os

win = Tk()
win.title("Billing Software")
win.iconbitmap("tk_inter\icon.ico")
win.maxsize(1360,768)
win.minsize(450,290)

# def func():
#     var.get()
      
# #label 
# label = Label(win, text="Billing Software",bg="white",fg="black",width=120,font=('arial', 15))
# # label.grid(row=3, column=3)
# label.place(x=10,y=10)

# #Entry 
# ent = Entry(win,bd=5)
# ent.place(x=10,y=80)

# #ComboBox
# com = ttk.Combobox(win,width=27)
# com['state'] = 'readonly'
# com['values'] = ('Select Product','Product A','Product B')
# com.current(0)
# com.place(x=10,y=160)

# # #checkbutton
# # Checkbutton1 = IntVar()
# # Checkbutton2 = IntVar()

# # select = Checkbutton(win,text="Male",variable=Checkbutton,onvalue=1,offvalue=0)
# # select.pack()
# # male = Checkbutton(win,text="Female", variable=Checkbutton)
# # select.pack()

# #button
# btn = Button(win,text="print",bg="red",bd=5)
# btn.place(x=1,y=120)

# def func():
#     print(var.get())

# var = IntVar()

# radio = Radiobutton(win,text="Male  ",value=0,variable=var).pack()
# radio = Radiobutton(win,text="Female",value=1,variable=var).pack()

# btn = Button(win,text= "Submit",command=func).pack()
# #End line of code

# topheader = Frame(win)
# topheader.pack()

# bottom = Frame(win)
# bottom.pack()

# label = Label(topheader,text="This is header")
# label.pack()

# label = Label(topheader,text="This is bottom")
# label.pack()

# def func():
#     if var.get()=="":
#         messagebox.showerror("Error","Please enter your name!")
# var = StringVar()
# ent = Entry(win,textvariable=var)
# ent.pack()

# btn = Button(win,text="Click me", command=func)
# btn.pack()

# def func():
#     lst.delete(ANCHOR)
# lst = Listbox(win,width=27)
# lst.insert(END,"Apple")
# lst.insert(END,"Apple")
# lst.insert(END,"Apple")
# lst.insert(END,"Apple")
# lst.insert(END,"Apple")

# items = ["Apple","Banana","etc"]

# for i in items:
#     lst.insert(END,i)

# btn  = Button(win, text='Delete', command=func).pack()
# lst.pack()

# canvas = Canvas(win)

# cord = 10,50,270,210
# canvas.create_arc(cord, start=0,extent=180, fill="blue")

# canvas.pack()
# def bar():
#     import time
#     progress['value']=20
#     progress.update_idletasks()
#     time.sleep(1)
    
#     progress['value']=40
#     progress.update_idletasks()
#     time.sleep(1)
    
#     progress['value']=60
#     progress.update_idletasks()
#     time.sleep(1)
    
#     progress['value']=80
#     progress.update_idletasks()
#     time.sleep(1)
    
#     progress['value']=100
#     progress.update_idletasks()
#     time.sleep(1)
    
# progress = ttk.Progressbar(win,orient=HORIZONTAL,length=100,mode='determinate')
# progress.pack()

# btn = Button(win,text="Start",command= bar).pack()

# scrollbar = Scrollbar(win)
# scrollbar.pack(side=RIGHT,fill=Y)

# mylist = Listbox(win)
# # mylist.insert(END,"Hello")
# # mylist.insert(END,"World!")
# for i in range(1000):
#     mylist.insert(END,i)
# mylist.pack(side=LEFT,fill=Y)
# scrollbar.config(command=mylist.yview)

def demo():
    pass
my_menu = Menu(win)
win.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_cascade(label="New",command=demo)
file_menu.add_separator()
file_menu.add_cascade(label="Open",command=demo)
file_menu.add_separator()
file_menu.add_cascade(label="Save",command=demo)
file_menu.add_separator()
file_menu.add_cascade(label="Save As",command=demo)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_cascade(label="Copy", command=demo)
edit_menu.add_separator()
edit_menu.add_cascade(label="Cut", command=demo)


format_menu = Menu(my_menu)
my_menu.add_cascade(label="Format", menu=format_menu)
format_menu.add_cascade(label="Size", command=demo)
format_menu.add_separator()
format_menu.add_cascade(label="Color", command=demo)

view_menu = Menu(my_menu)
my_menu.add_cascade(label="View", menu=view_menu)

help_menu = Menu(my_menu)
my_menu.add_cascade(label="Help", menu=help_menu)


win.mainloop()