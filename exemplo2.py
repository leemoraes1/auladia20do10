class estudantes :
    def __init__(self,nome):
        self.nome = nome
class turma:
        def __init__(self,nome):
             self.nome = nome
             self.estudantes = []
        
        def adicionar_estudantes(self,estudantes):
             self.estudantes.append(estudantes)