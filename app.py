from flask import Flask, jsonify, request, render_template
import sqlite3

app = Flask(__name__)

def get_menu():
    conn = sqlite3.connect('kiosk.db')
    cursor = conn.cursor()
    cursor.execute('SELECT item, price, category FROM menu')
    menu = cursor.fetchall()
    conn.close()
    return [{'item': item[0], 'price': item[1], 'category': item[2]} for item in menu]


@app.route('/')
def index():
    return render_template('index.html', menu=get_menu())

@app.route('/order', methods=['POST'])
def order():
    items = request.json.get('items', [])
    total = sum(item['price'] for item in items)
    return jsonify({'total': total})

if __name__ == '__main__':
    app.run(debug=True)
