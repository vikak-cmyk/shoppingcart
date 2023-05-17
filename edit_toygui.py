import Tkinter as tk
import sqlite3


class EditToy:

    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x500')
        self.root.title("Edit Toys")
        self.root.configure(bg='light blue')

        Label(self.root, text='Enter Original Toy ID', fg='dark blue', bg='light blue').pack()
        self.toy_code = Entry(self.root)  # Here they will enter in the ID that they want to change
        self.toy_code.pack()
        Label(self.root, text='Edit Toy Name', fg='dark blue', bg='light blue').pack()
        self.toy_name = Entry(self.root)  # They will need to enter the new details that they want to change
        self.toy_name.pack()
        Label(self.root, text='Edit Toy Brand', fg='dark blue', bg='light blue').pack()
        self.toy_brand = Entry(self.root)  # Any details they want to change they will need to do it in the entry box
        self.toy_brand.pack()
        Label(self.root, text='Edit Toy Price', fg='dark blue', bg='light blue').pack()
        self.toy_price = Entry(self.root)
        self.toy_price.pack()
        Label(self.root, text='Edit Toy Quantity', fg='dark blue', bg='light blue').pack()
        self.toy_quantity = Entry(self.root)
        self.toy_quantity.pack()

        Label(self.root, text="", bg='light blue').pack()
        Button(self.root, text='Submit', width='20', height='2', fg='dark blue', command=self.edit_toy).pack()
        Label(self.root, text="", bg='light blue').pack()
        # Once they have input the new details the user will click the submit button which will call the edit function
        Button(self.root, text='View database', width='20', height='2', fg='dark blue',
               command=self.display_results).pack()
        Label(self.root, text="", bg='light blue').pack()
        Button(self.root, text='Close', width='20', height='2', fg='dark blue', command=self.root.destroy).pack()
        self.centre_screen()

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

    def display_results(self):
        connection = sqlite3.connect('Database.db')
        c = connection.cursor()
        c.execute("SELECT *,oid FROM Toys")  # "oid" stands for the original id
        results = c.fetchall()
        print(str(results))  # This will print the results from the database
        Label(self.root, text=" ID: --> Toy Code: --> Toy Name: --> Toy Brand: --> Toy Price: --> Toy Quantity ").pack()
        # This is how it will show
        showiest = ''
        for result in results:
            showiest += str(result[5]) + "\t" + str(result[0]) + "\t" + str(result[1]) + "\t" + str(result[2]) + "\t" \
                        + str(result[3]) + "\t" + str(result[4]) + "\n"
            #  This line here shows the layout of each row in the database

        Label(self.root, text=showiest).pack()
        connection.commit()
        c.close()

    def centre_screen(self):
        windowWidth = self.root.winfo_reqwidth()  # Gets widths of your monitor
        windowHeight = self.root.winfo_reqheight()  # Gets height of your monitor
        Width = int(self.root.winfo_screenwidth() / 2 - windowWidth / 2)  # Finds middle
        Height = int(self.root.winfo_screenheight() / 2 - windowHeight)  # Finds middle
        self.root.geometry('+{}+{}'.format(Width, Height))  # Centres GUI in the middle