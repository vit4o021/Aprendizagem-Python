nome = input('Digite seu nome: ')
email = input('Digite seu e-mail: ')

if nome and email :
    pos_arroba = email.find('@')
    ver_ponto = email[pos_arroba:]
    if pos_arroba != -1 and '.' in ver_ponto :
        print('Cadastro concluido')
    else:
        print('Preencha todos os dados corretamente!')
else:
    print('Preencha todos os dados corretamente!')
