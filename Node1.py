import socket
import threading
import os

senderip = input("Enter your IP Address: ")
sport = int(input("Enter your port number: "))
receiverip = input("Enter receiver's IP Address: ")
rport = int(input("Enter receiver's port number: "))
os.system("cls")
print("\t\tChat-App")


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((senderip, sport))
def send():
	while True:
		msg = input()
		s.sendto(msg.encode(), (receiverip, rport))
def receive():
	while True:
		incmg = s.recvfrom(1024)
		msg = incmg[0].decode()
		print("Received ({}): {}".format(receiverip, msg))

t1 = threading.Thread(target=send)
t2 = threading.Thread(target=receive)
t1.start()
t2.start()

