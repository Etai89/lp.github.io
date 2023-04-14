import sqlite3

# connect to the database and read data from the 'users' table
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('SELECT * FROM users')
rows = c.fetchall()

# print the data to the console
for row in rows:
    print('Name:', row[0])
    print('Email:', row[1])
    print('---------------------------------------')

# close the database connection
conn.close()
