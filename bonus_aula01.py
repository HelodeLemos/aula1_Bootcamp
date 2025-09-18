# Constante definida para o cálculo do bônus
CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome
nome = input("Digite seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um npumero de ponto flutuante
salario = float(input("Digite o valor do seu salário: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus_recebido = float(input("Digite o valor do bônus recebido (em porcentagem, ex: 0.1 para 10%): "))

# 4) Calcule o valor do bônus final

bonus_final = CONSTANTE_BONUS + salario * bonus_recebido

# 5) Imprima cáculo de KPI PARA O USUÁRIO
# Este passo é opcional, mas ajuda a mostrar o valor calculado.
print(f"O valor do bônus calculado foi: R$ {bonus_final}")

# 6) Imprime a mensagem personalizada incluindo o nome do usuário
print(f"Olá {nome}, seu bônus final foi de R$ {bonus_final:.2f}.")