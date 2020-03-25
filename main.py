import http.server

port = 8080

class serv(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes("Hello world!!!", "utf-8"))


httpd = http.server.HTTPServer(("localhost", port), serv)
httpd.serve_forever()