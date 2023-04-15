from flask import Flask, request, jsonify, make_response
import sqlite3
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Create a users table in the database to store username and password
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT, password TEXT)''')
conn.commit()
conn.close()

# Define a function to authenticate users
def authenticate(username, password):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = c.fetchone()
    conn.close()
    if user is None:
        return False
    else:
        return True

# Define a function to add a user to the users table
# Define a function to add a user to the users table with default values for username and password
def add_user(username='etai1', password='acavish1'):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()


@app.route('/data', methods=['POST'])
def data():
    # Get the command and email from the request data
    data = request.get_json()
    command = data.get('command')
    username = data.get('username')
    password = data.get('password')

    # Authenticate the user
    if not authenticate(username, password):
        return make_response(jsonify({'error': 'Unauthorized access'}), 401)

    # connect to the database and insert the data into the 'commands' table
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('INSERT INTO commands (command, email) VALUES (?, ?)', (command, email))
    conn.commit()
    conn.close()

    return jsonify({'success': True})

# Define a route to add a new user to the users table
@app.route('/add_user', methods=['POST'])
def add_user_route():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    add_user(username, password)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
