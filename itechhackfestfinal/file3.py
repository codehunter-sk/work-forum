from tkinter import *
from tkinter.tix import *
from tkinter import messagebox as msgbox
from PIL import Image, ImageTk
import file4
import file6
import file7
import file9
def registeredfunc(a):
    root.destroy()
    file6.main()
def rootw():
    global root
    root = Tk()
    root.title('')
    root.geometry('600x500')
    root.resizable(0,0)
def lastbtn(a):
    if a:
        root.destroy()
        file9.main()
    else:
        root.destroy()
        file7.main(user1)
def main(user,leader):
    global frame1 , gobutton_img ,  registered , registered_img , user1
    rootw()
    user1=user



    frame1 = Frame(root, height = 500, width = 600, bg = 'black')
    frame1.grid(row = 0, column = 0)

    gobutton_img = ImageTk.PhotoImage(Image.open('.\\images\\loginblue.png'))


    bgimagload = Image.open('.\\images\\bg2.png')
    bgimag = ImageTk.PhotoImage(bgimagload)
    bgimaglabel = Label(frame1, image = bgimag,borderwidth=0).place(x = 0,y = 0)

    textlabel=Label(frame1, text = 'WORK FORUM', font=("calibri",28,"bold"), bg="white", fg="black")
    textlabel.place(x = 192, y = 20)

    registered_img = ImageTk.PhotoImage(Image.open('.\\images\\exitblue.png'))
    registered = Button(frame1, image = registered_img , cursor = 'hand2', bd = 0, command = lambda : registeredfunc(0))
    registered.place(x = 449, y = 82)

    
    ato = file4.main(user,leader)

    done=['not ','']

    if leader:
        textlabel=Label(frame1, text = f'Work assigned by you ({user})', font=("calibri",11,"bold"), bg="white", fg="black")
        textlabel.place(x = 200, y = 130)
        scwin_ato = ScrolledWindow(frame1, width = 235, height = 280)
        scwin_ato.place(x = 200, y = 160)
        wind_ato = scwin_ato.window

        for i in ato:
            w_ato = Message(wind_ato, text = i[0]+'-to-'+i[1]+'-'+done[int(i[2])]+'done', width = 236)
            w_ato.pack()

    else:

        textlabel=Label(frame1, text = f'Work assigned to you ({user})', font=("calibri",11,"bold"), bg="white", fg="black")
        textlabel.place(x = 200, y = 130)
        scwin_ato = ScrolledWindow(frame1, width = 235, height = 280)
        scwin_ato.place(x = 200, y = 160)
        wind_ato = scwin_ato.window

        for i in ato:
            w_ato = Message(wind_ato, text = i[0]+'-'+done[int(i[1])]+'done', width = 236)
            w_ato.pack()

    registered = Button(frame1, text = ['marks as done','assign work'][leader] , cursor = 'hand2', bd = 0, command = lambda : lastbtn(leader))
    registered.place(x = 209, y = 442)


    root.mainloop()

if __name__ == '__main__':
    main('suri',0)
