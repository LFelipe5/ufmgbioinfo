# Versão Python 3.12.3

# QUESTÃO 1

conjunto1 = {
    1.9, 1.8, 5.7, 1.6, 5.8, 1.7, 9.6, 5.9, 9.5, 6.5, 6.2, 1.1, 4.4, 3.5, 2.9, 4.7,4.6, 5.2, 5.3
}
conjunto2 = {
    4.7, 3.6, 6.2, 7.1, 7, 5.6, 5.7, 3.4, 3.3, 2.1, 3.8, 3.9, 5, 5.1, 1.9, 9.5, 1.0, 1.3, 5.4
}
conjunto3 = {
    2.2, 3.3, 5.1, 3, 3.7, 9.1, 8.8, 8.5, 2, 4.1, 6.1, 4.9, 1.1, 0.5, 0.8, 3.2, 6.9, 9.3, 9.5
}

# Questão 1 - a)
conjunto1.difference(conjunto2)
conjunto1.difference(conjunto3)
conjunto2.difference(conjunto3)

# Questão 1 - b)
conjunto1.intersection(conjunto2)
conjunto1.intersection(conjunto3)
conjunto2.intersection(conjunto3)

# Questão 1 - c)
conjunto1.update(conjunto2, conjunto3)

# Questão 1 - d)
print(len(conjunto1))

# QUESTÃO 2
A = {3, 6, 9, 12, 15, 18, 21, 24, 28, 27}
B = {2, 6, 8, 10, 14, 16, 18, 20, 22, 24}
C = {2, 6, 10, 18, 20}
D = {1, 30, 5, 11, 17, 16, 22, 26}

# Questão 2 - a)
print(A.intersection(B))
print(A.difference(B))

# Questão 2 - b)
print(A.isdisjoint(B))

# Questão 2 - c)
print(C.issubset(B))
print(C.issubset(A))

# Questão 2 - d)
D.update([18, 23, 25, 63])
print(D)
