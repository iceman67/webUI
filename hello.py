from flask import Flask
from flask import render_template
from flask import request

import array
import struct
import socket
import binascii
from struct import pack, unpack, calcsize

from webUI_server import RCV_HEADER_SZ

app = Flask(__name__)

# call cfg
@app.route("/")
def hello_world(name=None):
    return render_template('index.html', name=name)

host = "127.0.0.1"  # as both code is running on same pc
port = 8700  # socket server port number

RCV_HEADER_SZ=4
SND_HESDER_SZ=8

def client_program(header, payload):
   
    client_socket = socket.socket()  # instantiate
    # connect SERVER
    client_socket.connect((host, port))  # connect to the server
    # send header (8byte) and payload
    client_socket.sendall (header)  # send message
    client_socket.sendall (payload)  # send message

    # receive 4byte
    data = client_socket.recv(RCV_HEADER_SZ) # receive response
    print (data)
    recv = unpack('<i',data) # recv has a tuple with a number
    return recv[0]

# render the response of configuration
@app.route('/cfg')
def fps(value=None):
    value = request.args.get('fps')

    header = bytearray(SND_HESDER_SZ)
    fmt_str = "<BBBBi"
    struct.pack_into(fmt_str, header, 0, 0x01, 0x12, 0xff,0, 5) # offset, v1, v2, v3, v4(sz of payload)
    byteObject = bytes(header)
    payload  = b'fps' + value.encode()
    value  = client_program(byteObject, payload)
    return render_template('hello.html', fps=value)

