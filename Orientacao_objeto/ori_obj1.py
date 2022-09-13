# Criando nossa 1ª Classe em Python
# Sempre que você quiser criar uma classe, você vai fazer:
#
# class Nome_Classe:
#
# Dentro da classe, você vai criar a "função" (método) __init__
# Esse método é quem define o que acontece quando você cria uma instância da Classe
#
#"self" serve para acessar o parâmetro/atributo de determinada classe
#
#tv_sala.mudar_canal() --> Com parênteses, indica que está pegando um método
#tv_sala.cor = 'branca' --> Sem parênteses, indica que está pegando um atributo

class TV:
    cor = 'preta' #Deixa um valor fixo para o atributo da classe inteira

    def __init__(self, tamanho): #Ao add um parâmetro no init, é obrigatório declarar o valor dele
        self.ligada = False
        self.tamanho = tamanho      #Atributos
        self.canal = 'Netflix'
        self.volume = 10

    def mudar_canal(self, novo_canal):      #método
        self.canal = novo_canal
        #print('Canal alterado para {}.'.format(novo_canal))


tv_sala = TV(tamanho=55)
tv_quarto = TV(tamanho=70)

#print(tv_sala.tamanho)
#print(tv_quarto.tamanho)

#TV.cor = 'Branco' #Modifica a cor de toda a classe TV

print(tv_sala.cor)
print(tv_quarto.cor)

#tv_sala.mudar_canal('Globo') #Com parênteses, indica que está pegando um método
#tv_quarto.mudar_canal('Youtube')



#tv_sala.cor = 'branca' #Sem parênteses, indica que está pegando um atributo

#print(tv_sala.cor)
#print(tv_quarto.cor)

#tv_quarto.tamanho = 30

#print(tv_sala.tamanho)
#print(tv_quarto.tamanho)
