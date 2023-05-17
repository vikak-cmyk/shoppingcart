import Tkinter as tk
import sqlite3


class DeleteToy:

    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x400')  # Will be the size of the page
        self.root.title("Delete Toy")  # Will be the title of the page
        self.root.configure(bg='light blue')

        Label(self.root, text='Delete Toy ID', fg='dark blue', bg='light blue').pack()
        self.toy_code = Entry(self.root)  # Here the user will enter in the oid of the row they want to delete
        self.toy_code.pack()

        Label(self.root, text="", bg='light blue').pack()
        Button(self.root, text='Submit', fg="dark blue", width='20', height='2',
               command=self.delete_from_database).pack()
        Label(self.root, text="", bg='light blue').pack()
        # Calls function that will delete that row from the database
        Button(self.root, text='View database', fg="dark blue", width='20', height='2',
               command=self.display_results).pack()
        Label(self.root, text="", bg='light blue').pack()
        # The user can then check the database to see if it has been deleted
        Button(self.root, text='Close', fg="dark blue", width='20', height='2', command=self.root.destroy).pack()
        self.centre_screen()

    def delete_from_database(self):
        conn = sqlite3.connect('Database.db')
        c = conn.cursor()
        c.execute("DELETE from Toys WHERE oid = " + self.toy_code.get())
        # This will get the oid that the customer has choose and will delete that row from the database
        conn.commit()
        conn.close()

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
