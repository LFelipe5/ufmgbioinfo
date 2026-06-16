# Versão Python 3.12.3

# QUESTÃO 1
tamseq = 25

if tamseq >= 50:
    print("A sequência é aceita.")
else:
    print("A sequência é rejeitada.")

# QUESTÃO 2
tamseq = 10

if tamseq > 2 and tamseq <= 50:
    print("A sequência é aceita.")
else:
    print("A sequência é rejeitada.")

# QUESTÃO 3
aminoacidos = 30

if aminoacidos == 2:
    print("É dipeptídeo.")
elif aminoacidos == 3:
    print("É tripeptídeo.")
elif aminoacidos > 3 and aminoacidos <= 50:
    print("É polipeptídeo.")

# QUESTÃO 4
hidrofobico = ['I', 'V', 'L', 'M', 'C', 'A', 'T', 'F', 'Y', 'W', 'H', 'K']
pequeno = ['P', 'A', 'G', 'C', 'S', 'T', 'D', 'N', 'V']
polar = ['C', 'S', 'T', 'N', 'D', 'Q', 'Y', 'W', 'H', 'K', 'R', 'E']
carregado = ['D', 'E', 'R', 'K', 'H']
aromatico = ['F', 'Y', 'W', 'H']
minusculo = ['A', 'C', 'G', 'S']
alifatico = ['I', 'L', 'V']
hidroxila = ['T', 'S']
acido = ['N', 'Q']
enxofre = ['C', 'M']

aminoacido = 'A'

if aminoacido in hidrofobico:
    print(f"{aminoacido} - hidrofobico")
elif aminoacido in pequeno:
    print(f"{aminoacido} - pequeno")
elif aminoacido in polar:
    print(f"{aminoacido} - polar")
elif aminoacido in carregado:
    print(f"{aminoacido} - carregado")
elif aminoacido in aromatico:
    print(f"{aminoacido} - aromatico")
elif aminoacido in minusculo:
    print(f"{aminoacido} - minusculo")
elif aminoacido in alifatico:
    print(f"{aminoacido} - alifatico")
elif aminoacido in hidroxila:
    print(f"{aminoacido} - hidroxila")
elif aminoacido in acido:
    print(f"{aminoacido} - acido")
elif aminoacido in enxofre:
    print(f"{aminoacido} - enxofre")

# QUESTÃO 5
if aminoacido not in polar:
    print(f"{aminoacido} - não polar")
else:
    print(f"{aminoacido} - polar")

if aminoacido not in carregado:
    print(f"{aminoacido} - não carregado")
else:
    print(f"{aminoacido} - carregado")

# QUESTÃO 6
purinas = ['A', 'G']
pirimidinas = ['C', 'T']
todos_nucleotideos = purinas + pirimidinas

valor = 'A'

if valor in todos_nucleotideos:
    print(f"{valor} é um nucleotídeo.")

    if valor in purinas:
        print(f"{valor} é uma purina.")
    else:
        print(f"{valor} é uma pirimidina.")
else:
    print(f"{valor} não é um nucleotídeo.")