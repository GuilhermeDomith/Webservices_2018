from cliente import SocketCliente
from modelos import Turma, Aluno
from threading import Thread
import servidor as ss
import json

def main():
    Thread(target=ss.criarServidor, args=(27000, ), name="Servidor", daemon=False).start()

    aluno1 = Aluno('João', True)
    aluno2 = Aluno('Maria', True)
    aluno3 = Aluno('José', False)

    aluno4 = Aluno('Carla', True)
    aluno5 = Aluno('Ana', True)

    turma1 = Turma('DAW', 2018, [aluno1, aluno2, aluno3])
    turma2 = Turma('SOD', 2018, [aluno4, aluno5])

    turmas = {'turmas':[ turma1.to_json(), turma2.to_json()]}
    mensagem = json.dumps(turmas)
    
    socket = SocketCliente()
    socket.connect()
    socket.send(mensagem.encode('utf-8'))
    socket.close()

if __name__ == '__main__':
    main()
