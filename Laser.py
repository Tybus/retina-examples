#!/usr/bin/env python
import sys
import socket
import time
italk = socket.socket()
pos = socket.socket()
def connect():
	italk.connect((sys.argv[1],12345))
	print(italk.recv(1000))
	pos.connect((sys.argv[1],12347))
	return italk
def jogleft():
	italk.send("pass 32\n")
	print(italk.recv(1000))
	italk.sendall('\xaa\x01\x14\x00\x04\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xbb\xcc\xbb\xcc\xbb\xcc\xbb\xcc')
	print(italk.recv(1000))
	time.sleep(0.4)		
	italk.send('pass 16\n')
	print(italk.recv(1000))
	italk.send('\xaa\x06\x04\x00\x73\xf7\x01\x00\xbb\xcc\xbb\xcc\xbb\xcc\xbb\xcc')
	print(italk.recv(1000))
def jogright():
	italk.send("pass 32\n")
	print(italk.recv(1000))
	italk.sendall('\xaa\x01\x14\x00\x04\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xbb\xcc\xbb\xcc\xbb\xcc\xbb\xcc')
	print(italk.recv(1000))
	time.sleep(0.4)		
	italk.send('pass 16\n')
	print(italk.recv(1000))
	italk.send('\xaa\x06\x04\x00\x73\xf7\x01\x00\xbb\xcc\xbb\xcc\xbb\xcc\xbb\xcc')
	print(italk.recv(1000))
def jogup():
	italk.send("pass 32\n")
	print(italk.recv(1000))
	italk.sendall('\xaa\x01\x14\x00\x04\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xbb\xcc\xbb\xcc\xbb\xcc\xbb\xcc')
	print(italk.recv(1000))
	time.sleep(0.4)		
	italk.send('pass 16\n')
	print(italk.recv(1000))
	italk.send('\xaa\x06\x04\x00\x73\xf7\x01\x00\xbb\xcc\xbb\xcc\xbb\xcc\xbb\xcc')
	print(italk.recv(1000))
def jogdown():
	italk.send("pass 32\n")
	print(italk.recv(1000))
	italk.sendall('\xaa\x01\x14\x00\x04\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xbb\xcc\xbb\xcc\xbb\xcc\xbb\xcc')
	print(italk.recv(1000))
	time.sleep(0.4)		
	italk.send('pass 16\n')
	print(italk.recv(1000))
	italk.send('\xaa\x06\x04\x00\x73\xf7\x01\x00\xbb\xcc\xbb\xcc\xbb\xcc\xbb\xcc')
	print(italk.recv(1000))
def testfire():
	italk.send("pass 32\n")
	print(italk.recv(1000))
	tiempo = sys.argv[3]
	tiempo = tiempo*10
	tiempo = hex(tiempo)
	tiempo = tiempo.replace("0","")
	data = "\xaa\x01\x14\x00\x0d\x00"
	data +="\ "+tiempo
	data +="\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xbb\xcc\xbb\xcc\xbb\xcc\xbb\xcc"
	data = data.replace(" ","")
	italk.send(data)
	print(italk.recv(1000))
def gohome():
	italk.send("pass 32\n")
	print(italk.recv(100))
	italk.sendall("\xaa\x01\x14\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xbb\xcc\xbb\xcc\xbb\xcc\xbb\xcc")
	print(italk.recv(100))
connect()
if sys.argv[2] == "jogu": 
	jogup()
elif sys.argv[2] == "jogd":
	jogdown()
elif sys.argv[2] == "jogl":
	jogleft()
elif sys.argv[2] == "jogr":
	jogright()
elif sys.argv[2] == "testF":
	testfire()
elif sys.argv[2] == "gohome":
	gohome()
else:
	print("Valid Values are : jogu, jogd, jogl, jogr,testF")






	
