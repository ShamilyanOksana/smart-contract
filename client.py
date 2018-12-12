import socket
import pickle

text = b''
with open('text.txt', 'rb') as f:
    for i in f:
        text += i

text = pickle.dumps(text)

sock = socket.socket()
host = socket.gethostname()
port = 5050
sock.connect((host, port))
sock.send(text)
