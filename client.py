# -*- coding: utf-8 -*-
import sys
import socket

# host = socket.gethostbyname('lightson.dip.jp')
host = socket.gethostbyname('localhost')
# host = '133.14.234.245'
# host = '133.20.178.81'
port = 4000
print(len(sys.argv))
if len(sys.argv) > 1:
    port = int(sys.argv[1])

so = socket.socket()
so.connect((host, port))
json_data = '{"SSIDs":["TDU_MRCL_WLAN_DOT1X","TDU_MRCL_WLAN","eduroam","TDU_MRCL_GUEST","Buffalo-G-3658"], "twitterID":"ざっぷ"}'
so.send(json_data.encode('UTF-8'))

data = []
while True:
    message = so.recv(8192)
    if not message:
        break
    print(message)
    data.append(message)
so.close()

data = ''.join(data)
print(data)
