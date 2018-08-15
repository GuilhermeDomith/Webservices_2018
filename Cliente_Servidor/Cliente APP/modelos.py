
class Turma:
    _num_turmas = 0

    def __init__(self, curso=None, ano=None, alunos=[]):
        Turma._num_turmas += 1
        self._id = Turma._num_turmas
        self.ano = ano
        self.curso = curso
        self.alunos = alunos

    def id(self):
        return self._id

    def to_dict(self):
        return {'id': self._id, 'ano': self.ano, 'curso': self.curso, 'alunos': [a.to_dict() for a in self.alunos]}

    def __str__(self):
        alunos = '\n\n'.join([str(a) for a in self.alunos])
        return 'id: {t._id}\ncurso: {t.curso}\nano: {t.ano}\nalunos: [\n\n{a}]\n'.format(t=self, a=alunos)
    
    @staticmethod
    def num_turmas():
        return Turma._num_turmas


class Aluno:
    _num_alunos = 0

    def __init__(self, nome=None, matriculado=False):
        Aluno._num_alunos += 1
        self._id = Aluno._num_alunos
        self.nome = nome
        self.matriculado = matriculado

    def id(self):
        return self._id

    def to_dict(self):
        return {'id': self._id, 'nome': self.nome, 'matriculado': self.matriculado}

    def __str__(self):
        return 'id: {a._id}\nnome: {a.nome}\nmatriculado: {a.matriculado}'.format(a=self)

    @staticmethod
    def num_alunos():
        return Aluno._num_alunos
