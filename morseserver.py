#!/usr/bin/env python3

import socketserver
import sys
import codecs

morse ={"1" : ".----",
        "2" : "..---",
        "3" : "...--",
        "4" : "....-",
        "5" : ".....",
        "6" : "-....",
        "7" : "--...",
        "8" : "---..",
        "9" : "----.",
        "0" : "-----",
        "a" : ".-",
        "b" : "-...",
        "c" : "-.-.",
        "d" : "-..",
        "e" : ".",
        "f" : "..-."
}

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        MyMorseHandler(self.data)
        # just send back the same data, but upper-cased
        #self.request.sendall(self.data.upper())
        
def MyMorseHandler(data):
        try:
            d = codecs.decode(data)   #aus binary code einen string machen
            for zeichen in d:
                print(morse[zeichen])
        except KeyError as err:
            print("Nicht im Code enthalten:", err.args[0])

if len(sys.argv) !=2:
    raise ValueError("Bitte Port angeben")

port1 = int(sys.argv[1])    #erstes argument ist name von script, zweites ist Wert

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", port1

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()