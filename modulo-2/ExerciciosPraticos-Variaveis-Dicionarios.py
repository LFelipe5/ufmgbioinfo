# Versão Python 3.12.3

# QUESTÃO 1
dicionario={'1A8M':471,'1TNR':283, '2AZ5':592, '1TNF':471, '2TNF':468, '2TUN':942, '4TSV': 150 ,'5TSW' : 900,'2E7A':471,'6RMJ':489	}

# Questão 1 - a)
print(dicionario)

# Questão 1 - b)
print(dicionario['2TNF'])
print(dicionario['2E7A'])

# Questão 1 - c)
print(len(dicionario))

# Questão 1 - d)
lista_chaves = list(dicionario.keys())
print(lista_chaves)

# Questão 1 - e)
lista_valores = list(dicionario.values())
print(lista_valores)

# Questão 1 - f)
tuplas = dicionario.items()
print(tuplas)