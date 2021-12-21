#!/usr/bin/env python3
import sys
sys.dont_write_bytecode = True

from http.server import BaseHTTPRequestHandler, HTTPServer
from ev3dev.ev3 import *
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C

tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)

hostName = "192.168.1.13"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if "/A" in self.path:
            tank_pair.on(left_speed=50, right_speed=50)
        elif "/B" in self.path:
            tank_pair.off()
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes("{}", "utf-8"))
        return

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")