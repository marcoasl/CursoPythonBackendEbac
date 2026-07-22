while True:
 print("Escolha a operação")
 print("1 - Soma")
 print("2 - Subtração")
 print("3 - Multiplicação")
 print("4 - Divisão")
 print("5 - Sair")

 opcao = input("Digite o número da operação desejada: ")
 num1 = float(input("Digite o primeiro número: "))
 num2 = float(input("Digite o segundo número: "))
 if opcao == "5":
        print("Saindo do programa...")
        break

 if opcao == "1":
    print("Resultado:", num1 + num2)
    input("\nPressione Enter para tentar novamente...")
 elif opcao == "2":
    print("Resultado:", num1 - num2)
    input("\nPressione Enter para tentar novamente...")    
 elif opcao == "3":
    print("Resultado:", num1 * num2)
    input("\nPressione Enter para tentar novamente...")    
 elif opcao == "4":
    if num2 == 0:
        print("Erro: Não é possível dividir por zero.")
        input("\nPressione Enter para tentar novamente...")   
    else:
        print("Resultado:", num1 / num2)
        input("\nPressione Enter para tentar novamente...")    
 else:
    print("Erro: Opção inválida.")
    input("\nPressione Enter para tentar novamente...")     