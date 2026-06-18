import os  

ARQUIVO_DADOS = "dados_usuarios.txt"

def salvar_dados(usuarios):
    with open(ARQUIVO_DADOS, "w") as arquivo:
        for u in usuarios:
            linha = f"{u};{u[10]};{u[11]};{u[12]};{u[7]}\n"
            arquivo.write(linha) # [8]

def carregar_dados():
    usuarios = []

    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")
                usuario = dados
                senha = dados[10]
                fatura = float(dados[11])
                limite = float(dados[12])
                compras = eval(dados[7]) 
                usuarios.append([usuario, senha, fatura, limite, compras])
    return usuarios

def main():
    usuarios = carregar_dados()
    categorias = []

    while True:
        print("\n--- Dapper Finanças ---")
        print("1 - Cadastrar Conta")
        print("2 - Acessar")
        print("3 - Encerrar")

        escolha = int(input("\nEscolha uma opção: "))

        if escolha == 1:
            usuario = input("Cadastre o usuário: ")
            senha = input("Crie uma senha: ")

            usuarios.append([usuario, senha, 0, 100, []])
            
            salvar_dados(usuarios)
            print("Cliente cadastrado com sucesso!")

        elif escolha == 2:
            tentativas = 0
            while tentativas < 3:
                usuario_digitado = input("\nUsuário: ")
                senha_digitada = input("Senha: ")
                indice_usuario = -1
                 
                for i in range(len(usuarios)):
                    if (usuarios[i] == usuario_digitado and
                            usuarios[i][10] == senha_digitada):
                        indice_usuario = i
                        break

                if indice_usuario != -1:
                    print("\nAcesso permitido!")
                    menuInicial(usuarios, indice_usuario)
                    break
                else:
                    tentativas += 1
                    print("\nUsuário ou senha incorretos!")
                    print(f"Tentativas restantes: {3 - tentativas}")

            if tentativas == 3:
                print("Acesso bloqueado!")

        elif escolha == 3:
            salvar_dados(usuarios)
            print("Programa encerrado!")
            break
        else:
            print("Opção inválida!")

def menuInicial(usuarios, indice_usuario):
    continuar = True
    while continuar:
        print("===================================")
        print("==   Dapper Finanças  ==")
        print("===================================")
        print("==   1 - Consultar Fatura         ==")
        print("==   2 - Realizar Compra         ==")
        print("==   3 - Consultar Limite        ==")
        print("==   4 - Encerrar                ==")
        print("===================================")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            menuFatura(usuarios, indice_usuario)
            limparTela()
        elif opcao == 2:
            menuCompra(usuarios, indice_usuario)
            limparTela()
        elif opcao == 3:
            menuLimite(usuarios, indice_usuario)
            limparTela()
        elif opcao == 4:
            menuRetornar()
            continuar = False
        else:
            print("Opção inválida!")

def menuFatura(usuarios, indice_usuario):
    print("===================================")
    print("==             FATURA            ==")
    print("===================================")
    compras = usuarios[indice_usuario][7]
    total = 0
    if len(compras) == 0:
        print("Nenhuma compra realizada.")
        return
    print("Compras realizadas:\n")
    for compra in compras:
        print(f"Categoria: {compra['categoria']}")
        print(f"Valor: R$ {compra['valor']:.2f}")
        print("----------------------")
        total += compra['valor']
    print(f"\nTOTAL DA FATURA: R$ {total:.2f}")

def menuCompra(usuarios, indice_usuario):
    print("===================================")
    print("==            COMPRA             ==")
    print("===================================")
    valor = float(input("Digite o valor da compra: R$ "))
    categoria = str(input("Digite a categoria da compra (Ex.: Viagem): "))
    fatura = usuarios[indice_usuario][11]
    limite = usuarios[indice_usuario][12]

    if valor <= 0:
        print("Valor inválido")
    elif fatura + valor > limite:
        print("Compra recusada. Limite excedido.")
    else:
        usuarios[indice_usuario][11] += valor
        usuarios[indice_usuario][7].append({
            "categoria": categoria,
            "valor": valor
        })
        salvar_dados(usuarios)
        print("Compra realizada com sucesso")
        print(f"Fatura: R$ {usuarios[indice_usuario][11]:.2f}")

def menuLimite(usuarios, indice_usuario):
    print("===================================")
    print("==         MOSTRAR LIMITE        ==")
    print("===================================")
    limite = usuarios[indice_usuario][12]
    print(f"Limite: R$ {limite:.2f}")

def menuRetornar():
    print("Encerrar Sistema Solicitado")

def limparTela():
    for i in range(15):
        print()

main()
