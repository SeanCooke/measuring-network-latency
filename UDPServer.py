#!/usr/bin/env python
import sys
from socket import *

# UDPServer() starts a UDP Server on the machine on which the
# UDPServer executable is run, on the parameter [serverPort].
# 
# input arguments:
# 1. serverPort - The integer port number on the machine on which
# the UDPServer executable is run that listens for TCP connections
#
# return values:
# none
def UDPServer(serverPort):
	serverName = gethostname()
	serverPortStr = str(serverPort)
	serverSocket = socket(AF_INET, SOCK_DGRAM)
	serverSocket.bind(('', serverPort))
	print serverName+' listening for UDP connections on port '+serverPortStr
	try:
		while True:
			message, addr = serverSocket.recvfrom(10000)
			ipAddressPortNumber = addr[0]+':'+str(addr[1])
			print 'TCP connection opened with: '+ipAddressPortNumber
			serverSocket.sendto(message.encode(), addr)
			print 'Sent \''+message+'\' to '+ipAddressPortNumber+'.'
	except KeyboardInterrupt:
		print '\nUDP Server '+serverName+' listening on port '+serverPortStr+' stopped with a keyboard interrupt.'

# main() starts a UDP Server on the machine on which the
# UDPServer executable is run, on the port specified in the
# first command line argument.
def main():
	if len(sys.argv) == 2:
		UDPServer(int(sys.argv[1]))
	else:
		print 'ERROR: Invalid number of arguments'

# RUN COMMAND:
# ./UDPServer [serverPort]
main()