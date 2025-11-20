cadastro_paciente = []

# Aqui a função dados_coleta vai me coletar o nome, idade e telefone do paciente
def dados_coleta():
    nome = input('Nome: ')
    idade_soma = 0

    while True:
        idade_edit = input('Idade: ')
        if idade_edit.isdigit():
            idade = int(idade_edit)
            break
        else:
            print("Este campo aceita somente números!")

    while True:
        telefone_edit = input('Telefone: ')
        if telefone_edit.isdigit():
            telefone = int(telefone_edit)
            break
        else:
            print("Este campo aceita somente números!")

    idade_soma += idade
    cadastro_paciente.append({
        'Nome': nome,
        'Idade': idade,
        'Telefone': telefone
    })

    return idade_soma

# Variáveis que vou usar ao decorrer do tempo
total1 = 0
total2 = 0
opcao = 0
contador = 0
idade_total = 0

# Meu sistema Clínica +Saúde'
while True:

    print("=" * 30)
    print('    SISTEMA CLÍNICA +SAÚDE')
    print("=" * 30)
    print('1 - Cadastrar paciente')
    print('2 - Ver estatísticas')
    print('3 - Buscar paciente')
    print('4 - Listar todos os pacientes')
    print('5 - Sair')
    print('-' * 20)

    # Aqui o usuário escolhe uma das opções acima
    escolha = int(input('Escolha uma opção: '))

    # A primeira opção chama a função dados_coleta
    if escolha == 1:
        idade_total += dados_coleta()
        print('')
        print('Paciente cadastrado com sucesso!')
        print('')
        contador += 1

        continue

    # Mostra as estatísticas mencionadas no enunciado
    elif escolha == 2:

        print('')
        print(f'Número total de pacientes cadastrados: {contador}')
        print('')
        if contador > 0:
            print(f'Idade média dos pacientes cadastrados: {(idade_total / contador):.2f}')
        else:
            print("Nenhum paciente cadastrado ainda!")
        print('')
        if contador > 0:
            paciente_velho = cadastro_paciente[0]
            paciente_novo = cadastro_paciente[0]

            for p in cadastro_paciente:
                if p['Idade'] > paciente_velho['Idade']:
                    paciente_velho = p
                if p['Idade'] < paciente_novo['Idade']:
                    paciente_novo = p

            print(f"O paciente mais velho é: {paciente_velho['Nome']} de {paciente_velho['Idade']} anos")
            print('')
            print(f"O paciente mais novo é: {paciente_novo['Nome']} de {paciente_novo['Idade']} anos")
            print('')

    # Opção para fazer busca de paciente
    elif escolha == 3:

        campo_de_busca = input('Qual o nome do paciente que você quer buscar? ').strip()

        encontrado = False

        for b in cadastro_paciente:

            if b['Nome'].lower() == campo_de_busca.lower():
                print("\nPaciente encontrado:")
                print('')
                print(f"Nome: {b['Nome']}")
                print(f"Idade: {b['Idade']}")
                print(f"Telefone: {b['Telefone']}")
                print('')
                encontrado = True

        if not encontrado:
            print("\nERRO! O paciente mencionado não foi encontrado!")
            print('')

        continue

    # Lista todos os pacientes cadastrado no sistema
    elif escolha == 4:
        print('')
        print('LISTA DE TODOS OS PACIENTES CADASTRADOS:')
        print('')
        for l in cadastro_paciente:
                print('-'*15)
                print(f"Nome: {l['Nome']}")
                print(f"Idade: {l['Idade']}")
                print(f"Telefone: {l['Telefone']}")
        print('-'*15)
        print('')
        continue

    # Para o sistema
    elif escolha == 5:
        break

    else:
        print('')
        print('Escolha apenas uma das opções da lista!')
        print('')
        continue

print(' ')

print("=" * 30)
print(' ')
print(f'PROGRAMA ENCERRADO!')