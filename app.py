from http.server import HTTPServer, BaseHTTPRequestHandler
class DevOpsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        html = """
        <html>
            <head>
                <title>DevOps App</title>
            </head>
            <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
                <h1>My First DevOps App</h1>
                <H2>Built by Ositadilima Nwabuisi</H2>
                <p>This is a simple DevOps application. Running inside a docker container.</p>
            </body>
        </html>
        """
        self.wfile.write(html.encode())
    def log_message(self, format, *args):
        pass  # Override to prevent logging to stderr
print("Starting server on port 8080...")
httpd = HTTPServer(('', 8080), DevOpsHandler)
httpd.serve_forever()        