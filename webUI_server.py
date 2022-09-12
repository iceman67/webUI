import socket
from struct import *
import struct
import binascii

# get the hostname
host = "127.0.0.1"
port = 8700  # initiate port no above 1024
RCV_HEADER_SZ = 8
SND_PAYLOAD_SZ = 4


def server_program(host="127.0.0.1", port =8700):
    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    
    while True:
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        
        # get a messsage from webUI
        fmt_str = "<BBBBi" 
        dsize = calcsize(fmt_str)

        recv_buf = conn.recv(RCV_HEADER_SZ)
        (h1, h2, h3 , h4, sz)= unpack(fmt_str, recv_buf)
                
        if not recv_buf:
            # if data is not received break
            break

        recv_buf = conn.recv(sz)
        fmt_str = "<i"
        header = bytearray(SND_PAYLOAD_SZ)
        
        # FPS20
        print (recv_buf[3:5])
        struct.pack_into(fmt_str, header, 0, int(recv_buf[3:5]))
         
        # RELAY the message to Logger (for updating configuration)

        conn.send(header)  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    print ("** start server **")
    server_program()
