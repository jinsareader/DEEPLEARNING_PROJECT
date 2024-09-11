import socket;
import threading;

class Mysocket :
    def __init__(self, sock=None):
        if sock is None :
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else :
            self.sock = sock;
    def connect(self, host, port) :
        self.sock.connect((host, port));
    def mysend(self, data) :
        self.sock.sendall(data);