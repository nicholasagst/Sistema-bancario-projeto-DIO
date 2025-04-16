# 💰 NickBank - Simulador de Banco em Python

NickBank é um projeto simples em Python que simula o funcionamento básico de um sistema bancário, permitindo ao usuário realizar depósitos, saques e consultar o extrato da conta.

## 🧠 Funcionalidades

- Depósito de valores
- Saque com limite diário de R$500 por saque
- Limite de 3 saques diários
- Exibição de extrato com saldo e número de saques realizados
- Interface via terminal interativo
- Cadastro de usuários com CPF, nome completo, data de nascimento e endereço
- Criação de contas bancárias vinculadas a um CPF existente
- Consulta de todas as contas cadastradas para um determinado CPF

## 🚀 Como usar

1. Clone ou copie este repositório para sua máquina local.
2. Execute o script em qualquer terminal com Python 3 instalado:

```bash
python nickbank.py
```

3. Use o menu interativo para navegar pelas opções:

```
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Usuário
[5] Criar Conta
[6] Encontre sua conta
[0] Sair
```

## 🛠️ Pré-requisitos
Python 3.x instalado

## 📌 Observações
- O limite de saque é de R$500 por operação.
- Só são permitidos 3 saques por dia (por execução do script).
- O extrato é exibido a partir do histórico da sessão atual.
- É necessário criar um usuário antes de criar uma conta.
- Um mesmo CPF pode ter múltiplas contas vinculadas.

## 📄 Licença
Este projeto é livre para uso acadêmico e educacional.

