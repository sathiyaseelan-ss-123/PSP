
from http.server import HTTPServer, BaseHTTPRequestHandler


class NoticeBoard(BaseHTTPRequestHandler):

    def do_GET(self):
        html = """
        <html>
        <head>
            <title>College Notice Board</title>
        </head>
        <body>
            <h1>College Online Notice Board</h1>

            <h2>Announcements</h2>

            <ul>
                <li>Internal examination starts on Monday.</li>
                <li>Annual sports meet registration is open.</li>
                <li>Library will remain open until 7 PM.</li>
                <li>Project submission deadline is Friday.</li>
            </ul>

            <h3>College Information</h3>
            <p>Welcome to the College Online Notice Board.</p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(html.encode())


server = HTTPServer(("127.0.0.1", 8000), NoticeBoard)

print("Notice board running at http://127.0.0.1:8000")
print("Press Ctrl+C to stop.")

server.serve_forever()