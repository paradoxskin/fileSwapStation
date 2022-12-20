import socket,time,os,platform,threading

def clear():
	if(platform.system() == "Windows"):
		os.system("cls")
	else:
		os.system("clear")

def getIp():
	tmp = socket.gethostbyname(socket.gethostname())
	print(f'[*] your local ip is {tmp}.')
	return tmp

def getSocket(yourIp):
	ipt=input("[?] do you know the server's ip address?(n for don't) ")
	if ipt!='n' and len(ipt.split('.'))==4:
		try:
			tmp = socket.create_connection((ipt,23333),timeout=5)
			print(f'[+] found server at {ipt} !')
			return tmp
		except:
			print("[x] not server's ip address :(")
	if input('[?] enter y to create server directly. ') == 'y':
		return 0
	print("[*] finding for server...(just at 0-255)")
	for i in range(256):
		if i == int(yourIp.split('.')[-1]):
			continue
		ip = '.'.join(yourIp.split('.')[:-1])+'.'+str(i)
		print(f"[-] scaning at {ip}:23333 ..")
		try:
			tmp = socket.create_connection((ip,23333),timeout=0.45)
			clear()
			print(f'[+] found server at {ip} !')
			return tmp
		except:
			continue
	clear()
	print('[x] no server found :(')
	return 0

def getServer(yourIp):
	try:
		tmp = socket.create_server((yourIp,23333))
		print(f'[+] done, your id is {yourIp}')
		return tmp
	except:
		print('[x] fail :(')
		return 0

def main():
	nowIp = getIp()
	skt = getSocket(nowIp)
	if skt == 0:
		ser = getServer(nowIp)
		ser.listen()
		print('[*] start listening ..')
		while True:
			serveOn = ser.accept()
			print(f'[+] {serveOn[1]} connected.')
			serveOn[0].send(b'hello,world')
			serveOn[0].close()
			print('[*] connect closed.')
	else:
		data=skt.recv(1024)
		print(f'[+] recv the message: {data.decode()}')

if __name__ == "__main__":
	main()
