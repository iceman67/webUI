from struct import *
import array
import struct



st = Struct("<B")
packed_value = st.pack(1)
print( packed_value )


# big endian > 
st = Struct(">i")
packed_value =  st.pack(1)

print (packed_value)

# little endian  <
st = Struct("<i")
packed_value =  st.pack(1)
print (packed_value)



import socket 

def client_program(bmsg):
    host = "127.0.0.1"  # as both code is running on same pc
    port = 4000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    client_socket.sendall (bmsg)  # send message
    data = client_socket.recv(7) # receive response

    import binascii
    
    recv = binascii.hexlify(data).decode() # bytes to hex => string
    print (recv)
    print (bytes.fromhex(recv) )  # string to bytes

    print (bytes.fromhex(recv)[0])
    print (bytes.fromhex(recv)[1])
    print (bytes.fromhex(recv)[2])

    print ( unpack('<i',bytes.fromhex(recv)[3:8] )  )
    t = unpack('<i',bytes.fromhex(recv)[3:8])

    print ( t[0] )

    client_socket.close()  # close the connection


## MESSAGE DEFINE
send_buf = bytearray(7)
fmt_str = "<BBBi" 
struct.pack_into(fmt_str, send_buf, 0, 1, 1,15, 2) # offset, v1, v2, v3, v4
print (send_buf)

byteObject = bytes(send_buf)
print (byteObject)

client_program(byteObject)