#!/usr/bin/env python
import sys, time
from socket import *

# UDPClient() sends the parameter [data] to the UDP server
# listening on [serverName]:[serverPort] and recieves [serverName]'s
# response to [data]
#
# input arguments:
# 1. serverName - The hostname of the UDP server you wish to establish
# a UDP connection with
# 2. serverPort - the integer port number on [serverName] that
# listens for UDP connections
# 3. data - the data you would like to send to
# [serverName]:[serverPort]
#
# return values:
# none
def UDPClient(serverName, serverPort, data):
	clientSocket = socket(AF_INET, SOCK_DGRAM)
	clientSocket.sendto(data.encode(), (serverName, serverPort))
	dataFromServer, serverAddress = clientSocket.recvfrom(10000)
	# print 'From Server:', dataFromServer.decode()
	clientSocket.close()

# getAverageUDPTimeToSend() establishes a UDP connection with 
# [serverName]:[serverPort].  Sends this server [data] [repetitions]
# times and returns the average number of seconds it takes to send
# [data] one time.
#
# input arguments:
# 1. serverName - the hostname of the server you wish to
# establish a UDP connection with
# 2. serverPort - the integer port number on [serverName] that
# listens for UDP connections
# 3. data - the data you would like to send to
# [serverName]:[serverPort]
# 4. repetitions - The number of times you would like to send
# [serverName] [data].  The higher this number, the more accurate
# [avgTime] will be
#
# return values:
# avgTime - The average time, in seconds, it takes to send
# [data] to [serverName]:[serverPort] [repetitions] times
def getAverageUDPTimeToSend(serverName, serverPort, data, repetitions):
	timeStart = time.time()
	for iteration in range(0, repetitions):
		UDPClient(serverName, serverPort, data)
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
			avgUDPTimeCurrentByteVar = getAverageUDPTimeToSend(serverName, serverPort, byteString, repetitions)
			print clientName+'\t'+serverName+'\t'+numBytes+'\t'+str(avgUDPTimeCurrentByteVar)		

	else:
		print 'ERROR: Invalid number of arguments'
		
# RUN COMMAND:
# ./UDPClient [serverName] [serverPort]
main()