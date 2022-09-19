#!/usr/bin/env python3
# http://weifan-tmm.blogspot.kr/2015/07/a-simple-turorial-for-python-c-inter.html
import sysv_ipc
import struct

BUFF_SIZE = 16

from type_definitions import *

if __name__ == '__main__':
    msg_string = "sample string\0"
    msg_double1 = 1234.56789
    msg_double2 = 9876.12345
    try:
        mq = sysv_ipc.MessageQueue(1234, sysv_ipc.IPC_CREAT)

        # string transmission
        mq.send(msg_string, True, type=TYPE_STRING)
        print(f"string sent: {msg_string}")

        # Two double transmission
        bytearray1 = struct.pack("d", msg_double1)
        bytearray2 = struct.pack("d", msg_double2)
        mq.send(bytearray1 + bytearray2, True, type=TYPE_TWODOUBLES)
        print(f"two doubles sent: {msg_double1}, {msg_double2}")


        # CFG message transmission
        header = bytearray(13)
        fmt_str = "<BBBBi5s" 
        # offset, v1, v2, v3, v4
        struct.pack_into(fmt_str, header, 0, 0x01, 0x12, 0xff,0, 5, b"fps10") 
        print (header)
        mq.send(header, True, type=TYPE_CFG)



    except sysv_ipc.ExistentialError:
        print("ERROR: message queue creation failed")


