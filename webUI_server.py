import socket
from struct import *
import struct
import binascii


def server_program():
    # get the hostname
    host = "127.0.0.1"
    port = 8700  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    
    while True:
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        
        fmt_str = "<BBBBi" 
        dsize = calcsize(fmt_str)

        recv_buf = conn.recv(8)
        (h1, h2, h3 , h4, sz)= unpack(fmt_str, recv_buf)
                
        if not recv_buf:
            # if data is not received break
            break

        recv_buf = conn.recv(5)
        fmt_str = "<i"
        header = bytearray(4)
        print (recv_buf[3:5])
        struct.pack_into(fmt_str, header, 0, int(recv_buf[3:5]))
        conn.send(header)  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
