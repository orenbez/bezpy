# https://www.youtube.com/watch?v=Lbfe3-v7yE0
# https://youtu.be/CV7_stUWvBQ   SOCKETS
# https://realpython.com/python-sockets/
# https://www.tutorialspoint.com/python_penetration_testing/python_penetration_testing_socket_and_methods.htm
# https://www.tutorialspoint.com/python/python_networking.htm

# for threading see C:\Users\orenb\OneDrive\PYTHON\01_MISC\Sockets Tutorial
# https://www.techwithtim.net/tutorials/socket-programming/

# Packet = block of data sent across a network


import pickle  # to convert any python object to bytes so you can send it
import socket

BUFFSIZE = 1024                       # Size of the packets
PORT = 7383                           # 7383 is a random portnumber
HOST = socket.gethostname()           # Returns LOCAL HOST,  PC / Server Name
IP_ADDR = socket.gethostbyname(HOST)  # IP ADDRESS
ADDR = (HOST, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET = IPV4, SOCK_STREAM = TCP
s.bind(ADDR)  # Returns your PC NAME / LOCAL HOST,
s.listen(5)  # listens up to a queue of 5 calls

# Waits for client to attempt connection
while True:
    clientsocket, address = s.accept()  # returns socket & address from the client
    print(f'connection from {address[0]}:{address[1]} has been established!')
    x = clientsocket.recv(BUFFSIZE)
    y = x.decode(encoding='utf-8', errors='strict')
    policy_num, vehicle_num  = y.split(',')
    obj = {'policy_number':policy_num, 'vehicle_number': vehicle_num}
    obj_pickled = pickle.dumps(obj)
    clientsocket.send(bytes("Welcome to the server here is your object:",'utf-8'))
    clientsocket.send(obj_pickled)                   # also see sendall()
    clientsocket.close()  # close connection         # also see shutdown(SHUT_WR)

s.close()