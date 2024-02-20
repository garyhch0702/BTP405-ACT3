from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import mysql.connector

def create_table():
    conn = mysql.connector.connect(
        host='GaryHu',  
        user='root', 
        password='657300',  
        database='BTPact3' 
    )
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            content TEXT NOT NULL
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()

create_table()

class NoteRequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, content_type='application/json'):
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM notes")
        notes = cursor.fetchall()
        cursor.close()
        conn.close()

        self._set_headers()
        self.wfile.write(json.dumps(notes).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = json.loads(self.rfile.read(content_length))

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO notes (title, content) VALUES (%s, %s)", 
                       (post_data['title'], post_data['content']))
        conn.commit()
        cursor.close()
        conn.close()

        self._set_headers()
        self.wfile.write(json.dumps({"message": "Note created successfully"}).encode('utf-8'))

    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        post_data = json.loads(self.rfile.read(content_length))
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE notes SET title = %s, content = %s WHERE id = %s", 
                       (post_data['title'], post_data['content'], post_data['id']))
        conn.commit()
        cursor.close()
        conn.close()

        self._set_headers()
        self.wfile.write(json.dumps({"message": "Note updated successfully"}).encode('utf-8'))

    def do_DELETE(self):
        query_string = self.path.split('?', 1)[-1]
        note_id = int(query_string.split('=')[-1])

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM notes WHERE id = %s", (note_id,))
        conn.commit()
        cursor.close()
        conn.close()

        self._set_headers()
        self.wfile.write(json.dumps({"message": "Note deleted successfully"}).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=NoteRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Stopping httpd...')
        httpd.server_close()

if __name__ == '__main__':
    run()
