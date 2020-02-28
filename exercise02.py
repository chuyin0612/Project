from socket import *
import struct

st = struct.Struct('i9sif')

s = socket(AF_INET, SOCK_DGRAM)
s.bind(("0.0.0.0", 8899))

f = open('student.txt', 'a')

while True:
    data, addr = s.recvfrom(1024)
    info = st.unpack(data)
    # 分数大于90进行打印
    if info[-1] >= 90:
        id, name, age, score = info
        name = name.decode().strip("\x00")
        message = "%d  %s  %d  %.2f\n" % (id, name, age, score)
        f.write(message)
        f.flush()
