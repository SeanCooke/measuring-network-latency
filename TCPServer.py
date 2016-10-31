#!/usr/bin/env python
import sys, threading
from socket import *

# requestThread() allows for a concurrent TCP server.
#
# requestThread() is a two tuple composed of a connectionSocket
# and an address.  connectionSocket is a socket object and
# address is a list composed of the hostname and port number
# this request thread listens on.  requestThread() processes
# a TCP request then kills the thread.
class requestThread(threading.Thread):
	def __init__(self, connectionSocket, addr):
		threading.Thread.__init__(self)
		self.connectionSocket = connectionSocket
		self.addr = addr
	def run(self):
		ipAddressPortNumber = self.addr[0]+':'+str(self.addr[1])
		print 'TCP connection opened with: '+ipAddressPortNumber
		message = 'Connection closed by client before response sent.'
		# receiving data from the client in one 10000 byte chunk
		message = self.connectionSocket.recv(10000)
		self.connectionSocket.send(message.encode())
		self.connectionSocket.close()
		print 'TCP connection closed with: '+ipAddressPortNumber+'.  Sent \''+message+'\'.'

# TCPServer() starts a concurrent TCP Server on the machine
# on which the TCPServer executable is run, on the parameter
# [serverPort].
# 
# input arguments:
# 1. serverPort - The integer port number on the machine on which
# the TCPServer executable is run that listens for TCP connections
#
# return values:
# none
def TCPServer(serverPort):
		serverName = gethostname()
		serverPortStr = str(serverPort)
		serverSocket = socket(AF_INET, SOCK_STREAM)
		serverSocket.bind(('',serverPort))
		serverSocket.listen(1)
		print serverName+' listening for TCP connections on port '+serverPortStr
		try:
			while True:
				# for each new TCP request, spawn off a new requestThread()
				connectionSocket, addr = serverSocket.accept()
				requestThread(connectionSocket, addr).start()
		except KeyboardInterrupt:
			print '\nTCP Server '+serverName+' listening on port '+serverPortStr+' stopped with a keyboard interrupt.'

# main() starts a concurrent TCP Server on the machine on which
# the TCPServer executable is run, on the port specified
# in the first command line argument.
def main():
	if len(sys.argv) == 2:
		TCPServer(int(sys.argv[1]))
	else:
		print 'ERROR: Invalid number of arguments'

# RUN COMMAND:
# ./TCPServer [serverPort]
main()