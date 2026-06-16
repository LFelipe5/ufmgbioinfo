# Versão Python 3.12.3

# QUESTÃO 1
a = 25
b = "25"

print(a == b)  # Verifica se são iguais

# QUESTÃO 2
valor1 = 1
valor2 = 2
valor3 = 3
valor4 = 5
valor5 = 8

media_aritmetica = (valor1 + valor2 + valor3 + valor4 + valor5) / 5
print(media_aritmetica)

# QUESTÃO 3
valor_base = 3
valor_expoente = 3

resultado = valor_base ** valor_expoente
print(resultado)

# QUESTÃO 4
primeiro_numero = 10
segundo_numero = 3

resto_divisao = primeiro_numero % segundo_numero
print(resto_divisao == 0)

# QUESTÃO 5
numero1 = 15
numero2 = 5

quociente = numero1 // numero2
print(quociente)

# QUESTÃO 6
seq = 25
print(seq >= 5 and seq <= 30)  # Verifica se o número está entre 5 e 30

# Questão 7
seq = 3
print(seq > 5 and seq <= 30)  # Verifica se o número está entre 5 e 30

# Questão 8
aminoacido = 'd'

aminociados = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

print(aminoacido.upper() in aminociados)  # Verifica se o aminoácido está na lista

# Questão 9
pos=['H', 'K', 'R']
neg=['D', 'E']

aminoacido = 'D'

print(f"Positivamente carregados: {aminoacido in pos or aminoacido in neg}")
print(f"Negativamente neutro: {aminoacido not in pos and aminoacido not in neg}")
     