import sqlite3
import time

import winsound


def clear_db():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('DELETE FROM users')
    conn.commit()
    conn.close()
    


def clear_db():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('DELETE FROM users')
    conn.commit()
    conn.close()


while True:
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
        if "here" in row[0] or "here" in row[1]:
            print("activated")
            winsound.Beep(1350, 160)
##        else:
##            winsound.Beep(2550, 160)


    # close the database connection
    conn.close()
    time.sleep(5)



    # print the data to the console
    for row in rows:
        print('Name:', row[0])
        print('Email:', row[1])
        print('---------------------------------------')

    # close the database connection
    conn.close()

    # clear the database every 30 seconds
    time.sleep(30)
    #clear_db()

