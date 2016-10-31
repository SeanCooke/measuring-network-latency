all:
	cp TCPClient.py TCPClient
	cp TCPServer.py TCPServer
	cp UDPClient.py UDPClient
	cp UDPServer.py UDPServer
	chmod +x TCPClient
	chmod +x TCPServer
	chmod +x UDPClient
	chmod +x UDPServer

clean:
	rm -rf TCPClient
	rm -rf TCPServer
	rm -rf UDPClient
	rm -rf UDPServer