"""
A program that stores book information:
Title, Author, Year, ISBN

User can:

View all data records,
Search an Entry,
Add entry,
Update entry,
Delete,
Close
"""
import backend 
from tkinter import *
from typing import Collection

def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)


def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(END,selected_tuple[1])

        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])

        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass

def search_command():
    list1.delete(0, END)
    for row in backend.search(title_text.get(), Author_text.get(), Year_text.get(), ISBN_text.get()):
        list1.insert(END, row)

def add_command():
    backend.insert(title_text.get(), Author_text.get(), Year_text.get(), ISBN_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), Author_text.get(), Year_text.get(), ISBN_text.get()))


def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0], title_text.get(), Author_text.get(), Year_text.get(), ISBN_text.get())


window = Tk()

window.wm_title("BookStore")

#Labels on window
l1 = Label(window, text='Title')
l1.grid(row=0, column=0)

l2 = Label(window, text='Author')
l2.grid(row=0, column=2)

l3 = Label(window, text='Year')
l3.grid(row=1, column=0)

l4 = Label(window, text='ISBN')
l4.grid(row=1, column=2)

#entry text
title_text=StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

Author_text=StringVar()
e2 = Entry(window, textvariable=Author_text)
e2.grid(row=0, column=3)

Year_text=StringVar()
e3 = Entry(window, textvariable=Year_text)
e3.grid(row=1, column=1)

ISBN_text=StringVar()
e4 = Entry(window, textvariable=ISBN_text)
e4.grid(row=1, column=3)

#list of itmes
list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

#scrollBar
sb1=Scrollbar(window)
sb1.grid(row=2, column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#event
list1.bind('<<ListboxSelect>>', get_selected_row)


#button for actions
b1=Button(window, text="View all", width=12, command = view_command)
b1.grid(row=2, column=3)

b2=Button(window, text="Search entry", width=12, command = search_command)
b2.grid(row=3, column=3)

b3=Button(window, text="Add entry", width=12, command = add_command)
b3.grid(row=4, column=3)

b4=Button(window, text="Update selected", width=12, command = update_command)
b4.grid(row=5, column=3)

b5=Button(window, text="Delete selected", width=12, command = delete_command)
b5.grid(row=6, column=3)

b6=Button(window, text="Close", width=12, command = window.destroy)
b6.grid(row=7, column=3)


window.mainloop()