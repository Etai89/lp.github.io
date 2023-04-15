from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import sqlite3

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        data = json.loads(post_body)

        print("Name:", data['name'])


        # connect to the database and insert the data
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS users (name TEXT, email TEXT)')
        c.execute('INSERT INTO users VALUES (?, ?)', (data['name']))
        conn.commit()
        conn.close()

        # send a response to the client
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Success')

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()


server = HTTPServer(('localhost', 5000), RequestHandler)
server.serve_forever()

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Starting server...')
    httpd.serve_forever()
