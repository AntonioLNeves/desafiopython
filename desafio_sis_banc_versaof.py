menu = """
================ MENU ================

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==> """

saldo = 0
limite = 500
extrato = ""
qtde_saque = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Valor do saldo: R$ {valor:.2}\n"

        else:
            print("Falha na operação! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor desejado para saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = valor > qtde_saque >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha na operação! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Falha na operação! O valor do saque excedeu o limite atual.")

        elif excedeu_saques:
            print("Falha na operação! A quantidade máxima de saques foi excedida.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            qtde_saque += 1

        else:
            print("Falha na operação! O valor informado é inválido.")

    elif opcao == "e":
            print("\n================ EXTRATO ================")
            print("Nenhuma movimentação realizada." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")

    elif opcao == "q":
            print("Obrigado por utilizar nossos serviços! É um prazer te ter como cliente.")
            break
            

    else:
            print("Falha na operação, por favor selecione novamente a operação desejada.")
