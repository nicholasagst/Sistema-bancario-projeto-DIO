menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
valores_depositados = 0
extrato = ""


while True:

    opcao = input(menu)

    if opcao == "1":
        print("Depósito")
        valor_deposito = float(input("Digite o valor que deseja depositar: "))
        saldo += valor_deposito
        print(f"Valor de R${valor_deposito} depositado com sucesso!")
        valores_depositados += valor_deposito
        extrato = f'Limite disponível R${saldo:.2f}\nValores depositados nesta conta R${valores_depositados}\nNúmero de saques realizados {numero_saques}\nObs:(Lembrando que o limite de saques diário é de {LIMITE_SAQUES} saques'

    elif opcao == "2":
        if numero_saques < LIMITE_SAQUES:
            print("Saque")
        
            valor_saque = float(input("Digite o valor de saque: "))
            
            if valor_saque <= limite:
        
                if valor_saque <= saldo:
            
                    print(f"Saque de R${valor_saque} permitido. Porfavor retire seu dinheiro abaixo! ")
                    saldo -= valor_saque
                    numero_saques += 1
                    extrato = f'Limite disponível R${saldo:.2f}\nValores depositados nesta conta R${valores_depositados}\nNúmero de saques realizados {numero_saques}\nObs:(Lembrando que o limite de saques diário é de {LIMITE_SAQUES} saques'
                else:
                    print("Saldo indisponível em conta! Tente novamente.")
            else:
                print(f"Valor digitado de R${valor_saque} ultrapassa o limite de saque diário que é de R${limite} por saque. Tente novamente!")
        else:
            print("Desculpe, você ultrapassou o limite de saques diários")
            

    elif opcao == "3":
        print("Extrato")
        print(extrato)

    elif opcao == "0":
        print("Obrigado por usar a NickBank!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")