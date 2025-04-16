menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Usuário
[5] Criar Conta
[6] Encontre sua conta
[0] Sair

=> """

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
valores_depositados = 0
extrato = ""
usuarios = []
AGENCIA = "0001"
contas_cadastradas = []
conta = 0



def deposito(saldo, extrato, valores_depositados, numero_saques, LIMITE_SAQUES,/):
    print('Depósito')
    valor_de_deposito = float(input("Digite o valor que deseja depositar: "))
    saldo += valor_de_deposito
    print(f"Valor de R${valor_de_deposito:.2f} depositado com sucesso!")
    valores_depositados += valor_de_deposito
    extrato = f'Limite disponível R${saldo:.2f}\nValores depositados nesta conta R${valores_depositados:.2f}\nNúmero de saques realizados {numero_saques}\nObs:(Lembrando que o limite de saques diário é de {LIMITE_SAQUES} saques'
    return saldo, valores_depositados, extrato

def sacar(*,saldo, extrato, limite, numero_saques, LIMITE_SAQUES, valores_depositados):
    if numero_saques < LIMITE_SAQUES:
        print("Saque")
        valor_saque = float(input("Digite o valor que deseja sacar: "))
        if valor_saque <= limite:
            if valor_saque <= saldo:
                print(f"Saque de R$ {valor_saque:.2f} permitido. Favor retirar seu dinheiro na saída indicada.")
                saldo -= valor_saque
                numero_saques += 1
                extrato = (f'Limite disponível R${saldo:.2f}\nValores depositados nesta conta R${valores_depositados:.2f}\nNúmero de saques realizados {numero_saques}\nObs:(Lembrando que o limite de saques diário é de {LIMITE_SAQUES} saques')
            else:
                print("Saldo indisponível em conta! Tente Novamente.")    
        else:
            print(f"Valor digitado de R${valor_saque:.2f} ultrapassa o limite de saque diário que é de R${limite:.2f} por saque. Tente novamente!")    
    else:
        print("Desculpe, você ultrapassou o limite de saques diários")
    return saldo, extrato, numero_saques

def extrato_completo(extrato,/, *, saldo):
    print("Extrato")
    print(extrato)

def criar_usuario(usuarios):
    print("Criar Usuário!")
    nome = input("Digite seu nome completo: ")
    data_nascimento  = input("Digite sua data de nascimento(ex: 01-01-2000): ")
    cpf = int(input("Digite seu CPF.(Apenas numero ex: 12345678900): "))
    endereco = input("Digite seu endreço (conforme exemplo: Logradouro, número - bairro - cidade/sigla estado): ")
    usuario = {"nome":nome, "data_nascimento":data_nascimento, "cpf": cpf, "endereco":endereco}
    usuarios.append(usuario)
    print("Usuário criado com sucesso!")
    return usuarios

def criar_conta(usuarios,conta, contas_cadastradas):
    cpf = int(input("Digite seu CPF(exe: 12345678900): "))
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            conta +=1
            conta_cadastrada = {"nome":usuario['nome'], "cpf":usuario['cpf'], "conta": conta}
            contas_cadastradas.append(conta_cadastrada)
            cadastro_sucesso = f"\nConta criada com sucesso!\nCliente: {usuario['nome']}\nCPF: {usuario['cpf']}\nAgência: {AGENCIA}\nConta: {conta}"
            print(cadastro_sucesso)
            return conta, contas_cadastradas
        
    print("Usuário não encontrado. Realize o cadastro!")
    return conta, contas_cadastradas

def listar_contas(contas_cadastradas, conta):
    print("Se você já possui uma conta, verifique aqui!")
    cpf = int(input("Digite seu CPF (ex: 12345678900): "))
    encontrado = False  

    for usuario in contas_cadastradas:
        if usuario['cpf'] == cpf:
            print(f"\nConta vinculada ao usuário encontrada!")
            print(f"Cliente: {usuario['nome']}")
            print(f"CPF: {usuario['cpf']}")
            print(f"Agência: {AGENCIA}")
            print(f"Conta: {usuario['conta']}")
            encontrado = True

    if not encontrado:
        print("\nNão há nenhuma conta vinculada a este CPF.")
        print("Considere criar uma conta ou verifique se você possui uma conta de usuário cadastrada.")

    return contas_cadastradas, conta
  


while True:

    opcao = input(menu)

    if opcao == "1":
       saldo,valores_depositados, extrato = deposito(saldo, extrato, valores_depositados, numero_saques, LIMITE_SAQUES)

    elif opcao == "2":
        saldo, extrato, numero_saques = sacar(
            saldo = saldo,
            extrato = extrato,
            limite = limite,
            numero_saques = numero_saques,
            LIMITE_SAQUES = LIMITE_SAQUES,
            valores_depositados = valores_depositados
        )
            

    elif opcao == "3":
       mostrar_extrato = extrato_completo(extrato, saldo = saldo)
    
    elif opcao == "4":
       usuarios = criar_usuario(usuarios)
        
    elif opcao == "5":
       conta, contas_cadastradas = criar_conta(usuarios,conta, contas_cadastradas)

    elif opcao == "6":
       contas_cadastradas, conta = listar_contas(contas_cadastradas,conta)    

    elif opcao == "0":
        print("Obrigado por usar a NickBank!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")