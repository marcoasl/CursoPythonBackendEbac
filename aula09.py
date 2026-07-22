# Uma Classe"Class" é um molde.
# Vamos usar esse molde para construir coisas que queremos que tem um mesmo padrão

#  << molde >>
# - nome :
# - hp :
# - tipo "terra,fogo etc" :                     <<<<< este é o molde que sera usado para poder preencher igual abaixo as informaçoes a qual o molde pede e 
# - Quais seus ataques :                              voce passa as informaçoes somente
# - altura :
# - Peso :


# - nome : SHARIZARD
# - hp  : 500
# - tipo "terra,fogo etc"  : FOGO
# - Quais seus ataques  : BOLA DE FOGO
# - altura: 2,0 mt
# - Peso: 250 kg

# - nome : BULBASSAURO
# - hp  : 80
# - tipo "terra,fogo etc"  : AGUA
# - Quais seus ataques  : VORTEX AGUA
# - altura: 40 cm
# - Peso: 18 kg
class MoldePokemon:
    # __init__ é o metodo construtor "função"
    # Self é o item o qual tem a responsabilidade de armazenar e manipular essas informações dos "atributospokemon"
    def __init__(self, nome, hp, tipo, ataque, altura, peso):              #<< definindo atribuitos do molde "atributospokemon" 
        Self.nome = nome
        self.hp = hp
        self.tipo = tipo
        self.ataque = ataque
        sel.altura = altura
        self.peso = peso          
# Agora voce pode definir um novo metodo "mostrar_nome_pokemon" chamando somente o self que vai estar armazenando e manipulando essas informaçoes e atributos definidos acima.
    def mostrar_nome_pokemon(self):  # <<< nao vai precisar definir atributos igual ao decima pois o self ja esta organizando la encima essa e a função dele.
        print(f"O nome do meu pokemon é : {self.nome}") 

        # pronto agora ele chama o self em cada parametro do molde sem precisar definir o atributo ali encima juntamente com o self porque voce ja fez no molde ;