
from tkinter import *
# datas = []
# def MyButtonClicked(var):
#     inputValue=txtfld.get()
#     datas = scrap.scrapDetails(inputValue)
#     for i in datas:
#         print(i)
#         listbox.insert(i)

# window = Tk()

# window.title('Check Phone Details')
# window.geometry("500x500+10+20")\
    
# lbl=Label(window, text="Enter Phone Number", fg='black', font=("Helvetica", 12))
# lbl.place(x=60, y=50)

# txtfld=Entry(window, text="+91", bd=5)
# txtfld.place(x=80, y=80)

# btn=Button(window, text="Submit", fg='black')
# btn.place(x=80, y=120)
# btn.bind('<Button-1>', MyButtonClicked)

# list_items = StringVar(value=datas)
# listbox = Listbox(
#     window,
#     height=6,
#     listvariable=list_items
# )
# window.mainloop()


import scrap
import os


more = 'y'

while more in 'Yy':
    os.system('cls')

    print('Number Tracer')
    print('---------------')

    number = input('Enter the number: +91: ')
    more = scrap.scrapDetails(number)