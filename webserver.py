from http.server import HTTPServer,BaseHTTPRequestHandler
import cgi

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                output = ""
                output += "<html><body>Hello!"
                output += "<form method = 'POST' enctype='multipart/form-data' action='/hello'><h2>Waht would your message be?</h2><input name='message' type='text'><input type='submit' value='Submit'></form>"
                output += "</body></html>"
                # in python 3 you are required to encode a string to byte literals
                output = bytes(output,encoding="ascii")
                self.wfile.write(output)
                return
            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                output = ""
                output += "<html><body>Hola!"
                output += "<form method = 'POST' enctype='multipart/form-data' action='/hello'><h2>Waht would your message be?</h2><input name='message' type='text'><input type='submit' value='Submit'></form>"
                output += "</body></html>"
                # in python 3 you are required to encode a string to byte literals
                output = bytes(output,encoding="ascii")
                self.wfile.write(output)
                return
        except:
            print("Inside except")
            self.send_error(404,"File not found %s" %self.path)

    def do_POST(self):
        try:
            self.send_response(301)
            self.end_headers()

            ctype,pdict = cgi.parse(self.headers.getheader('content-type'))
            print("Test")
            if ctype == 'multipart/form-data' :
                fields = cgi.parse_multipart(self.rfile,pdict)
                messagecontent = fields.get('message')

                output = ""
                output += "<html><body>"
                output += "<h2>How about this one :</h2>"
                output += "<h1>%s</h1>" %messagecontent[0]
                output += "<form method = 'POST' enctype='multipart/form-data' action='/hello'><h2>Waht would your message be?</h2><input name='message' type='text'><input type='submit' value='Submit'></form>"
                output += "</body></html>"

                #output = bytes(output,encoding="ascii")
                self.wfile.write(output)
                print(output)
        except:
            print("Inside Except of post")
            pass

def main():
    try:
        port = 8080
        server = HTTPServer(('',port),webserverHandler)
        print("Web Server ruuning on port %s" % port)
        server.serve_forever()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()