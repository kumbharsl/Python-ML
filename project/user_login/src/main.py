from tkinter  import *
from tkinter import messagebox

root =Tk()
root.title('Login')
root.geometry( '1000x500+100+50' )
root.configure(bg= 'white')
# root.resizable(False, False)

def signup():
    screen=Toplevel(root)
    screen.title("App")
    screen.geometry('1000x500+100+50' )
    screen.config(bg='white')
    
    def signup():
        username=user.get()
        password=code.get()
        conform_password=code1.get()
        
        if password == conform_password:
            try:
                file=open('datasheet.txt','r+')
                d=file.read()
                r.ast.literal_eval(d)
                
                dict2= {username:password}
                r.update(dict2)
                file.turncate(0)
                file.close()
                
                file=open('datasheet.txt','w')
                w=file.write(str(r))
                
                messagebox.showinfo('Signup','Sucessfully sign up')
                
            except:
                file = open('datasheet.txt','w')
                pp=str({'Username':'password'})
                file.write(pp)
                file.close()
        
        else:
            messagebox.showerror( "Invalid", "Password does not match"  )  
    
    img  = PhotoImage(file='login1.png')
    Label(screen, image=img,bg='white').place(x=50,y=100)
    
    frame=Frame(screen,width=500,height=450,bg="white")
    frame.place(x=550, y=70)

    heading = Label(frame,text= "SIGN UP",font=("Helvetica",20,"bold"),fg="#57a1f8" , bg="white")
    heading.place(x=100,y=5)
    
    #-------------------------------------------------------------------------------------------------------------
    #creat user name input
    def on_enter(e):
        user.delete(0,'end')
    
    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')
            
    user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,"Username")
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)
    Frame(frame,width=295,height=2,bg="black").place(x=25,y=110)
    
    #-------------------------------------------------------------------------------------------------------------
    #create password input
    def on_enter(e):
        code.delete(0,'end')
    
    def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0,'Password')
    code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    code.place(x=30,y=150)
    code.insert(0,"Password")
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)
    Frame(frame,width=295,height=2,bg="black").place(x=25,y=180)
    #-------------------------------------------------------------------------------------------------------------
    #create confirm password input
    def on_enter(e):
        code1.delete(0,'end')
    
    def on_leave(e):
        name=code1.get()
        if name=='':
            code1.insert(0,'Password  Confirm')
    code1 = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
    code1.place(x=30,y=220)
    code1.insert(0,"Password Confirm")
    code1.bind('<FocusIn>',on_enter)
    code1.bind('<FocusOut>',on_leave)
    Frame(frame,width=295,height=2,bg="black").place(x=25,y=250)
    
    #------------------------------------------------------------------------------------------------------------------
    Button(frame,width=39,pady=7,text='Sign up', bg='#57a1f8',fg='white',border=0).place(x=35,y=274)
    label = Label(frame,text="I have an account?",fg="black",bg='white',font=('Microsoft YaHei UI Light',9))
    label.place(x=75,y=320)
    
    signin = Button(frame,width=6,text='Sign in', border=0, bg= 'white',cursor='hand2',fg='#57a1f8',command=signup)
    signin.place(x=190,y=320)
    
    screen.mainloop()
#-----------------------------------------------------------------------------------------------------------------
def signin():
    username=user.get()
    password=code.get()
    
    if username=='admin' and password=='1234':
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry('1000x500+100+50' )
        screen.config(bg='white')
        
        # Label(screen,text='Hello Everyone!',bg='#fff',font=('Calibri',50,'bold')).pack(expand=True)
        def demo():
            pass
        my_menu = Menu(screen)
        screen.config(menu=my_menu)

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

                
        screen.mainloop()
    
    elif username != 'admin' and password !='1234':
        messagebox.showerror('Invalid','Invalid username and password')
        
    elif password != '1234':
        messagebox.showerror('Invalid','Invalid password')
    
    elif username != 'admin':
        messagebox.showerror('Invalid','Invalid username')

img  = PhotoImage(file='login.png')
Label(root, image=img,bg='white').place(x=50,y=90)

frame=Frame(root,width=500,height=350,bg="white")
frame.place(x=550, y=70)

heading = Label(frame,text= "SIGN IN",font=("Helvetica",20,"bold"),fg="#57a1f8" , bg="white")
heading.place(x=100,y=5)

#-------------------------------------------------------------------------------------------------------------
def on_enter(e):
    user.delete(0,'end')
    
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,"Username")
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=110)
#-------------------------------------------------------------------------------------------------------------
def on_enter(e):
    code.delete(0,'end')
    
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')
code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,"Password")
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=180)

#-------------------------------------------------------------------------------------------------------------
Button(frame,width=39,pady=7,text='Sign in', bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
label = Label(frame,text="Don't have an account?",fg="black",bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

sign_up = Button(frame,width=6,text='Sign up', border=0, bg= 'white',cursor='hand2',fg='#57a1f8',command=signup)
sign_up.place(x=215,y=270)


root.mainloop()