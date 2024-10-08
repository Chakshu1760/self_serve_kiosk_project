import sqlite3

def create_db():
    conn = sqlite3.connect('kiosk.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS menu (
            id INTEGER PRIMARY KEY,
            item TEXT NOT NULL,
            price REAL NOT NULL,
            combo INTEGER NOT NULL DEFAULT 0  -- 1 if it's a combo, 0 if it's a single item
        )
    ''')

    # Sample menu items for Chick-fil-A
    menu_items = [
        ('Chick-fil-A Chicken Sandwich Combo', 8.99, 1),
        ('Chick-fil-A Deluxe Sandwich Combo', 9.29, 1),
        ('Chicken Nuggets Combo', 9.49, 1),
        ('Spicy Chicken Sandwich Combo', 9.79, 1),
        ('Spicy Deluxe Sandwich Combo', 9.49, 1),
        ('Spicy Chicken Strips Combo', 7.99, 1),
        ('Grilled Chicken Sandwich Combo', 8.49, 1),
        ('Grilled Chicken Club Combo', 9.99, 1),
        ('Grilled Nuggets Combo', 9.89, 1),
        ('Chick-fil-A Chicken Sandwich', 3.49, 0),
        ('Chick-fil-A Deluxe Sandwich', 3.79, 0),
        ('Chicken Nuggets', 4.49, 0),
        ('Spicy Chicken Sandwich', 4.99, 0),
        ('Spicy Deluxe Sanwich', 4.49, 0),
        ('Spicy Chicken Strips', 2.99, 0),
        ('Grilled Chicken Sandwich', 3.49, 0),
        ('Grilled Chicken Club', 4.99, 0),
        ('Grilled Nuggets', 4.89, 0),
        ('Waffle Fries', 2.19, 0),
        ('Beverage', 1.99, 0)
    ]

    cursor.executemany('INSERT INTO menu (item, price, combo) VALUES (?, ?, ?)', menu_items)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()
