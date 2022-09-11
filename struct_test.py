from struct import pack, unpack, calcsize

# < little endian
# integer -> byte array
data = pack('<i', 5)
print(data)


# byte array -> integer
value= unpack('<i', data)
print(value[0])

#
data = pack('<Bi5s', 0x00, 5, b'fps10')
print(data)


# byte array -> integer
(header, number, payload)= unpack('<Bi5s', data)

print (header, " ", number, " ", payload.decode())

'''
value= unpack('<Bi5s', data)
print(value[0])  
print(value[1]) 
print(value[2][:]) 
'''
