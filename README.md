# Measuring Network Latency

[Read me on GitHub!](https://github.com/SeanCooke/measuring-network-latency)

## Commands
BUILD COMMAND: `$ make all`

RUN COMMANDS:

TCPServer: `$ ./TCPServer [server_port_number]`

TCPClient: `$ ./TCPClient [server_name] [server_port_number]`

UDPServer: `$ ./UDPServer [server_port_number]`

UDPClient: `$ ./UDPClient [server_name] [server_port_number]`

CLEAN COMMAND: `$ make clean`

## Objective
Measuring Network Latency measures the network latency of TCP and UDP messages between two machines.  `TCPClient` and `UDPClient` send 1 byte, 10 bytes, 100 bytes, 1,000 bytes, and 10,000 bytes of data over both TCP and UDP 100 times and print a table containing the average round trip time.

## Results
After running the command `$ ./TCPServer [server_port_number]` on machine CLIENT_NAME then running `$ ./TCPClient [server_name] [server_port_number]` on machine SERVER_NAME we see a table like the one shown below:

    Number of Repetitions: 100
    Client		Server			Bytes		Average Time (sec)
    CLIENT_NAME	SERVER_NAME		1			0.00131623029709
    CLIENT_NAME	SERVER_NAME		10			0.00130241155624
    CLIENT_NAME	SERVER_NAME		100			0.00110690116882
    CLIENT_NAME	SERVER_NAME		1000		0.00114426136017
    CLIENT_NAME SERVER_NAME     10000	    0.00150153875351


After running the command `$ ./UDPServer [server_port_number]` on machine CLIENT_NAME then running `$ ./UDPClient [server_name] [server_port_number]` on machine SERVER_NAME we see a table like the one shown below:

    Number of Repetitions: 100
    Client		Server			Bytes		Average Time (sec)
    CLIENT_NAME	SERVER_NAME		1			0.000562031269073
    CLIENT_NAME	SERVER_NAME		10			0.000509560108185
    CLIENT_NAME	SERVER_NAME		100			0.000526950359344
    CLIENT_NAME	SERVER_NAME		1000		0.000582931041718
    CLIENT_NAME SERVER_NAME     10000	    0.000999598503113

It is observed that UDP is an order of magnitude faster than TCP.  This is because UDP is a connectionless protocol while TCP is a connection-oriented protocol.

These observations were taken on two machines in the same network.

## Method
`TCPClient` and `UDPClient` start a clock before sending a message to `TCPServer` and `UDPServer`, respectively.  `TCPClient` and `UDPClient` then send bytes of data to `TCPServer` and `UDPServer`, respectively 100 times.  `TCPClient` and `UDPClient` then stop their clock, and divide the clock time by 100 to get the average round trip time for one request.

This process is repeated for data of size 1 byte, 10 bytes, 100 bytes, 1,000 bytes, and 10,000 bytes.