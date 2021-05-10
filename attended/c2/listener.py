from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
from time import sleep
import threading
from urllib.parse import urlparse, unquote_plus, parse_qs

import main

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if 'output' in self.path:
                rq_url = urlparse(self.path)
                rq_param = parse_qs(rq_url.query)
                print()
                for i in rq_param['q']:
                    print(i.strip())
                self.send_response(200)
                self.end_headers()
                #self.wfile.write(b"Hello World")
                self.wfile.write(main.cmd.encode())
                return
        except:
            None
        while main.cmd == '':
            sleep(.25)
        #import pdb;pdb.set_trace()
        self.send_response(200)
        self.end_headers()
        #self.wfile.write(b"Hello World")
        self.wfile.write(main.cmd.encode())
        main.cmd = ''
    # Makes sure log messages are not outputted to terminal.
    def log_message(self,format, *args):
        return

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass

def run():
    #http = ThreadingSimpleServer( ('10.10.14.15', 80), BaseHTTPRequestHandler)
    http = ThreadingSimpleServer( ('10.10.14.15', 80), Handler)
    http.serve_forever()

