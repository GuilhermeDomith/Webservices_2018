import socket as s

def enviarParaServidor(porta):
    socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    socket.settimeout(20)

    while True:
        try:
            socket.connect(('127.0.0.3', porta))
            break
        except:
            continue

    socket.send(entrada.encode('utf-8'))
