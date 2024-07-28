import psycopg2
#  In the file menu_item.py, create a new class called MenuItem, 
# the attributes should be the name and price of each item.

class MenuItem:
    def __init__(self, name: str, price : float) -> None:
        self.name = name
        self.price = price
    
# Create several methods (save, delete, update) these methods will allow a user to save, 
# delete and update items from the Menu_Items table. 
# The update method can update the name as well as the price of an item.
    def save(self):
        connection = psycopg2.connect(
            
        dbname="Menu_Items", 
        user="postgres",
        password="0137",
        host="localhost",
        port="5432"
        )
        cursor = connection.cursor()


        cursor.execute('INSERT INTO menu_items (name, price) VALUES (%s, %s)', (self.name, self.price))
        connection.commit()
        cursor.close()
        connection.close()
    

    def delete(self):
        connection = psycopg2.connect(
            
        dbname="Menu_Items", 
        user="postgres",
        password="0137",
        host="localhost",
        port="5432"
        )
        cursor = connection.cursor()
        cursor.execute('DELETE FROM menu_items WHERE name = %s', (self.name,))
        connection.commit()
        cursor.close()
        connection.close()

    def update(self, new_name=None, new_price=None):
        connection = psycopg2.connect(
          
        dbname="Menu_Items", 
        user="postgres",
        password="0137",
        host="localhost",
        port="5432"
        )
        cursor = connection.cursor()

        if new_name:
            cursor.execute('UPDATE menu_items SET name = %s WHERE name = %s', (new_name, self.name))
            self.name = new_name
        if new_price:
            cursor.execute('UPDATE menu_items SET price = %s WHERE name = %s', (new_price, self.name))
            self.price = new_price
        connection.commit()
        cursor.close()
        connection.close()



