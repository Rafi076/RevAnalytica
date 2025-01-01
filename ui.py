from tkinter import *
from logic import search_transaction_details, refresh_transaction_fields, submit_transaction_details, get_frequent_item

def create_ui():
    root = Tk()
    root.title("Sales Transaction Form")
    root.geometry("1200x700")
    root.configure(bg="#87CEEB")

    # Labels and Entry fields
    Label(root, text="Please fill This form: ", font=("Arial", 16, "bold"), bg="#87CEEB", fg="#000000").place(x=550, y=20)

    # Labels
    Label(root, text='Customer ID: ', font=("Arial", 12), bg="#87CEEB", fg="black").place(x=20, y=80)
    Label(root, text='Transaction ID:', font=("Arial", 12), bg="#87CEEB", fg="black").place(x=700, y=80)
    Label(root, text='Salesperson:', font=("Arial", 12), bg="#87CEEB", fg="black").place(x=20, y=120)
    Label(root, text='Date: ', font=("Arial", 12), bg="#87CEEB", fg="black").place(x=20, y=300)
    Label(root, text='Month of Sale: ', font=("Arial", 12), bg="#87CEEB", fg="black").place(x=20, y=200)
    Label(root, text='Item Set: ', font=("Arial", 12), bg="#87CEEB", fg="black").place(x=20, y=380)
    Label(root, text='Product Category: ', font=("Arial", 12), bg="#87CEEB", fg="black").place(x=20, y=420)
    Label(root, text='Quantity Sold: ', font=("Arial", 12), bg="#87CEEB", fg="black").place(x=20, y=460)
    Label(root, text='Price Per Unit: ', font=("Arial", 12), bg="#87CEEB", fg="black").place(x=415, y=420)
    Label(root, text='Total Sale: ', font=("Arial", 12), bg="#87CEEB", fg="black").place(x=415, y=460)
    Label(root, text='Payment Method: ', font=("Arial", 12), bg="#87CEEB", fg="black").place(x=800, y=380)
    Label(root, text='Profit Margin: ', font=("Arial", 12), bg="#87CEEB", fg="black").place(x=800, y=420)
    Label(root, text='Membership: ', font=("Arial", 12), bg="#87CEEB", fg="black").place(x=800, y=460)
    Label(root, text="Most Frequent Item Set: ", font=("Arial", 12), bg="#87CEEB", fg="black").place(x=20, y=500)

    # Entry fields
    global customerIDEntry, transactionIDEntry, salespersonIDEntry, dateEntry, monthEntry
    global itemSetEntry, productCategoryEntry, quantitySoldEntry, pricePerUnitEntry
    global totalSaleAmountEntry, paymentMethodEntry, profitMarginEntry, membershipEntry
    global frequentItemEntry

    customerIDEntry = Entry(root, width=20, bd=2, font=12)
    transactionIDEntry = Entry(root, width=20, bd=2, font=12)
    salespersonIDEntry = Entry(root, width=20, bd=2, font=12)
    dateEntry = Entry(root, width=20, bd=2, font=12)
    monthEntry = Entry(root, width=20, bd=2, font=12)
    itemSetEntry = Entry(root, width=20, bd=2, font=12)
    productCategoryEntry = Entry(root, width=20, bd=2, font=12)
    quantitySoldEntry = Entry(root, width=20, bd=2, font=12)
    pricePerUnitEntry = Entry(root, width=20, bd=2, font=12)
    totalSaleAmountEntry = Entry(root, width=20, bd=2, font=12)
    paymentMethodEntry = Entry(root, width=20, bd=2, font=12)
    profitMarginEntry = Entry(root, width=20, bd=2, font=12)
    membershipEntry = Entry(root, width=20, bd=2, font=12)
    frequentItemEntry = Entry(root, width=30, bd=2, font=12)

    # Positioning entry fields
    entries = [
        (customerIDEntry, 150, 80), (transactionIDEntry, 880, 80), (salespersonIDEntry, 150, 120),
        (dateEntry, 150, 300), (monthEntry, 150, 200), (itemSetEntry, 150, 380),
        (productCategoryEntry, 150, 420), (quantitySoldEntry, 150, 460), (pricePerUnitEntry, 550, 420),
        (totalSaleAmountEntry, 550, 460), (paymentMethodEntry, 970, 380), (profitMarginEntry, 970, 420),
        (membershipEntry, 970, 460), (frequentItemEntry, 250, 500)
    ]
    for entry, x, y in entries:
        entry.place(x=x, y=y)

    # Buttons
    Button(
        root,
        text="Search",
        font=("Arial", 10),
        command=lambda: search_transaction_details(
            transactionIDEntry, customerIDEntry, salespersonIDEntry, dateEntry, monthEntry, itemSetEntry,
            productCategoryEntry, quantitySoldEntry, pricePerUnitEntry, totalSaleAmountEntry,
            paymentMethodEntry, profitMarginEntry, membershipEntry
        ),
    ).place(x=900, y=110)

    Button(
        root,
        text="Refresh",
        font=("Arial", 10),
        command=lambda: refresh_transaction_fields([ 
            transactionIDEntry, customerIDEntry, salespersonIDEntry, dateEntry, monthEntry,
            itemSetEntry, productCategoryEntry, quantitySoldEntry, pricePerUnitEntry,
            totalSaleAmountEntry, paymentMethodEntry, profitMarginEntry, membershipEntry
        ]),
    ).place(x=980, y=110)

    Button(root, text="Submit", font=("Arial", 14), command=lambda: submit_transaction_details([ 
        transactionIDEntry, customerIDEntry, salespersonIDEntry, dateEntry, monthEntry,
        itemSetEntry, productCategoryEntry, quantitySoldEntry, pricePerUnitEntry,
        totalSaleAmountEntry, paymentMethodEntry, profitMarginEntry, membershipEntry
    ])).place(x=450, y=600)

    Button(root, text="Exit", font=("Arial", 14), command=root.destroy).place(x=550, y=600)

    Button(
        root,
        text="Frequent",
        font=("Arial", 10),
        command=lambda: get_frequent_item(frequentItemEntry),
    ).place(x=550, y=500)

    root.mainloop()
