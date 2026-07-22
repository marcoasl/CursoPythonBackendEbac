class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        print(f"O animal emitiu um som genérico.")


class Cachorro(Animal):
    def emitir_som(self):
        print(f"A {self.nome} de {self.idade} anos latiu!")

class Gato(Animal):
    def emitir_som(self):
        print(f"A {self.nome} de {self.idade} anos miou!")

lana = Cachorro("Lana", 2)
quiqui = Gato("quiqui", 3)

lana.emitir_som()
quiqui.emitir_som()


