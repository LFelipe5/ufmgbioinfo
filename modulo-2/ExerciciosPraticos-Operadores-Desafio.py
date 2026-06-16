# Versão Python 3.12.3
import math
# QUESTÃO 1
glicinaNum1 = [
    [108.304, 100.827, 67.992], 
    [108.477, 100.389, 69.362],
    [109.907, 100.555, 69.817],
    [110.821, 100.799, 69.027]
]
glicinaNum2 = [
    [107.670, 101.359, 70.074], 
    [108.477, 100.389, 69.362], 
    [109.513, 101.011, 68.450], 
    [110.667, 100.572, 68.425]
]

# Cálculo do RSMD
N = len(glicinaNum1)
soma_total = 0.0

for i in range(N):
    x1, y1, z1 = glicinaNum1[i]
    x2, y2, z2 = glicinaNum2[i]
    dist_quadrada = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2
    soma_total += dist_quadrada

rmsd = math.sqrt(soma_total / N)

print(f"O RMSD calculado para a Glicina é: {rmsd:.6f}")

# QUESTÃO 2
seqA = "ATGATCTCGTAATTAACCGGAATTTTGGGCC"
seqB = "GGCCTTAAGTTTAACCCGGAATTTAAAGGCCCCAAA"

total_gc_A = seqA.count('G') + seqA.count('C')
total_bases_A = len(seqA)
porcentagem_gc_A = (total_gc_A / total_bases_A) * 100

total_gc_B = seqB.count('G') + seqB.count('C')
total_bases_B = len(seqB)
porcentagem_gc_B = (total_gc_B / total_bases_B) * 100

print(f"Sequência A: {porcentagem_gc_A:.2f}")
print(f"Sequência B: {porcentagem_gc_B:.2f}")