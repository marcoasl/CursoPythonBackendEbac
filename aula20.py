operacoes = {
    1: lambda x, y: x + y,
    2: lambda x, y: x - y,
    3: lambda x, y: x * y,
    4: lambda x, y: x / y if y != 0 else "Erro" 
}

nomes_operacoes = ["Soma", "Subtração", "Multiplicação", "Divisão"]

def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Valor inválido! Por favor, insira apenas números.")

while True:
    print("\n CALCULADORA ")        

    # Entrada dos dois números com tratamento de exceção
    num1 = obter_numero("Insira o primeiro número: ")
    num2 = obter_numero("Insira o segundo número: ")
    
    # Menu dinâmico organizado com List Comprehension
    print("\nEscolha uma operação:")
    menu = [f"{i+1} - {nome}" for i, nome in enumerate(nomes_operacoes)]
    for opcao in menu:
        print(opcao)
        
    # Validação da escolha da operação
    while True:
        try:
            escolha = int(input("\nVocê escolheu: "))
            if escolha in operacoes:
                break
            else:
                print("Opção inválida! Escolha um número de 1 a 4.")
        except ValueError:
            print("Por favor, digite um número inteiro correspondente à opção.")

    # Tratamento específico para a Divisão por Zero
    if escolha == 4:
        while num2 == 0:
            print("Divisão por zero não é permitida.")
            num2 = obter_numero("Por favor, insira outro número (divisor): ")

    # Executa a operação usando a função lambda correspondente
    resultado = operacoes[escolha](num1, num2)
    print(f"\nO resultado é: {resultado}")
    
    # Pergunta se o usuário quer continuar
    continuar = input("\nDeseja realizar outra operação? (S/N): ").strip().upper()
    if continuar != 'S':
        print("Encerrando o programa. Até mais!")
        break 