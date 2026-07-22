def adicionar_produto(estoque, nome, quantidade, preco):
    nome = nome.strip()
    if nome in estoque:
        return "Erro: Produto já cadastrado."
    else:
        estoque[nome] = {"quantidade": quantidade, "preço": preco}
        return f"Produto '{nome}' adicionado com sucesso!"
    
def listar_produtos(estoque):
    if not estoque:
        return "Nenhum produto cadastrado."
    else:
        resultado = ["Lista de produtos:"]
        for nome, dados in sorted(estoque.items(), key=lambda x: x[0]):
            resultado.append(f"{nome}: Quantidade disponível - {dados['quantidade']} | Preço - R${dados['preço']:.2f}")
        return "\n".join(resultado)
    
def remover_produto(estoque, nome):
    nome = nome.strip()
    if nome in estoque:
        del estoque[nome]
        return f"Produto '{nome}' removido com sucesso!"
    else:
        return "Erro: Produto não encontrado."
    
def atualizar_quantidade(estoque, nome, nova_qtd):
    nome = nome.strip()
    if nome in estoque:
        estoque[nome]["quantidade"] = nova_qtd
        return f"Quantidade do produto '{nome}' atualizada para {nova_qtd}."
    else:
        return "Erro: Produto não encontrado."

def exibir_menu():
    return ( 
        "\n--- MENU ESTOQUE ---\n"
        "1 - Adicionar produto\n"
        "2 - Listar produtos\n"
        "3 - Remover produto\n"
        "4 - Atualizar quantidade\n"
        "5 - Sair\n"
        "Escolha uma opção: "
    )

def main():
    estoque = {}
    while True:
        opcao = input(exibir_menu()).strip()
        
        if opcao == "1":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            resposta = adicionar_produto(estoque, nome, quantidade, preco)
            print(resposta)

        elif opcao == "2":
            print(listar_produtos(estoque))

        elif opcao == "3":
            nome = input("Nome do produto a remover: ")
            print(remover_produto(estoque, nome))

        elif opcao == "4":
            nome = input("Nome do produto para atualizar: ")
            nova_qtd = int(input("Nova quantidade: "))
            print(atualizar_quantidade(estoque, nome, nova_qtd))

        elif opcao == "5":
            print("Saindo do programa... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()