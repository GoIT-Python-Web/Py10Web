import urllib.parse
import pathlib
import mimetypes
from http.server import HTTPServer, BaseHTTPRequestHandler

BASE_DIR = pathlib.Path()


class TheBestFastApp(BaseHTTPRequestHandler):
    def do_POST(self):
        length = self.headers.get('Content-Length')
        data = self.rfile.read(int(length))
        print(urllib.parse.unquote_plus(data.decode()))
        self.send_response(302)
        self.send_header('Location', '/contact')
        self.end_headers()

    def do_GET(self):
        route = urllib.parse.urlparse(self.path)
        print(route.path)
        match route.path:
            case '/':
                self.send_html('index.html')
            case '/contact':
                self.send_html('contact.html')
            case '/blog':
                self.send_html('blog.html')
            case _:
                file = BASE_DIR.joinpath(route.path[1:])
                if file.exists():
                    self.send_static(file)
                else:
                    self.send_html('404.html', 404)

    def send_html(self, filename, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as fd:
            self.wfile.write(fd.read())

    def send_static(self, filename, status_code=200):
        self.send_response(status_code)
        mt = mimetypes.guess_type(filename)
        if mt:
            self.send_header('Content-type', mt[0])
        else:
            self.send_header('Content-type', 'text/plain')
        self.end_headers()
        with open(filename, 'rb') as fd:
            self.wfile.write(fd.read())


def run():

    address = ('localhost', 8080)
    httpd = HTTPServer(address, TheBestFastApp)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()


if __name__ == '__main__':
    run()
