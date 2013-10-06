#!/usr/bin/python
"""
Simple TCP server that sends back the IP address and port from which it 
sees you connect. Useful when used with `telnet` for network debugging.
Currently only IPv4.
"""
import SocketServer

VERBOSE = False

class TCPHandler(SocketServer.BaseRequestHandler):
    """
    Handles each request be sending the client's IP address and port, then
    closing the connection.
    """
    def handle(self):
        # self.request is the TCP socket connected to the client
        address = self.client_address[0] + ":" + str(self.client_address[1])
        if VERBOSE:
            print "Request from: " + address
        self.request.sendall(address + "\n")


def main():
    import optparse
    global VERBOSE
    parser = optparse.OptionParser()
    parser.add_option("-p", "--port", type="int", default=9999,
                      help="port to listen on")
    parser.add_option("-v", "--verbose", action="store_true")
    options = parser.parse_args()[0]
    port = options.port
    VERBOSE = options.verbose
    server = SocketServer.TCPServer(("0.0.0.0", port), TCPHandler)
    print "Listening on port %d" % port
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
        
if __name__ == "__main__":
    main()
