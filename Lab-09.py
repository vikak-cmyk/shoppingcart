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

myBasket = Item()
