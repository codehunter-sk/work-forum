from tkinter import  *
import os
import file3

def loginid_verify():
    username1=username_verify.get()

    username_entry1.delete(0, END)

    list_of_files = os.listdir()
    
    if(username1 in list_of_files):
        f=open('works.txt','a')
        f.write(work.get()+','+username1+',0.')
        f.close()
        screen2.destroy()
        file3.main('leader',1)
    else:
        Label(screen2,text="**Invalid User",fg = "red",font=("calibri",13)).pack()
def destroy3():
    screen2.destroy()
    file3.main('leader',1)

def main():
    global screen2, work
    screen2=Tk()
    screen2.title("Work assigner")
    screen2.geometry("600x500")
    global username_verify
    username_verify = StringVar()
    work= StringVar()

    global username_entry1

    Label(screen2,text = "Please enter the details below to assign work").pack()
    Label(screen2,text=" ").pack()
    Label(screen2,text="Worker username *").pack()
    username_entry1=Entry(screen2, textvariable= username_verify)
    username_entry1.pack()
    Label(screen2,text="work *").pack()
    password_entry1=Entry(screen2, textvariable=work )
    password_entry1.pack()
    Label(screen2,text=" ").pack()
    Button(screen2,text = "Assign",bg = "grey",width = "60",height="4",command= loginid_verify).pack()
    Button(screen2,text = "Back",bg = "blue",fg="gold",width = "60",height="4",command = destroy3).pack()

    screen2.mainloop()


if __name__ == '__main__':
    main()
