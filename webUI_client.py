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

def client_program(header, payload):
    host = "127.0.0.1"  # as both code is running on same pc
    port = 8700  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    client_socket.sendall (header)  # send message
    client_socket.sendall (payload)  # send message

    #data = client_socket.recv(7) # receive response
    client_socket.close()  # close the connection
'''
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
'''


## MESSAGE DEFINE
header = bytearray(8)
fmt_str = "<BBBBi" 
struct.pack_into(fmt_str, header, 0, 0x01, 0x12, 0xff,0, 5) # offset, v1, v2, v3, v4
print (header)
payload  = b'fps10'

byteObject = bytes(header)
print (byteObject)

client_program(byteObject, payload)
