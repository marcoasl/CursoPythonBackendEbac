import os

# Banco de dados temporário usando dicionário (chaves)
sistema_alunos = {}

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def adicionar_aluno():
    limpar_tela()
    print("=== CADASTRAR NOVO ALUNO ===")
    id_aluno = input("Digite a matrícula (ex: 101): ")
    
    if id_aluno in sistema_alunos:
        print("\n[Erro] Esta matrícula já existe!")
        input("\nPressione Enter para voltar...")
        return

    nome = input("Nome do aluno: ")
    try:
        nota1 = float(input("Nota do 1º Bimestre: "))
        nota2 = float(input("Nota do 2º Bimestre: "))
    except ValueError:
        print("\n[Erro] Digite apenas números para as notas!")
        input("\nPressione Enter para voltar...")
        return

    media = (nota1 + nota2) / 2
    status = "Aprovado" if media >= 6.0 else "Reprovado"

    # Usando chaves {} para criar a ficha do aluno
    sistema_alunos[id_aluno] = {
        "nome": nome,
        "notas": [nota1, nota2],
        "media": media,
        "status": status
    }
    print(f"\n[Sucesso] {nome} foi cadastrado!")
    input("\nPressione Enter para voltar...")

def listar_alunos():
    limpar_tela()
    print("=== LISTA DE ALUNOS CADASTRADOS ===")
    
    if not sistema_alunos:
        print("\nNenhum aluno cadastrado no momento.")
    else:
        for matricula, dados in sistema_alunos.items():
            print("-" * 40)
            print(f"Matrícula: {matricula}")
            print(f"Nome: {dados['nome']}")
            print(f"Notas: {dados['notas'][0]} e {dados['notas'][1]}")
            print(f"Média Final: {dados['media']:.1f}")
            print(f"Situação: {dados['status']}")
        print("-" * 40)
        
    input("\nPressione Enter para voltar...")

def menu_principal():
    while True:
        limpar_tela()
        print("====================================")
        print("    SISTEMA ESCOLAR PYTHON v1.0     ")
        print("====================================")
        print("[1] Cadastrar Aluno")
        print("[2] Listar Alunos")
        print("[3] Sair do Programa")
        print("====================================")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            print("\nEncerrando o sistema. Até logo!")
            break
        else:
            print("\n[Erro] Opção inválida!")
            input("\nPressione Enter para tentar novamente...")

# Inicia o programa completo
if __name__ == "__main__":
    menu_principal()