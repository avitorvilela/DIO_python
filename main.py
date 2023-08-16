print("BANCO DIO $$$")

saldo = 0
OPCOES = [1, 2, 3, 4]

while True:
    print("""
[1] DEPOSITAR
[2] SACAR
[3] SALDO
[4] SAIR
""")

    opcao = int(input(">>> "))

    if opcao not in OPCOES:
        print("\nInsira uma opção válida.")

    if opcao == 1:
        deposito = int(input("\nQuanto deseja depositar? R$ "))
        saldo += deposito

    elif opcao == 2:
        saque = int(input("\nQuanto deseja sacar? R$ "))
        saldo -= saque

    elif opcao == 3:
        print(f"\nSeu saldo é: R$ {saldo}")

    elif opcao == 4:
        print("\nNós do BANCO DIO agradeçemos pela preferência!")
        break