import socket
import pickle

sock = socket.socket()
host = socket.gethostname()
port = 5050
sock.bind((host, port))
sock.listen(1)

while True:
    con, addr = sock.accept()
    data = con.recv(4096)
    if data:
        print(pickle.loads(data))
