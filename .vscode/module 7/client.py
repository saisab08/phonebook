import socket
HOST = '192.168.18.208'
PORT = 65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    print("connected to the server ")

    while True:
        message = input("enter the message:")
        if message.lower()=="exit":
            print("disconnect init from the server")
            break
        s.sendall(message.encode())#send the message to the server

        #Receive a response from the server
        data = s.recv(1024)
        print("server responded:{data.decode()}")