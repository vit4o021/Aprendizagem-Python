cpf = input('Insira seu CPF (Digite apenas números): ')

#tratar CPF
#retirar espaços
cpf = cpf.strip()
#retirar pontos
cpf = cpf.replace('.' , '')
#retirar traços
cpf = cpf.replace('-' , '')

if len(cpf) == 11 and cpf.isnumeric():
    print(cpf)
else:
    print('Digite seu CPF corretamente e digite apenas números!')

