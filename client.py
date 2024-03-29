#!/usr/bin/env python3
# Python program to implement client side of chat room. 
import socket 
import select 
import sys 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
if len(sys.argv) != 3: 
	print ("Correct usage: script, IP address, port number")
	exit() 
name = input('Your name: ')
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 

server.connect((IP_address, Port))
server.send(name.encode()) 

while True: 

	# maintains a list of possible input streams 
	sockets_list = [sys.stdin, server] 

	""" There are two possible input situations. Either the 
	user wants to give manual input to send to other people, 
	or the server is sending a message to be printed on the 
	screen. Select returns from sockets_list, the stream that 
	is reader for input. So for example, if the server wants 
	to send a message, then the if condition will hold true 
	below.If the user wants to send a message, the else 
	condition will evaluate as true"""
	read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 

	for socks in read_sockets: 
		if socks == server: 
			message = socks.recv(2048) 
			print (message.decode()) 
		else:
			message = name + ": " + sys.stdin.readline()
			msg_quit = name + ": " + "[bye]";
			if message == msg_quit:
				message = name + " is leaving the Chat room"
				soc.send(message.encode())
				print("\n")
				break
			sys.stdout.write("> ") 
			server.send(message.encode()) 
			# sys.stdout.write("You: ") 
			sys.stdout.write(message) 
			sys.stdout.flush() 
server.close() 
