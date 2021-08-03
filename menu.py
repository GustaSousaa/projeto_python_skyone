from projeto_python_skyone.cadastro_de_squad import *


print('\n-==-=-=-=-=-=-=-=-=-=-Sky.One Solutions=-=-=-=-=-=-=-=-=-=-')
print('Bem vindo ao sistema de cadastro de squads!\n')
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

    while True:
        nome_dev = input('\nNome do desenvolvedor: ')
        fone_dev = input('Telefone do desenvolvedor: ')
        cargo_dev = input('Cargo do desenvolvedor: ')
        dev = Dev(nome_dev, fone_dev, cargo_dev)
        dev.incluir_squad(squad)
        squad.incluir_dev(dev)

        option = input('Deseja adicionar mais um dev [S/N]: ')
        if option in 'Nn':
            break

    option = input('\nDeseja adicionar mais Squad [S/N]: ')
    if option in 'Nn':
        break

print('\n-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('\nSquads cridas:     ')
for squad in squads:
    print(f'\n------------------------------{squad.nome}------------------------------')
    print(f'TechLead: {squad.techlead.nome}')
    print('\n-------Devs do squad-------')
    for dev in squad.devs:
        dev.exibir()
    print(f'------------------------------{squad.nome}------------------------------')

print('\n-==-=-=-=-=-=-=-=-=-=-Sky.One Solutions=-=-=-=-=-=-=-=-=-=-')