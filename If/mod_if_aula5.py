meta = 1000
vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700

if vendas_funcionario1 >= meta :
    bonus1 = vendas_funcionario1 * 0.10
    print('O funcionário 1 ganhou {:.0f} de bônus.'.format(bonus1))
else :
    print('O funcionário 1 ganhou 0 de bônus.')
if vendas_funcionario2 >= meta :
    bonus2 = vendas_funcionario2 * 0.10
    print('O funcionário 2 ganhou {:.0f} de bônus.'.format(bonus2))
else :
    print('O funcionário 2 ganhou 0 de bônus.')
if vendas_funcionario3 >= meta :
    bonus3 = vendas_funcionario3 * 0.10
    print('O funcionário 3 ganhou {:.0f} de bônus.'.format(bonus3))
else:
    print('O funcionário 3 ganhou 0 de bônus.')


