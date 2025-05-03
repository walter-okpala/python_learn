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
        valor = float(input("Qual valor deseja depositar ?"))
        
        if valor <= 0:
            print("Não podem ser depositado valores negativos ou zerados")
        else: 
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if numero_saques < LIMITE_SAQUES:   
            
            if valor > limite:
                print(f"Operação não realizada, máximo permitido para saque é R$ {limite}")

            elif valor > saldo:
                print(f"Operação não realizada, valor de R${valor} é maior que saldo R$ {saldo}")
                
            else:
                 saldo -= valor
                 numero_saques += 1
                 extrato += f"Saque: R$ {valor:.2f}\n"    

        else: print(f"Número máximo de saques {LIMITE_SAQUES} já foram realizados ")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

