import random

# Define os caracteres para a nova senha
minusculo = "abcdefghijklmnopqrstuvxyz"
maiusculo = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
numericos = "0123456789"
especiais = "!_-.;:[]()"

# -------------------------------------------------------------
# AGORA, VOCÊ DEVE ADICIONAR CARACTERES NUMÉRIOS PARA A SENHA.
# -------------------------------------------------------------

# Junta todos os caracteres em uma única string
tudo = minusculo + maiusculo + numericos + especiais
tamanho = 12  # Tamanho da senha

# Inicializa a senha como uma string vazia
senha = ""

# Gera a senha selecionando aleatoriamente caracteres da string "tudo"
for _ in range(tamanho):
    senha += random.choice(tudo)

# OUTPUT
print("=========================================")
print("\nTa aqui a senha seu preguiçoso:", senha)
print("=========================================")
