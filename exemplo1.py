class endereco: #nome da classe#
    def __init__(self,rua,cidade): #atributo#
        self.rua = rua
        self.cidade = cidade

    def mostrar_endereco(self):#metodos#
        return f"{self.rua}{self.cidade}"

class Pessoa:
    def __init__(self,nome,endereco):
        self.nome = nome 
        self.endereco = endereco

    def mostrar_informacoes(self):
        return f"{self.nome} mora em {self.endereco.mostrar_endereco()}" 
    
endereco_maria = endereco("Av. Principal"," São Paulo")
maria = Pessoa("maria", endereco_maria)
print(maria.mostrar_informacoes())