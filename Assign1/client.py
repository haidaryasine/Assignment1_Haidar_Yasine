import socket
import datetime
import time


HOST = '127.0.0.1'
PORT = 1234
BUFFER_SIZE = 1024
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Total_time = 0

i = 0
while (i < 5):
    # Time now
    start = time.time()

    # To send an echo request
    client.sendto(str.encode("Hello echo server"), (HOST, PORT))

    # To recieve a reply
    message_from_server = client.recvfrom(BUFFER_SIZE)

    # Time now
    end = time.time()

    # Print the reply received from the server
    msg = "Message from Server {}".format(message_from_server[0])
    print(msg)

    # Print the elapsed time btwn request and reply
    elapsed = end - start
    print("RTT is: ", elapsed)

    # The sum of all elapsed time
    Total_time = Total_time + elapsed
    i = i + 1

# Print the average of the elapsed time
Average = Total_time/5
print("The Average RTT",  Average)

# Close the client socket
client.close()
