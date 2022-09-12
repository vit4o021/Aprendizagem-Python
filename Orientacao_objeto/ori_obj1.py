# Criando nossa 1ª Classe em Python
# Sempre que você quiser criar uma classe, você vai fazer:
#
# class Nome_Classe:
#
# Dentro da classe, você vai criar a "função" (método) __init__
# Esse método é quem define o que acontece quando você cria uma instância da Classe
#
#"self" serve para acessar o parâmetro/atributo de determinada classe

class TV:
    def __init__(self):
        self.cor = 'preta'
        self.ligada = False
        self.tamanho = 55
        self.canal = 'Netflix'
        self.volume = 10
tv_sala = TV()
tv_quarto = TV()

tv_sala.cor = 'branca'

print(tv_sala.cor)
print(tv_quarto.cor)

tv_quarto.tamanho = 30

print(tv_sala.tamanho)
print(tv_quarto.tamanho)
