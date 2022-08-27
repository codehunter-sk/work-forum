from tkinter import  *
import os
import file3 as f3

def register_user():

     username_info=username.get()
     password_info=password.get()

     file=open(username_info,"w")
     file.write(username_info+"\n")
     file.write(password_info)
     file.close()

     username_entry.delete(0, END)
     password_entry.delete(0,END)

     Label(screen1,text = "Registration success", fg="green",font = ("calibri",13)).pack()

def login_verify():
    username1=username_verify.get()
    password1=password_verify.get()

    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    
    if((username1 in list_of_files) and (username1!="leader")):
        file1 = open(username1,"r")
        verify=file1.read().splitlines()
        if(password1 in verify):
            screen.destroy()
            f3.main(username1,0)
        else:
            Label(screen2,text="**password incorrect",fg = "red",font=("calibri",13)).pack()
    else:
        Label(screen2,text="**Invalid User",fg = "red",font=("calibri",13)).pack()

def leader_login_verify():
    username3=username_verify3.get()
    password3=password_verify3.get()

    username_entry3.delete(0, END)
    password_entry3.delete(0, END)

    list_of_files = os.listdir()
    if(username3=='leader'):
        if((username3 in list_of_files)):
            file3 = open(username3,"r")
            verify=file3.read().splitlines()
            # verify=list(file3)
            if(password3 in verify):
                screen.destroy()
                f3.main('leader',1)
            else:
                Label(screen3,text="**password incorrect",fg = "red",font=("calibri",13)).pack()
        else:
            Label(screen3,text="**Invalid User",fg = "red",font=("calibri",13)).pack()
    else:
            Label(screen3,text="**Invalid User",fg = "red",font=("calibri",13)).pack()

        
def destroy3():
    screen3.destroy()
    
def destroy2():
    screen2.destroy()

def destroy1():
    screen1.destroy()
    
def register():
    global screen1
    global username
    global password
    global username_entry
    global password_entry
    screen1=Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("600x500")

    username = StringVar()
    password = StringVar()

    Label(screen1,text = "Please enter the details below").pack()
    Label(screen1,text=" ").pack()
    Label(screen1,text="Username *").pack()
    username_entry=Entry(screen1, textvariable= username)
    username_entry.pack()
    Label(screen1,text=" ").pack()
    Label(screen1,text="password *").pack()
    password_entry=Entry(screen1, textvariable= password,show='*')
    password_entry.pack()
    Label(screen1,text=" ").pack()
    Button(screen1,text = "Register",bg = "grey",width = "60",height="4",command= register_user).pack()
    Label(screen1,text="\n\n\n\n\n ").pack()
    Button(screen1,text = "Back",bg = "blue",fg="gold",width = "60",height="4",command=destroy1).pack()

def login():
    global screen2
    screen2=Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("600x500")
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify= StringVar()

    global username_entry1
    global password_entry1

    Label(screen2,text = "Please enter the details below to login").pack()
    Label(screen2,text=" ").pack()
    Label(screen2,text="Username *").pack()
    username_entry1=Entry(screen2, textvariable= username_verify)
    username_entry1.pack()
    Label(screen2,text=" ").pack()
    Label(screen2,text="password *").pack()
    password_entry1=Entry(screen2, textvariable= password_verify,show='*')
    password_entry1.pack()
    Label(screen2,text=" ").pack()
    Button(screen2,text = "Login",bg = "grey",width = "60",height="4",command= login_verify).pack()
    Label(screen2,text="\n\n\n\n\n ").pack()
    Button(screen2,text = "Back",bg = "blue",fg="gold",width = "60",height="4",command = destroy2).pack()

def leader_login():
        global screen3
        screen3=Toplevel(screen)
        screen3.title("Login")
        screen3.geometry("600x500")
        global username_verify3
        global password_verify3
        username_verify3 = StringVar()
        password_verify3= StringVar()

        global username_entry3
        global password_entry3

        Label(screen3,text = "Please enter the details below to login").pack()
        Label(screen3,text=" ").pack()
        Label(screen3,text="Username *").pack()
        username_entry3=Entry(screen3, textvariable= username_verify3)
        username_entry3.pack()
        Label(screen3,text=" ").pack()
        Label(screen3,text="password *").pack()
        password_entry3=Entry(screen3, textvariable= password_verify3,show='*')
        password_entry3.pack()
        Label(screen3,text=" ").pack()
        Button(screen3,text = "Login",bg = "grey",width = "60",height="4",command= leader_login_verify).pack()
        Label(screen3,text="\n\n\n\n\n ").pack()
        Button(screen3,text = "Back",bg = "blue",fg="gold",width = "60",height="4",command = destroy3).pack()
    
def main():
    global screen
    screen=Tk()
    screen.geometry("600x500")
    screen.title("Work Assigner")
    try:
        f=open('works.txt','r')
    except:
        f=open('works.txt','w')
    f.close()
    Label(text = "Work Assigner",bg = "blue",width ="600",height = "4",font = ("calibri",13)).pack()
    Label(text="\n\n\n\n\n ").pack()
    Button(text="Login",bg ="grey",width="60",height="4",command = login).pack()
    Label(text=" ").pack
    Button(text="Register",bg ="grey",width="60",height="4",command = register).pack()
    Label(text=" ").pack
    Button(text="Leader login",bg ="grey",width="60",height="4",command = leader_login).pack()

    screen.mainloop()
if __name__ == '__main__':
    main()