# Versão Python 3.12.3

# QUESTÃO 1
tupla = ("A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y")

# Questão 1 - a)
print(len(tupla))

# Questão 1 - b)
print("S" in tupla)

# Questão 1 - c)
seg_tupla = ("P", "G", "N", "Y", "V", "W")
print(seg_tupla)

# Questão 1 - d)
print(tupla + seg_tupla)

# Questão 1 - e)
print(f"Ocorrências de 'G' na tupla: {tupla.count('G')}")
print(f"Ocorrências de 'N' na tupla: {tupla.count('N')}")
print(f"Ocorrências de 'C' na tupla: {tupla.count('C')}")

# Questão 1 - f)
print(f"Primeiro elemento Asparagina (N): {tupla.index('N')}")

# Questão 1 - g)
print(tupla[-5:])

