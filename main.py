import os

# tuplas
chaves = ('Nome completo',
'Data de Nascimento',
'CPF',
'Profissão',
'Email',
'Endereço',
'Telefone')

usuarios = []

usuario = {}

os.system('cls')

while True:
    print('1 - Listar todos os usuários.')
    print('2 - Cadastrar novo usuário.')
    print('3 - Pesquisar usuário cadastrado.')
    print('4 - Alterar os dados do usuário.')
    print('5 - Excluir nome cadastardo.')
    print('6 - Sair do programa.')

    opcao = input('Opção do usuário: ')

    os.system('cls')
 
    match opcao:
        case '1':
            for usuario in usuarios:
                print('\n')
                for chave in chaves:
                    print(f'{chave}: {usuario[chave]}')
            continue
        case '2':
            for i in range(len(chaves)):
                usuario[chaves[i]] = input(f'Informe {chaves[i]}: ')
            usuarios.append(usuario)
            print(f'\nUsuário cadstrado com sucesso.')
            continue
        case '3':
            nome = input('Informe o nome que deseja procurar: ')
            for i in range(len(usuarios)):
                if nome in usuarios[i]['Nome completo']:
                    print(f'índice: {i + 1}')
                    print(f'Nome completo: {usuarios[i]['Nome completo']}')
                    print(f'Data de nascimento: {usuarios[i]['Data de Nascimento']}')
                    print(f'CPF: {usuarios[i]['CPF']}')
                    print(f'Profissão: {usuarios[i]['Profissão']}')
                    print(f'Email: {usuarios[i]['Email']}')
                    print(f'Endereço: {usuarios[i]['Endereço']}')
                    print(f'Telefone: {usuarios[i]['Telefone']}')
                else:
                    continue
        case '4':
            indice = int(input('Informe o índice a ser alterado: '))
            campo = input('Informe o nome do campo a ser alterado: ')
            indice -= 1
            try:
                usuarios[indice][campo] = input(f'Informe o novo valor do campo {campo}: ')
            except:
                print('Não foi possível alterar.')

            print(f'Novos dados do índice {indice + 1}:\n')
            print(f'Nome completo: {usuarios[indice]['Nome completo']}')
            print(f'Data de nascimento: {usuarios[i]['Data de Nascimento']}')
            print(f'CPF: {usuarios[i]['CPF']}')
            print(f'Profissão: {usuarios[i]['Profissão']}')
            print(f'Email: {usuarios[i]['Email']}')
            print(f'Endereço: {usuarios[i]['Endereço']}')
            print(f'Telefone: {usuarios[i]['Telefone']}')
            continue
        case '5':
            indice = int(input('Informe o índice a excluir: '))
            indice -= 1
            try:
                del[usuarios[indice]]
                print('Usuário excluído com sucesso.')
            except:
                print('Não foi possível excluir o nome.')
            finally:
                continue
        case '6':
            print('Programa encerrado ')
            break
        case _:
            print('Opção inválida')
            continue