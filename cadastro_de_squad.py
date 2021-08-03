
class Pessoa:
    def __init__(self,nome, fone ):
        self.nome = nome
        self.fone = fone

    def exibir(self):
        print(f'-> {self.nome} - {self.fone}')

class Squad:
    def __init__(self, nome, techlead=None, devs=None):
        self.nome = nome
        self.devs = []
        self.techlead = techlead

    def incluir_dev(self, dev):
        self.devs.append(dev)

    def incluir_techlead(self,techlead):
        self.techlead = techlead

class Colaborador(Pessoa):
    def __init__(self, nome,fone, squad=None):
        super().__init__(nome, fone)
        self.squad = squad

    def incluir_squad(self,squad):
        self.squad = squad

class Dev(Colaborador):
    def __init__(self, nome, fone, cargo, squad=None):
        super().__init__(nome, fone, squad)
        self.cargo = cargo

    def exibir(self):
        super().exibir()
        print(f'   Cargo de {self.cargo} na squad {self.squad.nome}\n')