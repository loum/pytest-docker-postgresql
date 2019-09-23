#!/usr/bin/python

import BaseHTTPServer
import CGIHTTPServer

def run(server_class=BaseHTTPServer.HTTPServer,
        handler_class=CGIHTTPServer.CGIHTTPRequestHandler):
    server_address = ('', 8888)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    run()
