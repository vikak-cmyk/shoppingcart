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