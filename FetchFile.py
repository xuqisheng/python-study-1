#encoding:utf-8
import sys
import socket
import os

'''从远程主机获取文件
	
	本地没有公网IP，远程主机公网IP，连接远程主机获取文件

	Arguments:
		<S/C>:启动Server/启动Client
		<remote path>:远程文件绝对路径

	e.g.:
		Server:python FetchFile.py s
		Client:python FetchFile.py c /etc/hosts > ./hosts
			   python FetchFile.py c shutdown
'''

IP='127.0.0.1'
PORT=5007
BUFFER_SIZE = 1024 

#Arguments
if len(sys.argv)<2:
	print('Need Arguments:<S/C> [<remote path>] [remote ip]')
	sys.exit(0)
command=sys.argv[1]
#Server
if command == 's' or command == 'S':
	server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	#Important! Set reuse
	server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	server_socket.bind((IP,PORT))
	print('listen on :'+str(PORT))
	while 1: 
		server_socket.listen(1)
		conn,addr = server_socket.accept()
		print(addr)
		remote_path = conn.recv(BUFFER_SIZE)
		print(remote_path)
		#Shut down Server
		if remote_path == 'shutdown':break
		#Not exist file
		if not os.path.isfile(remote_path):
			continue
		#Read and Return
		file = open(remote_path,'r')
		print(file)
		data=file.read(BUFFER_SIZE)
		while len(data)>0:
			conn.send(data)
			print(data)
			data=file.read(BUFFER_SIZE)	
		file.close()
		conn.close()
	conn.close()
	server_socket.close()
#Client
elif command == 'c' or command == 'C':
	#Quit without remote path
	if len(sys.argv)<4:
		print('Need Arguments:<S/C> [<remote path>] [remote addr]')
		sys.exit(0)
	#Get remote addr
	IP=sys.argv[3]
	#Get remote path
	remote_path = sys.argv[2]
	client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client.connect((IP,PORT))
	client.send(remote_path)
	while 1:
		data = client.recv(BUFFER_SIZE)
		if not data:break
		print(data)
else:
	print('Need argument s (Server) or c (Client)')

abcdefg