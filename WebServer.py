# Import socket module
from socket import *    

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)


# Assign a port number

# Bind the socket to server address and server port

# Listen to at most 1 connection at a time

# Server should be up and running and listening to the incoming connections
while True:
	print 'Ready to serve...'
	
	# Set up a new connection from the client
	
	# If an exception occurs during the execution of try clause
	# the rest of the clause is skipped
	# If the exception type matches the word after except
	# the except clause is executed
	try:
		# Receives the request message from the client

		# Extract the path of the requested object from the message
		# The path is the second part of HTTP header, identified by [1]

		# Because the extracted path of the HTTP request includes 
		# a character '\', we read the path from the second character 

		# Store the entire contenet of the requested file in a temporary buffer

		# Send the HTTP response header line to the connection socket

 
		# Send the content of the requested file to the connection socket

		# Close the client connection socket


	except IOError:
		# Send HTTP response message for file not found

		# Close the client connection socket

# Close the Server connection socket
