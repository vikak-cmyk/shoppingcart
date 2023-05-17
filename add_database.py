import sqlite3
import self as self
from tkinter import messagebox

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

def delete_from_database(self):
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    c.execute("DELETE from Toys WHERE oid = " + self.toy_code.get())
    # This will get the oid that the customer has choose and will delete that row from the database
    conn.commit()
    conn.close()

    def edit_toy(self):
        conn = sqlite3.connect('Database.db')
        c = conn.cursor()
        c.execute('UPDATE Toys SET toy_name = :Name, toy_brand = :Brand, toy_price = :Price, toy_quantity = :Quantity '
                  'WHERE oid= :oid',
                  {'Name': self.toy_name.get(), 'Quantity': self.toy_quantity.get(), 'Brand': self.toy_brand.get(),
                   'Price': self.toy_price.get(), 'oid': self.toy_code.get()})
        # It will take the entry that the user inputted from line 13 to 22
        # This will get the oid from the old details and update it with a new details that the user entered
        conn.commit()
        c.close()