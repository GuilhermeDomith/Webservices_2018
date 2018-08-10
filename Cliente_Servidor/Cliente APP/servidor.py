import socket as s

def criarServidor(porta):
    socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    socket.bind(('', porta))
    socket.listen(1)

    print('O servidor esta ouvindo')

    while True:
        try:
            connectionSocket, addr = socket.accept()
            print('Aguardando...')
            connectionSocket.settimeout(60)

            msg = connectionSocket.recv(1024)
            print(msg)
        except Exception as e:
            break

    print('O servidor será encerrado.')
    serverSocket.close()
