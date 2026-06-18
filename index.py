def main():
    usuarios = []

    while True:

        print("\n--- Dapper Finanças ---")
        print("1 - Cadastrar Conta")
        print("2 - Acessar")
        print("3 - Encerrar")

        escolha = int(input("\nEscolha uma opção: "))

        if escolha == 1:

            usuario = input("Cadastre o usuário: ")
            senha = input("Crie uma senha: ")

            usuarios.append([usuario, senha, 131, 100])

            print("Cliente cadastrado com sucesso!")

        elif escolha == 2:

            tentativas = 0

            while tentativas < 3:

                usuario_digitado = input("\nUsuário: ")
                senha_digitada = input("Senha: ")


                indice_usuario = -1

                 
                for i in range(len(usuarios)):

                    if (usuarios[i][0] == usuario_digitado and
                            usuarios[i][1] == senha_digitada):

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

        match opcao:

            case 1:
                menuFatura(usuarios, indice_usuario)
                limparTela()

            case 2:
                menuCompra(usuarios, indice_usuario)
                limparTela()

            case 3:
                menuLimite(usuarios, indice_usuario)
                limparTela()

            case 4:
                menuRetornar()
                continuar = False

            case _:
                print("Opção inválida!")

def menuFatura(usuarios, indice_usuario):

    print("===================================")
    print("==             FATURA             ==")
    print("===================================")

    fatura = usuarios[indice_usuario][2]

    print(f"Fatura: R$ {fatura:.2f}")

def menuCompra(usuarios, indice_usuario):

    print("===================================")
    print("==            COMPRA             ==")
    print("===================================")

    valor = float(input("Digite o valor da compra: R$ "))

    if valor <= 0:

        print("Valor inválido")

    else:

        usuarios[indice_usuario][2] += valor

        print("Compra realizada com sucesso")
        print(f"Fatura: R$ {usuarios[indice_usuario][2]:.2f}")

def menuLimite(usuarios, indice_usuario):

    print("===================================")
    print("==         MOSTRAR LIMITE        ==")
    print("===================================")

    limite = usuarios[indice_usuario][3]

    print(f"Limite: R$ {limite:.2f}")

def menuRetornar():

    print("Encerrar Sistema Solicitado")

def limparTela():

    for i in range(15):
        print()

main()