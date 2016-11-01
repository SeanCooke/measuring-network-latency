#!/usr/bin/env python
import sys, time
from socket import *

# TCPClient() opens a TCP Connection with a server, sends data
# to that server and receives data from that server.
#
# input arguments:
# 1. serverName - the hostname of the server you wish to
# establish a TCP connection with
# 2. serverPort - the integer port number on [serverName] that
# listens for TCP connections
# 3. data - the data you would like to send to
# [serverName]:[serverPort]
#
# return values:
# none
def TCPClient(serverName, serverPort, data):
	serverName = serverName
	serverPort = serverPort
	clientSocket = socket(AF_INET, SOCK_STREAM)
	clientSocket.connect((serverName, serverPort))
	clientSocket.send(data.encode())
	dataFromServer = ''
	# receive data from [serverName] in 2048 byte chunks
	while True:
		messageFragmentFromServer = clientSocket.recv(2048)
		if not messageFragmentFromServer:
			break
		dataFromServer += messageFragmentFromServer
	# print 'From Server:', dataFromServer.decode()
	clientSocket.close()

# getAverageTCPTimeToSend() establishes a TCP connection with 
# [serverName]:[serverPort].  Sends this server [data] [repetitions]
# times and returns the average number of seconds it takes to send
# [data] one time.
#
# input arguments:
# 1. serverName - the hostname of the server you wish to
# establish a TCP connection with
# 2. serverPort - the integer port number on [serverName] that
# listens for TCP connections
# 3. data - the data you would like to send to
# [serverName]:[serverPort]
# 4. repetitions - The number of times you would like to send
# [serverName] [data].  The higher this number, the more accurate
# [avgTime] will be
#
# return values:
# avgTime - The average time, in seconds, it takes to send
# [data] to [serverName]:[serverPort] [repetitions] times
def getAverageTCPTimeToSend(serverName, serverPort, data, repetitions):
	timeStart = time.time()
	for iteration in range(0, repetitions):
		TCPClient(serverName, serverPort, data)
	deltaTime = time.time() - timeStart
	avgTime = deltaTime/repetitions
	return avgTime

# main() will send 1 byte, 10 bytes, 100 bytes and 1,000 bytes and
# 10,000 bytes to the host specified in the first command line argument
# on the port specified in the second command line argument 100 times.
#
# main() will then print out the average round trip time for these
# data streams in a table as well as the number of repetitions.
def main():
	if len(sys.argv) == 3:
		clientName = gethostname()
		serverName = sys.argv[1]
		serverPort = int(sys.argv[2])
		repetitions = 100
		
		listOfBytes = []
		for magnitude in range(0, 5):
			numBytes = 10**magnitude
			byteString = 'a' * numBytes
			byteVarArray = [numBytes, byteString]
			listOfBytes.append(byteVarArray)
		
		print 'Number of Repetitions: '+str(repetitions)
		print 'Client\t\t\t\t\tServer\t\t\t\t\tBytes\tAverage Time (sec)'
		for currentByteList in listOfBytes:
			numBytes = str(currentByteList[0])
			byteString = currentByteList[1]
			avgTCPTimeCurrentByteVar = getAverageTCPTimeToSend(serverName, serverPort, byteString, repetitions)
			print clientName+'\t'+serverName+'\t'+numBytes+'\t'+str(avgTCPTimeCurrentByteVar)		
	else:
		print 'ERROR: Invalid number of arguments'

# RUN COMMAND:
# ./TCPClient [serverName] [serverPort]
main()