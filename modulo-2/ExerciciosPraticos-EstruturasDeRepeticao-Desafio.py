# Versão Python 3.12.3

# QUESTÃO 1
for i in range(1, 150):
    C = 5 / 9 * (i - 32)
    print(f"C = {C} F = {i}")

# QUESTÃO 2
sequencias = [
    "ATCDLASKWNWNHTLCAAHCIARRYRGGYCNSKAVCVCRN",
    "TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT"
    "ATCBDLASKWXWNHTLCAAHCIARRYRGGYCNSJAVCVCRN",
    "xyz"
]

dna = ["A", "G", "C", "T"]
rna = ["U", "C", "A", "G"]
proteinas = set(["A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y"])    
for i, seq in enumerate(sequencias, 1):
    print(f"--- Sequência {i}: {seq} ---")

    # Considera true inicialmente
    bool_dna = True
    bool_rna = True
    bool_proteina = True
    
    # Loop para verificar se é DNA
    for letra in seq:
        if letra not in dna:
            bool_dna = False  
            break
            
    # Loop para verificar se é RNA
    for letra in seq:
        if letra not in rna:
            bool_rna = False
            break
            
    # Loop para verificar se é PROTEÍNA
    for letra in seq:
        if letra not in proteinas:
            bool_proteina = False
            break
            
    # Verificação dos resultados baseada nas variáveis de controle (flags)
    if bool_dna:
        print("Resultado: É uma sequência de DNA.")
    elif bool_rna:
        print("Resultado: É uma sequência de RNA.")
    elif bool_proteina:
        print("Resultado: É uma sequência de PROTEÍNA.")
    else:
        print("Resultado: Nenhuma das opções.")
        
        # Loop para encontrar caracteres que não pertencem a NENHUM dos três alfabetos
        letras_invalidas = []
        for letra in seq:
            if letra not in dna and letra not in rna and letra not in proteinas:
                # Evita adicionar letras repetidas na lista de exibição
                if letra not in letras_invalidas:
                    letras_invalidas.append(letra)
                    
        print(f"Letras que não fazem parte de nenhum alfabeto: {letras_invalidas}")
    print()

# QUESTÃO 3
seq3 = "TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT"
complemento = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

seq_complemento_reverso = ""

# Loop para percorrer a sequência original de trás para frente
for i in range(len(seq3) - 1, -1, -1):
    letra_original = seq3[i]
    letra_complementar = complemento[letra_original]

    # nova string
    seq_complemento_reverso += letra_complementar

# Imprime os resultados
print(f"Sequência Original: {seq3}")
print(f"Complemento Reverso: {seq_complemento_reverso}")

# QUESTÃO 4
valor_fat = 5
resultado = 0

for i in range(1, valor_fat):
    resultado = resultado * i

print(resultado)

# QUESTÃO 5
for valor in range(1, 16):
    print(f"Tabuada do {valor}:")

    for i in range(1, 11):
        produto = valor * i
        print(f"{valor} x {i} = {produto}")

# QUESTÃO 6
seqCalcMolar = "VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL"
tabela_massas = {
    "A": 71.03711, "C": 103.00919, "D": 115.02694, "E": 129.04259,
    "F": 147.06841, "G": 57.02146, "H": 137.05891, "I": 113.08406,
    "K": 128.09496, "L": 113.08406, "M": 131.04049, "N": 114.04293,
    "P": 97.05276, "Q": 128.05858, "R": 156.10111, "S": 87.03203,
    "T": 101.04768, "V": 99.06841, "W": 186.07931, "Y": 163.06333
}

massa_molar_total = 0.0

for aminoacido in seqCalcMolar:
    if aminoacido in tabela_massas:
        massa_molar_total += tabela_massas[aminoacido]
    else:
        print(f"Aviso: Caractere inválido encontrado: {aminoacido}")
print(f"Massa Molar Total da sequência: {massa_molar_total:.5f} g/mol")

# QUESTÃO 7
sequencias = [
    "KTCENLADTFRGPCFTDGSDDHCKNKEHLIKGRCRDDFRCWCTRNC",
    "ATCDLASGFGVGSSLCAAHCLVKGYRGGYCKNKICHCRDKF",
    "ATCDLASGFGVGSSLCAAHCIARRYRGGYCNSKAVCVCRN",
    "ATCDLASIFNVNHALCAAHCIARRYRGGYCNSKAVCVCRN",
    "ATCDLASKWNWNHTLCAAHCIARRYRGGYCNSKAVCVCRN",
    "ATCDLASFSSQWVTPNDSLCAAHCIARRYRGGYCNGKRVCVCR",
    "ATCDLASFSSQWVTPNDSLCAAHCLVKGYRGGYCKNKICHCRDKF"
]
menor_seq = sequencias[0]
maior_seq = sequencias[0]

soma_comprimentos = 0
comprimentos = []

# Loop para processar os comprimentos de todas as sequências
for seq in sequencias:
    tamanho = len(seq)
    comprimentos.append(tamanho)
    soma_comprimentos += tamanho
    
    # A) Verifica se é a menor sequência encontrada até agora
    if tamanho < len(menor_seq):
        menor_seq = seq
        
    # B) Verifica se é a maior sequência encontrada até agora
    if tamanho > len(maior_seq):
        maior_seq = seq

# C) Cálculo da Média
media_comprimento = soma_comprimentos / len(sequencias)

# D) Cálculo da Mediana (utilizando ordenação manual/loops)
# Primeiro, ordenamos a lista de comprimentos de forma crescente (algoritmo Bubble Sort simples)
comprimentos_ordenados = sorted(comprimentos)
n = len(comprimentos_ordenados)

if n % 2 != 0:
    mediana_comprimento = comprimentos[n // 2]
else:
    mediana_comprimento = (comprimentos[(n // 2) - 1] + comprimentos[n // 2]) / 2

print(f"A) MENOR SEQUÊNCIA:\n   {menor_seq}\n   Comprimento: {len(menor_seq)} aminoácidos\n")
print(f"B) MAIOR SEQUÊNCIA:\n   {maior_seq}\n   Comprimento: {len(maior_seq)} aminoácidos\n")
print(f"C) MÉDIA DOS COMPRIMENTOS:\n   {media_comprimento:.2f} aminoácidos\n")
print(f"D) MEDIANA DOS COMPRIMENTOS:\n   {mediana_comprimento} aminoácidos")

# QUESTÃO 8
mol1 = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1]
mol2 = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0]
soma_and = 0
soma_or = 0
for i in range(len(mol1)):
    bit1 = mol1[i]
    bit2 = mol2[i]
    
    if bit1 == 1 and bit2 == 1:
        soma_and += 1
        
    if bit1 == 1 or bit2 == 1:
        soma_or += 1

if soma_or > 0:
    distancia_tanimoto = soma_and / soma_or
else:
    distancia_tanimoto = 0.0

print(f"Soma do vetor AND (A ∧ B): {soma_and}")
print(f"Soma do vetor OR  (A ∨ B): {soma_or}")
print(f"Distância de Tanimoto:     {distancia_tanimoto:.4f}")