import Tkinter as tk
from tkinter import messagebox
import sqlite3


class AddToy:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x500')
        self.root.title("Add Toy")
        self.root.configure(bg='light blue')
        Label(self.root, text="Add Toy")
        Label(self.root, text="Toy Code", fg='dark blue', bg='light blue').pack()
        self.toy_code = Entry(self.root, width=30)  # The user will be able to enter in all the details about the toy
        self.toy_code.pack()
        Label(self.root, text="Toy Name", fg='dark blue', bg='light blue').pack()
        self.toy_name = Entry(self.root, width=30)  # The name of the toy
        self.toy_name.pack()
        Label(self.root, text="Toy Brand", fg='dark blue', bg='light blue').pack()
        self.toy_brand = Entry(self.root, width=30)  # The brand of the toy
        self.toy_brand.pack()
        Label(self.root, text="Toy Price", fg='dark blue', bg='light blue').pack()
        self.toy_price = Entry(self.root, width=30)  # The price of the toy
        self.toy_price.pack()
        Label(self.root, text="Toy Quantity", fg='dark blue', bg='light blue').pack()
        self.toy_quantity = Entry(self.root, width=30)  # The quantity of the toy
        self.toy_quantity.pack()

        # A label above each box saying what to enter
        Label(self.root, text="", bg='light blue').pack()
        Button(self.root, text="Add records to database", width=20, height=2, fg='dark blue',
               command=self.add_to_database).pack()
        Label(self.root, text="", bg='light blue').pack()
        # The command will go to call the function which will add the entry to the database
        Button(self.root, text="show records in database", width=20, height=2, fg='dark blue',
               command=self.display_results).pack()
        Label(self.root, text="", bg='light blue').pack()
        Button(self.root, text='Close', fg='dark blue', width=20, height=2, command=self.root.destroy).pack()
        # Once the data has been added to the database you can click show records and it will show the database
        self.centre_screen()

        connection = sqlite3.connect('Database.db')
        c = connection.cursor()

        #  Here I created a table which will check to see if once is already created
        c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Toys' ''')
        if c.fetchone()[0] != 1:
            try:
                c.execute('CREATE TABLE Toys(toy_code int UNIQUE, toy_name text UNIQUE, toy_brand text UNIQUE,'
                          'toy_price int UNIQUE, toy_quantity int UNIQUE)')
            except sqlite3.IntegrityError:
                messagebox.showerror('Error', 'Toy already exists.')
        # The if statement will only make a database if one is not already made otherwise it wil give an error
        else:
            try:
                c.execute('INSERT INTO Toys VALUES(:Code, :Name, :Brand, :Price, :Quantity)',
                          {'Code': self.toy_code.get(), 'Name': self.toy_name.get(), 'Brand': self.toy_brand.get(),
                           'Price': self.toy_price.get(), 'Quantity': self.toy_quantity.get()}).fetchall()
            except sqlite3.IntegrityError:
                messagebox.showerror('Failed!', 'Toy already exists.')
        connection.commit()  # We need to make sure we save the changes we made to the database
        c.close()  # We need to make sure we close it after
        #  If it has been made it will insert in the table category

    def add_to_database(self):
        connection = sqlite3.connect('Database.db')
        try:
            connection.execute("INSERT INTO Toys VALUES (:Code, :Name, :Brand, :Price, :Quantity)",
                               {'Code': self.toy_code.get(), 'Name': self.toy_name.get(), 'Brand': self.toy_brand.get(),
                                'Price': self.toy_price.get(), 'Quantity': self.toy_quantity.get()}).fetchall()
        except sqlite3.IntegrityError:
            messagebox.showwarning("Error!", "There is already a toy with these details.")
        #  I have used another if statement that wil check to see if the category code or name has already been entered
        connection.commit()
        connection.close()

    def display_results(self):
        connection = sqlite3.connect('Database.db')
        c = connection.cursor()
        c.execute("SELECT *,oid FROM Toys")  # "oid" stands for the original id
        results = c.fetchall()
        print(str(results))  # This will print the results from the database
        Label(self.root, text=" ID: --> Toy Code: --> Toy Name: --> Toy Brand: --> Toy Price: --> Toy Quantity: ")\
            .pack()
        showiest = ''
        for result in results:
            showiest += str(result[5]) + "\t" + str(result[0]) + "\t" + str(result[1]) + "\t" + str(result[2]) + "\t" \
                        + str(result[3]) + "\t" + str(result[4]) + "\n"
        #  this line here shows the layout of each row in the database
        Label(self.root, text=showiest).pack()

        connection.commit()
        c.close()

    def centre_screen(self):
        windowWidth = self.root.winfo_reqwidth()  # Gets widths of your monitor
        windowHeight = self.root.winfo_reqheight()  # Gets height of your monitor
        Width = int(self.root.winfo_screenwidth() / 2 - windowWidth / 2)  # Finds middle
        Height = int(self.root.winfo_screenheight() / 2 - windowHeight)  # Finds middle
        self.root.geometry('+{}+{}'.format(Width, Height))  # Centres GUI in the middle
