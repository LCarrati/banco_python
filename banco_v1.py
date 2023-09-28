menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Quanto deseja depositar? "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

    elif opcao == "s":
        valor = float(input("Quanto deseja sacar? "))
        if valor > 0 and valor <= limite and numero_saques < LIMITE_SAQUES:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: {valor:.2f}\n"
            print(f"Saque de {valor:.2f} realizado com sucesso!")
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
        

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print(extrato)
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
