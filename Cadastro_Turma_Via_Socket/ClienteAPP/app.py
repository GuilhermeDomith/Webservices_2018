from cliente import SocketCliente
from modelos import Turma, Aluno
from threading import Thread
import json


def main():
    turmas = cadastrarTurmas()
    turmasDict = {'turmas': [turma.to_dict() for turma in turmas]}
    mensagemJson = json.dumps(turmasDict)
    enviarMensagem(mensagemJson)

def cadastrarTurmas():
    turmas = []
    while True:
        turma = Turma(alunos=[])

        print()
        turma.curso = entrada('\tNome do Curso: ').upper()
        turma.nome = entrada('\tNome da Turma: ').upper()

        while True:
            turma.ano = entrada('\tAno da turma: ')
            if str(turma.ano).isdigit():
                break

        print('\n\t**Alunos da turma {} {}**\n'.format(turma.nome,turma.ano))
        while True:
            aluno = Aluno()
            aluno.nome = entrada('\tNome do %dº aluno: ' %(len(turma.alunos)+1)).upper()
            matriculado = entrada('\tAluno esta matriculado? (s-sim | n-não): ', 's', 'n')
            aluno.matriculado = matriculado == 's' if True else False
            turma.alunos.append(aluno)

            if entrada('\t*Cadastrar mais alunos na turma? (s-sim | n-não)*: ', 's', 'n') == 'n':
                break
            print()

        turmas.append(turma)
        if entrada('\t*Cadastrar mais turmas? (s-sim | n-não)*: ', 's', 'n') == 'n':
            break
        print()

    return turmas


def entrada(mensagem, *opcoes):

    while True:
        entrada = input(mensagem)

        if opcoes:
            if opcoes.__contains__(entrada):
                return entrada
        elif entrada:
            return entrada


def enviarMensagem(mensagem):
    socket = SocketCliente()
    try:
        socket.connect()
        socket.send(mensagem.encode('utf-8'))
        socket.send("\nexit".encode('utf-8'))
        print('\nOs dados foram enviados para cadastro.')
    except:
        pass
    
    socket.close()


if __name__ == '__main__':
    main()
