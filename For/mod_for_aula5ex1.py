qtnd_hospedes = int(input('Quantas pessoas irão ficar no quarto? '))
quarto = []
for i in range(qtnd_hospedes):
    nome = input('Qual o nome da pessoa {} ? '.format(i))
    cpf = input('Qual o CPF da pessoa {} ? '.format(i))
    hospede = [nome, cpf]
    quarto.append(hospede)
print(quarto)