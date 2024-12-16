from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
import openpyxl, xlrd
from openpyxl import Workbook
import pathlib
import re


root = tk.Tk()
root.title("Data Entry")
root.geometry('1200x700+700+100')
root.resizable(False, False)
root.configure(bg="White")

# Icon
# icon_image = PhotoImage(file="icon.png")
# root.iconphoto(False, icon_image)

# Heading
Label(root, text="Please fill This form: ", font="arial", bg="#87CEEB", fg="#000000").place(x=20, y=20)

# Labels
Label(root, text='Transaction ID: ', font=23, bg="#87CEEB", fg="black").place(x=20, y=80)
Label(root, text='Customer ID:', font=23, bg="#87CEEB", fg="black").place(x=700, y=80)
Label(root, text='Salesperson ID:', font=23, bg="#87CEEB", fg="black").place(x=700, y=180)
Label(root, text='Date: ', font=23, bg="#87CEEB", fg="black").place(x=20, y=300)
Label(root, text='Month of Sale: ', font=23, bg="#87CEEB", fg="black").place(x=20, y=200)
Label(root, text='Item Set: ', font=23, bg="#87CEEB", fg="black").place(x=20, y=380)
Label(root, text='Product Category: ', font=23, bg="#87CEEB", fg="black").place(x=20, y=420)
Label(root, text='Quantity Sold: ', font=23, bg="#87CEEB", fg="black").place(x=20, y=460)
Label(root, text='Price Per Unit: ', font=23, bg="#87CEEB", fg="black").place(x=315, y=420)
Label(root, text='Total Sale Amount: ', font=23, bg="#87CEEB", fg="black").place(x=315, y=460)
Label(root, text='Payment Method: ', font=23, bg="#87CEEB", fg="black").place(x=600, y=380)
Label(root, text='Profit Margin: ', font=23, bg="#87CEEB", fg="black").place(x=600, y=420)
Label(root, text='Membership: ', font=23, bg="#87CEEB", fg="black").place(x=600, y=460)


# # Search field and button
# Button(root, text="Search", bg="#87CEEB", fg="black", width=10, command=search).place(x=900, y=120)
# Button(root, text="Refresh", bg="#87CEEB", fg="black", width=10, command=refresh).place(x=1000, y=120)


# # Submit and Clear buttons
# Button(root, text="Submit", bg="#87CEEB", fg="black", width=15, height=2, command=submit).place(x=350, y=550)
# Button(root, text="Clear", bg="#87CEEB", fg="black", width=15, height=2, command=clear).place(x=500, y=550)
Button(root, text="Exit", bg="#87CEEB", fg="black", width=15, height=2, command=lambda: root.destroy()).place(x=650, y=550)

root.mainloop()