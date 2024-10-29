# Criando-um-Sistema-Bancario-com-Python

README: Simulador de Banco Simples em Python
Descrição:
Este projeto em Python simula um simples sistema bancário, permitindo ao usuário realizar operações como depósito, saque e consulta de extrato. O sistema possui um limite de saques diários e um limite de valor por saque.

Funcionalidades:
Depósito: Permite ao usuário depositar valores em sua conta.
Saque: Permite ao usuário sacar valores, respeitando o limite de saques diários e o limite de valor por saque.
Extrato: Exibe o histórico de transações e o saldo atual da conta.
Sair: Encerra o programa.
Como usar:
Executar o código: Execute o script Python em seu ambiente de desenvolvimento.
Selecionar a operação: O programa apresentará um menu com as opções disponíveis. Digite o número correspondente à operação desejada e pressione Enter.
Seguir as instruções: Siga as instruções na tela para realizar cada operação.
Variáveis:
saldo: Armazena o saldo atual da conta.
limite: Define o limite máximo por saque.
extrato: Armazena o histórico de transações em formato de string.
numero_saques: Contabiliza o número de saques realizados no dia.
LIMITE_SAQUES: Define o limite máximo de saques por dia.
Lógica do programa:
Loop principal: Um loop while True mantém o programa em execução até que o usuário escolha a opção de sair.
Menu: Apresenta as opções disponíveis ao usuário.
Verificação de opções: O programa verifica a opção escolhida pelo usuário e executa a ação correspondente.
Validações: São realizadas diversas validações para garantir a integridade das operações, como:
Valor de depósito positivo.
Valor de saque menor ou igual ao saldo e ao limite.
Número de saques dentro do limite diário.
Considerações:
Simplificação: Este é um exemplo simplificado de um sistema bancário e não inclui funcionalidades mais complexas como juros, taxas, etc.
