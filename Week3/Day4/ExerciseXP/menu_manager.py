# In the file menu_manager.py, create a new class called MenuManager
# Create a Class Method called get_by_name that will return a single item from the Menu_Items table depending 
# on it’s name, if an object is not found (there is no item matching the name in the get_by_name method) return None.

# Create a Class Method called all_items which will return a list of all the items from the Menu_Items table. 

import psycopg2

class MenuManager:

    
    def get_by_name(cls, name):
        connection = psycopg2.connect(
            dbname="Menu_Items",
            user="postgres",
            password="0137",
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()
        
        cursor.execute('SELECT * FROM menu_items WHERE item_name = %s', (name,))
        item = cursor.fetchone()
        
        cursor.close()
        connection.close()
        
        if item:
            return {'item_id': item[0], 'item_name': item[1], 'item_price': item[2]}
        else:
            return None

  
    def all_items(cls):
        connection = psycopg2.connect(
            dbname="Menu_Items",
            user="postgres",
            password="0137",
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()
        
        cursor.execute('SELECT * FROM menu_items')
        items = cursor.fetchall()
        
        cursor.close()
        connection.close()
        
        return [{'item_id': item[0], 'item_name': item[1], 'item_price': item[2]} for item in items]
