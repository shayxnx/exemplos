class Gato:
    def __init__(self, nome, cor, idade):
        self.nome = nome
        self.cor = cor
        self.idade = idade
        self.fome = True  # Inicializa com fome

    def miar(self):
        print(f"{self.nome} (cor {self.cor}) diz: Miau!")

    def comer(self):
        if self.fome:
            print(f"{self.nome} está comendo.")
            self.fome = False
        else:
            print(f"{self.nome} já está cheio.")

# Criando os gatos com nome, cor e idade
gato1 = Gato("Menino", "preto", 2)
gato2 = Gato("Akali", "frajolinha", 3)
gato3 = Gato("Nala", "tricolor", 1)

print("---")

gato2.miar() 
gato3.comer()


