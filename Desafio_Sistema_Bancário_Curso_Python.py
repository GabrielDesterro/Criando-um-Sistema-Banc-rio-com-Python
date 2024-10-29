menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    print("\nSelecione a operação que deseja realizar")
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("\nDigite o valor que deseja depositar: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}\n"

        else:
            print("\nA operação falhou! O valor informado é inválido.")
    
    elif opcao == "2":
        
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("\nDigite o valor que deseja sacar: "))

            if valor <= limite:

                if valor <= saldo and valor > 0:
                    saldo -= valor
                    extrato += f"Saque: R$ {valor: .2f}\n"
                    numero_saques += 1
                
                elif valor < 0:
                    print("\nImpossível realizar a operação! O valor digitado é inválido.")

                elif valor > saldo:
                    print("\nImpossível realizar a operação! O valor digitado é maior que o saldo em conta.")
            
            else:
                print("\nImpossível Realizar a operação! O valor digitado é maior que o limite de saque.")

        else:
            print("\nImpossível realizar a operação! A quantidade máxima de saques diários já foi atingido.")

    elif opcao == "3":
        print("\n=====================EXTRATO=====================")
        print(f"\nNão foram realizadas operações!\n\nSaldo: R$ {saldo: .2f}\n" if not extrato else f"\nExtrato:\n{extrato} \nSaldo: R$ {saldo: .2f}\n")
        print("=================================================")
    
    elif opcao == "0":
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")