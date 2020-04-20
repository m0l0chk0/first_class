import random
from tkinter import *
from tkinter import messagebox
color_fg = "White"
bg = "#597da3"

def author():
    messagebox.showinfo("О программе","Авторы: Никанкин Антон \nВерсия: 1.0")
def check(ans):
    Ans.grid_remove()
    Next.grid(row=3,column=1,columnspan=5 )

    if int(en.get())==ans:
        label1["text"]='Правильно'
    else:
        label1["text"]='Неправильно'


def task():
    main_menu.entryconfig(2,state=NORMAL)
    label1["text"]=""
    en.delete(0, END)
    z = random.choice(["+","-"])
    Next.grid_remove()
    btn1.grid_remove()
    a = random.randint(1,20)
    if z=="+":
        b = random.randint(1,21-a)
    else:
        b = random.randint(1,a)
    c=eval(str(a)+z+str(b))
    label["text"]=text=str(a)+" "+z+" "+str(b)+" = "
    label.grid(row=1,column=3)
    en.grid(row=1,column=4)
    label1.grid(row=2,column=1,columnspan=5)
    Ans.grid(row=3,column=1,columnspan=5 )
    checkin = lambda x=c:check(x)
    Ans["command"]=checkin
    
def main():
    main_menu.entryconfig(2,state=DISABLED)
    label.grid_remove()
    en.grid_remove()
    Ans.grid_remove()
    Next.grid_remove()
    label1.grid_remove()
    btn1.grid(row=0,column=0)



    
    
    


win = Tk()
win.title("Примеры для 1 класса")
main_menu = Menu()
main_menu.add_command(label="О программе",command = author)
main_menu.add_command(label="Вернуться",command=main,state=DISABLED)
win.config(menu=main_menu)

btn1 = Button(text="Примеры",padx="120",pady="20",width=7,background=bg, fg=color_fg,command = task)
btn1.grid(row=0,column=0)
label = Label()
Ans = Button(text="Ответ",padx="120",pady="5",width=7,background=bg, fg=color_fg)
en = Entry(width=2)
Next = Button(text="Дальше",padx="120",pady="5",command = task,width=7,background=bg, fg=color_fg)

label1 = Label(text="",width=10)


win.mainloop()

