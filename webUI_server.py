import socket
from struct import *


def server_program():
    # get the hostname
    host = "127.0.0.1"
    port = 4000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    
    while True:
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        
        fmt_str = "<BBBi" 
        dsize = calcsize(fmt_str)

        recv_buf = conn.recv(7)
                
        if not recv_buf:
            # if data is not received break
            break
        #conn.send(b"ACK")  # send data to the client
        conn.send(recv_buf)  # send data to the client


    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()