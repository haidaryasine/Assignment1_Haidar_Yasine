import socket
import datetime

HOST = '127.0.0.1'
PORT = 1234
BUFFER_SIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

i = 0
while(i < 5):

    # Receive a request from a client
    Request_from_client = server.recvfrom(BUFFER_SIZE)

    # Print time a request is received
    now = datetime.datetime.now()
    print(now)

    # Reply to the client
    address = Request_from_client[1]
    server.sendto(str.encode("I received Your Request"), address)

    i = i + 1

# Close the server socket
server.close()
