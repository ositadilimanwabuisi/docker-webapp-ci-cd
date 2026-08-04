from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class DevOpsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        db_host = os.environ.get('DB_HOST', 'not connected')
        
        html = f"""
        <html>
        <body style="font-family: Arial; text-align: center; padding: 50px;">
            <h1>My First Docker App!</h1>
            <h2>Built by Ositadilima Nwabuisi</h2>
            <p>Running inside a Docker container</p>
            <p>Database Host: {db_host}</p>
            <p>Month 2 - DevOps Foundations</p>
        </body>
        </html>
        """
        self.wfile.write(html.encode())

    def log_message(self, format, *args):
        pass

print("Server starting on port 8080...")
httpd = HTTPServer(('0.0.0.0', 8080), DevOpsHandler)
httpd.serve_forever()