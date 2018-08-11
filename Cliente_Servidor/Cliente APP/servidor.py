import socket as s

def criarServidor(porta):
    socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    socket.bind(('', porta))
    socket.listen(1)

    print('O servidor está ativo...')
    
    try:
        connectionSocket, addr = socket.accept()
        connectionSocket.settimeout(30)

        msg = connectionSocket.recv(1024)
        print('\nMensagem recebida: {}\n\n'.format(msg.decode('utf-8')))
    except Exception:
        print('Erro no servidor')

    print('O servidor será encerrado.')
    socket.close()
