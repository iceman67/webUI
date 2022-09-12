from flask import Flask
from flask import render_template
from flask import request

import array
import struct
import socket
import binascii
from struct import pack, unpack, calcsize

app = Flask(__name__)

# call cfg
@app.route("/")
def hello_world(name=None):
    return render_template('index.html', name=name)

def client_program(header, payload):
    host = "127.0.0.1"  # as both code is running on same pc
    port = 8700  # socket server port number
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    client_socket.sendall (header)  # send message
    client_socket.sendall (payload)  # send message

    # receive 4byte
    data = client_socket.recv(4) # receive response
    print (data)
    recv = unpack('<i',data) # bytes to hex => string
    return recv[0]

# render the response of configuration
@app.route('/cfg')
def fps(value=None):
    value = request.args.get('fps')

    header = bytearray(8)
    fmt_str = "<BBBBi"
    struct.pack_into(fmt_str, header, 0, 0x01, 0x12, 0xff,0, 5) # offset, v1, v2, v3, v4
    byteObject = bytes(header)
    payload  = b'fps' + value.encode()
    value  = client_program(byteObject, payload)
    return render_template('hello.html', fps=value)

