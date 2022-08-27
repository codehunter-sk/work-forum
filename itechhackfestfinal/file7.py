from tkinter import *
from tkinter.tix import *
from tkinter import messagebox as msgbox
from tkinter import ttk
from PIL import Image, ImageTk
import file4
import file3
import file8
def registeredfunc(a):
    root.destroy()
    file6.main()
def rootw():
    global root
    root = Tk()
    root.title('')
    root.geometry('600x500')
    root.resizable(0,0)
def main(user):
    global frame1 , gobutton_img ,  registered , registered_img 
    rootw()



    frame1 = Frame(root, height = 500, width = 600, bg = '#f0f0f0')
    frame1.grid(row = 0, column = 0)

    ato = file4.main(user,0)

    done=['not ','']

    the_vars = []
    user_selected = []

    def get_user_selected():
        nonlocal user_selected
        
       
        user_selected = []
        for i in range(len(the_vars)):
            if (globals()[the_vars[i][0]]).get() :
                user_selected.append(ato[i])
        print(user_selected)
        root.destroy()
        file8.main(user,user_selected)
        file3.main(user,0)




    def _on_mousewheel(event):
        try:
            canvas_c.yview_scroll(int(-1*(event.delta/120)), "units")
        except Exception :
            pass

    def configfunc(event):
        canvas_c.config(scrollregion = canvas_c.bbox('all'))

    canvas_c = Canvas(frame1)
    frame1a = Frame(canvas_c,bd = 5)
    myscrollbar = Scrollbar(frame1,orient = VERTICAL,command = canvas_c.yview)
    canvas_c.configure(yscrollcommand = myscrollbar.set)

    canvas_c.grid(row = 0,column = 0)
    myscrollbar.grid(row = 0,column = 1,sticky = 'ns')
    canvas_c.create_window((0,0),window = frame1a,anchor = 'nw')

    frame1a.bind('<Configure>',configfunc)

    canvas_c.bind_all("<MouseWheel>", _on_mousewheel)

    
    for numb in range(len(ato)):
        globals()['CityVar'+str(numb)] = IntVar()
        globals()['City'+str(numb+1)] = ttk.Checkbutton(frame1a,text = ato[numb],\
            variable = globals()['CityVar'+str(numb)],onvalue = 1 ,offvalue = 0)
        (globals()['City'+str(numb+1)]).grid(row = numb + 1,sticky = 'w')

        the_vars.append(['CityVar'+str(numb),'City'+str(numb+1)])

    donebtn_cities = ttk.Button(frame1,text = 'CONFIRM', width = 10,command = get_user_selected)
    donebtn_cities.grid(row = 0,column = 2,sticky = 's')

    root.mainloop()

if __name__ == '__main__':
    main('suri')
