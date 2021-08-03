from projeto_python_skyone.cadastro_de_squad import *

while True:
    squads = []
    nome_squad = input ('\nNome da Squad: ')
    nome_techlead = input ('Nome do techlead da squad: ')
    fone_techlead = input ('Telefone do techlead: ')

    squad = Squad(nome_squad)
    techlead = Colaborador(nome_techlead, fone_techlead)
    squad.incluir_techlead(techlead)
    techlead.incluir_squad(squad)

    squads.append(squad)

    nome_dev = input('\nNome do desenvolvedor: ')

    option = input('\nDeseja adicionar mais Squad [S/N]: ')
    if option in 'Nn':
        break