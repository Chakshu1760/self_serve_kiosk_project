import sqlite3

def create_db():
    conn = sqlite3.connect('kiosk.db')
    cursor = conn.cursor()

    # Drop the menu table if it exists
    cursor.execute('DROP TABLE IF EXISTS menu')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS menu (
            id INTEGER PRIMARY KEY,
            item TEXT NOT NULL,
            price REAL NOT NULL,
            combo INTEGER NOT NULL DEFAULT 0,  -- 1 if it's a combo, 0 if it's a single item
            category TEXT NOT NULL               -- Added category field
        )
    ''')

    # Sample menu items for Chick-fil-A with categories
    menu_items = [
        ('Chick-fil-A Chicken Sandwich Combo', 8.99, 1, 'Fried'),
        ('Chick-fil-A Deluxe Sandwich Combo', 9.29, 1, 'Fried'),
        ('Chicken Nuggets Combo', 9.49, 1, 'Fried'),
        ('Spicy Chicken Sandwich Combo', 9.79, 1, 'Fried'),
        ('Spicy Deluxe Sandwich Combo', 9.49, 1, 'Fried'),
        ('Spicy Chicken Strips Combo', 7.99, 1, 'Fried'),
        ('Grilled Chicken Sandwich Combo', 8.49, 1, 'Grilled'),
        ('Grilled Chicken Club Combo', 9.99, 1, 'Grilled'),
        ('Grilled Nuggets Combo', 9.89, 1, 'Grilled'),
        ('Chick-fil-A Chicken Sandwich', 3.49, 0, 'Fried'),
        ('Chick-fil-A Deluxe Sandwich', 3.79, 0, 'Fried'),
        ('Chicken Nuggets', 4.49, 0, 'Fried'),
        ('Spicy Chicken Sandwich', 4.99, 0, 'Fried'),
        ('Spicy Deluxe Sandwich', 4.49, 0, 'Fried'),
        ('Spicy Chicken Strips', 2.99, 0, 'Fried'),
        ('Grilled Chicken Sandwich', 3.49, 0, 'Grilled'),
        ('Grilled Chicken Club', 4.99, 0, 'Grilled'),
        ('Grilled Nuggets', 4.89, 0, 'Grilled'),
        ('Waffle Fries', 2.19, 0, 'Sides'),
        ('Beverage', 1.99, 0, 'Beverages'),
        ('Side Salad', 3.49, 0, 'Salads'),
        ('Fruit Cup', 2.99, 0, 'Sides')
    ]

    cursor.executemany('INSERT INTO menu (item, price, combo, category) VALUES (?, ?, ?, ?)', menu_items)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()
