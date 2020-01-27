from tkinter import *
from tkinter import messagebox
from database import DataBase

root = Tk()
instance = DataBase()
instance.checkDate()

def add():
    if text.get().strip() != '':
        instance.insert(text.get().strip())
        text.delete(0, END)
        getalltodo()
    else:
        messagebox.showwarning('Warning', 'You cannot leave text field empty')

def check():
    try:
        index = listbox.curselection()[0]
    except Exception:
        return None
    else:
        selecteditem = listbox.get(index)
        return int(selecteditem.split('  ,  ')[0])

def delete():
    text.delete(0,END)
    idnumber = check()
    if idnumber is not None:
        instance.delete(idnumber)
        getalltodo()


def update():
    idnumber = check()
    if idnumber is not None:
        if text.get() == '':
            messagebox.showwarning('Warning', 'You cannot leave text field empty')
        else:
            instance.update(idnumber, text.get())
            getalltodo()


def getalltodo():
    listbox.delete(0, END)
    todos = instance.fetchAll()
    for todo in todos:
        todo = list(todo)
        todo[0] = str(todo[0])
        listbox.insert(END, '  ,  '.join(todo))


def select(event):
    text.delete(0, END)
    index = listbox.curselection()[0]
    selecteditem = listbox.get(index)
    text.insert(0, selecteditem.split('  ,  ')[1])


root.title('Todo List')
root.geometry('475x500')
root.iconbitmap('todolist.ico')

title = Label(root, text='Todo List', font=('bold', 20), pady=10)
title.grid(row=0, column=0)

text = Entry(root, font=(10), width=50)
text.grid(row=1, column=0, padx=10, columnspan=3, ipady=8)

addbutton = Button(root, text='Add', width=15, bg='#32BF01', fg='white', command=add)
addbutton.grid(row=2, column=0, pady=10, ipady=4)

deletebutton = Button(root, text='Delete', width=15, bg='#FA1805', fg='white', command=delete)
deletebutton.grid(row=2, column=2, ipady=4)

updatebutton = Button(root, text='Update', width=15, bg='#05EBFA', fg='white', command=update)
updatebutton.grid(row=2, column=1, ipady=4)

listbox = Listbox(root, width=70, height=20, border=0)
listbox.grid(row=3, column=0, padx=5, pady=5, columnspan=3, rowspan=6)
listbox.bind('<<ListboxSelect>>', select)

scrollbary = Scrollbar(root)
scrollbary.grid(row=3, column=2)
listbox.configure(yscrollcommand=scrollbary.set)
scrollbary.configure(command=listbox.yview)

scrollbarx = Scrollbar(root)
scrollbarx.grid(row=7, column=2)
listbox.configure(xscrollcommand=scrollbarx.set)
scrollbarx.configure(command=listbox.xview)

getalltodo()

root.mainloop()
