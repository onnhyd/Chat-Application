import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP_address = '192.168.110.66'
Port = 123
server.connect((IP_address, Port))

while True:
	print("accepting requests")
	sockets_list = [sys.stdin, server]
	read_sockets = sockets_list

	for socks in read_sockets:
		if socks == server:
			message = socks.recv(2048)
			print(message)
		else:
			message = sys.stdin.readline()
			server.send(message.encode("utf-8"))
			sys.stdout.write("<You>")
			sys.stdout.write(message)
			sys.stdout.flush()
server.close()

