from audioop import add
from encodings import utf_8
from http import client
from ipaddress import ip_address
import socket
from sqlite3 import connect
from threading import Thread 


server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000
client = []


server.bind((ip_address , port))

server.listen()

print("Server is running")

def clientthread(conn,address):
    conn.send("Welcome to this chat room".encode('utf-8'))
    while True: 
        try:
            message= conn.recv(2048).decode('utf-8')
            if message:
                print("<"+address[0]+'>'+message)
                message_to_send = "<"+address[0]+'>'+message
                broadcast(message_to_send,conn)
            else:
                remove(conn)
        except:
            continue

def broadcast(message,conn):
    for i in client:
        if i !=conn:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove(client)

def remove(conn):
    if conn in client:
        client.remove(conn)


while True:
    conn,address = server.accept()
    client.append(conn)
    print(address[0]+" connected")
    new_thread = Thread(target=clientthread , args=(conn,address))