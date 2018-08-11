import socket as s

class SocketCliente(s.socket):
    
    def __init__(self):
        super().__init__(s.AF_INET, s.SOCK_STREAM)
        super().settimeout(30)

    
    def connect(self, address=('127.0.0.1', 27000)):
        return super().connect(address)
