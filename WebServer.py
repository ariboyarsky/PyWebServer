# Import socket module
from socket import *
import socket
# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Assign a port number
PORT = 8080
HOST = ''
# Create a log
log = open('log.txt', 'a')
log.write("Python Web Server Log \n")
# Bind the socket to server address and server port
listener.bind((HOST,PORT))
# Listen to at most 1 connection at a time
listener.listen(1)

# Server should be up and running and listening to the incoming connections
print "Running on port: ", PORT
log.write("Running on port: %s " % PORT)
while True:
    print 'Ready to serve...'
    log.write("\n Ready to serve...\n")
    # Set up a new connection from the client
    connection, addr = listener.accept()
    # If an exception occurs during the execution of try clause
    # the rest of the clause is skipped
    # If the exception type matches the word after except
    # the except clause is executed
    try:
        # Receives the request message from the client
        request = connection.recv(1024)
        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        log.write("HTTP Request:\n %s \n" % request)
        req = request.split()
        path = req[1]
        # Because the extracted path of the HTTP request includes
        # a character '\', we read the path from the second character
        path = path[1:]
        log.write("Url Path: %s" % path)
        # Store the entire content of the requested file in a temporary buffer
        f = open(path, "r")
        c = f.read();
        # Send the HTTP response header line to the connection socket
        connection.send('HTTP/1.0 200 OK\r\n')
        log.write("\n Send HTTP 200 OK")
        connection.send("Content-type: text/html\r\n\r\n")
        # Send the content of the requested file to the connection socket
        connection.send(c)
        # Close the client connection socket
        connection.close()
        log.write("\n Connection close \n")

    except IOError:
        # Send HTTP response message for file not found
        connection.send('HTTP/1.0 404 Not Found\r\n')
        log.write("\n Send HTTP 404 Not Found")
        connection.send("Content-type: text/html\r\n\r\n")
        connection.send("<h1>404 Not Found</h1><br/>File not found: %s" % path)
        # Close the client connection socket
        connection.close()
        log.write("\n Connection close\n")
# Close the Server connection socket
listener.close()
log.write("\n Listener close")
