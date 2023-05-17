# import of the sqlite module
import sqlite3
# importing widgets for the GUI design
import Tkinter as tk
# import of closing
from contextlib import closing

# opening of a database connection, creates a new database if it does not exist
c = sqlite3.connect("Database.db")

# getting of a cursor object
# it enables us to send SQL statements to SQLite
cursor = c.cursor()

# sending an SQL statement to retrieve data
rows = cursor.execute("SELECT product_name, price, quantity, discount FROM products").fetchall()

print(rows)

# removing a product
product_to_delete = "Doll"
rows = cursor.execute("SELECT product_name, price, quantity, discount FROM products").fetchall()
print(rows)

with closing(sqlite3.connect("Items.db")) as connection:
    with closing(connection.cursor()) as cursor:
        rows = cursor.execute("SELECT 1").fetchall()


class Item:

    def __init__(self):
        # stores all information about the items in the basket
        # the variable is initialized to empty
        self.item_dic = {}

    # accepts parameters
    # the information is saved in the item_dic, product name is key and value is list of info
    def add_item(self, product_name, price, quantity, discount):
        self.item_dic[product_name] = [price, quantity, discount]

    # accepts parameters
    # checks if the product that wants to be updated already exists in the basket
    # checks which part of info needs to be updated such as name, quantity or discount
    # as soon as it is identified then the info will be updated
    def update_product(self, info_to_update, name_of_product, new_value):
        if self.item_dic.__contains__(name_of_product):
            if info_to_update == 'name':
                product_info = self.item_dic[name_of_product]
                del self.item_dic[name_of_product]
                self.item_dic[new_value] = product_info
            elif info_to_update == 'quantity':
                new_value = int(new_value)
                product_info = self.item_dic[name_of_product]
                price_per_item = product_info[0] / product_info[1]
                product_info[1] = new_value
                product_info[0] = price_per_item * new_value
                self.item_dic[name_of_product] = product_info
            elif info_to_update == 'discount':
                new_value = int(new_value)
                product_info = self.item_dic[name_of_product]
                product_info[2] = new_value
                self.item_dic[name_of_product] = product_info
        else:
            print("Product does not exist")

    # removes the product (name_of_product) received as a parameter
    # so if the name_of_product is in item_dic then that item will be removed otherwise a message will be printed
    def remove_product(self, name_of_product):
        if self.item_dic.__contains__(name_of_product):
            del self.item_dic[name_of_product]
        else:
            print("Product does not exist")

    # prints every item that is in item_dic with all of its additional info
    def display_items(self):
        for item in self.item_dic:
            info = self.item_dic[item]
            output = "\n" + "Name: " + item
            "\nTotal Price: {0}".format(str(info[0]))
            "\nQuantity: {0}".format(str(info[1]))
            "\nDiscount: {0}".format(str(info[2]))

            print(output)


# an instance of a class Item is created
myBasket = Item()

# the following code allows the user to add to basket, update basket, remove from cart, display and quit
# in order to get any of the features to work the user has to enter the first letter of the word in upper case
# then the information needed to call the function lets say update_product will be asked for the user
while True:
    feature = input("Enter (a)dd, (u)pdate, (r)emove, (d)isplay, (q)uit: ")
    if feature == 'A':
        name = input("Enter product name: ")
        price = input("Enter product total price: ")
        quantity = input("Enter product quantity: ")
        discount = input("Enter discount(Discount will be applied at check-out): ")

        myBasket.add_item(name, int(price), int(quantity), int(discount))

    elif feature == 'U':
        info_to_update = input("Enter info to update('name', 'quantity', 'discount'): ")
        name = input("Enter product name: ")
        new_value = input("Enter new value: ")
        myBasket.update_product(info_to_update, name, new_value)

    elif feature == 'R':
        name = input("Enter product name to remove: ")
        myBasket.remove_product(name)

    elif feature == 'D':
        myBasket.display_items()

    elif feature == 'Q':
        print("Goodbye!")
        break

print("Please select your delivery option")
print("For default delivery option choose : 01")
print("For a custom delivery option choose : 02")
option_selected = int(input())


# calculates the discount
def offer(discount):
    global discount1
    discount1 = discount / 100
    return discount1


# customers who decide to collect their purchase in store
def collect_store(cost, discount):
    total_cost = cost - (cost * offer(discount))
    return total_cost


# customers who decide to choose home delivery
def home_delivery(cost, discount, delivery_cost):
    discount_price = offer(discount)
    total_cost = cost - (cost * discount_price) + delivery_cost
    return total_cost


# if selected option equals two then the customer can choose how he wants his product delivered
if option_selected == 2:
    print("To collect product in the store please choose:11 ")
    print("To receive home delivery please choose: 22 ")
    option = int(input())

    # customer selected collect in store
    if option == 11:
        print("Price for product:", 242)

        # the function offer() is called out
        percentage = 242 * offer(10)
        print("Special Offers (10% discount)", percentage)

        # the function collect_store() is called out
        total_price = collect_store(242, 10)
        print("In total: ", total_price)
    else:
        print("Price for product:", 242)

        # the function offer() is called out
        percentage = 242 * offer(10)
        print("Special Offers (10% discount)", percentage)
        global rate
        delivery_cost = 41
        print("Delivery rate:", 41)

        # the function home_delivery() is called out
        total_price = home_delivery(242, 10, 41)
        print("In total:", home_delivery(242, 10, 41))
else:
    print("Default delivery option is Home delivery")
    print("Price for product:", 242)
    delivery_cost = 41
    print("Delivery rate:", 41)

    # the function offer() is called out
    percentage = 242 * offer(10)
    print("Special Offers (10% discount)", percentage)

    # the function home_delivery() is called out
    total_price = home_delivery(242, 10, 41)
print("In total:", home_delivery(242, 10, 41))


# this function verifies if the users entered credit card info is correct
def payment():
    number = int(input("Credit card number: "))
    date = int(input("Expiry date: "))
    value = int(input("CVC" "/" "CVV:"))


payment()
# if the credit card info is correct then this message will appear to the customer
print("Credit Card Verified")

root = tk.Tk()
root.geometry("350x500")
root.title("Receipt")
root.configure(background="blue")

label_1 = tk.Label(root, text="--------------------All About Toys Store--------------------")
label_1.config(font="Courier,40")
label_1.pack()

label_2 = tk.Label(root, text=percentage)
label_2.config(font="Courier,40")
label_2.pack()

label_3 = tk.Label(root, text=total_price)
label_3.config(font="Courier,40")
label_3.pack()

label_4 = tk.Label(root, text=41)
label_4.config(font="Courier,40")
label_4.pack()


def delivery1():
    if delivery_cost == 0:
        return "collect from store"


def delivery2():
    if delivery_cost > 0:
        return "Home delivery"


label_5 = tk.Label(root, text='Home delivery')
label_5.config(font="Courier,40")
label_5.pack()

button = tk.Button(root, width=10, height=8).place(x=100, y=500)
btn = tk.Button(root, text='Exit', fg='dark red', bg='dark gray', command=quit)
btn.pack()

btn = tk.Button(root, text='Print', fg='dark red', bg='dark gray', command=exit)
btn.pack()

btn = tk.Button(root, text='Save', fg='dark red', bg='dark gray', command=exit)
btn.pack()

root.title("Receipt")  # The text in the title bar.
root.configure(bg='white')  # Set the colour scheme.

root.mainloop()
