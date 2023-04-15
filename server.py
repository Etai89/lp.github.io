from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import sqlite3
import winsound


def clear_db():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('DELETE FROM users')
    conn.commit()
    conn.close()


class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        data = json.loads(post_body)

        print("Command:", data['name'])

        # check if "clear data" is in the received data
        if "clear data" in data['name']:
            clear_db()  # call the clear_db function to clear the database file
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b'Data cleared successfully')
            return

        # check if "print data" is in the received data
        if "print data" in data['name']:
            conn = sqlite3.connect('example.db')
            c = conn.cursor()
            c.execute('SELECT * FROM users')
            rows = c.fetchall()
            for row in rows:
                print(row[0])
            conn.close()

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b'Data printed successfully')
            return

        # check if "money" is in the received data
        if "money" in data['name']:
            print('activate')
            winsound.Beep(1350, 160)
            response_to_website = "Ok brother"
        else:
            response_to_website = "Success"

        # connect to the database and insert the name
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS users (name TEXT)')
        c.execute('INSERT INTO users (name) VALUES (?)', (data['name'],))
        conn.commit()
        conn.close()

        # send a response to the client
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(response_to_website.encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()


if __name__ == '__main__':
    server_address = ('10.100.102.34', 5000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Starting server...')
    httpd.serve_forever()
