# Versão Python 3.12.3

# QUESTÃO 1

for i in range(0, 11):
    print(i)
print("while")
i = 0
while i <= 10:
    print(i)
    i += 1
# QUESTÃO 2
for i in range(0, 11):
    if i % 2 == 0:
        print(i)
print("while")
i = 0
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1
# QUESTÃO 3
dna = "TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT"
base_dna = "AGCT"
validez = True

for letra in dna:
    if letra not in base_dna:
        validez = False
        break

if validez:
    print("A sequência é válida.")
else:
    print("A sequência é inválida.")

# QUESTÃO 4
for i in range(1, 101):
    divisores = []

    for j in range(1, i + 1):
        if i % j == 0:
            divisores.append(j)
    print(f"{i}: {divisores}")

# QUESTÃO 5
for i in range(1, 1001):
    if i < 2:
        continue

    primo = True
    limite = int(i ** 0.5)
    for j in range(2, limite + 1):
        if i % j == 0:
            primo = False
            break
    if primo:
        print(f"{i} é primo.")

# QUESTÃO 6
subseq = "AAA"

seq = "VRSSSRTPSDKPVAAAAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLAAAFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKAAASPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAAAAEINRPDYLLFAESGQVYFGIIAL"
print("Ocorrências encontradas:")
posicao = 0
while True:
    posicao = seq.find(subseq, posicao)
    if posicao == -1:
        break
    print(f"Ocorrência encontrada na posição: {posicao}")
    posicao += 1

# QUESTÃO 7
lista = ['KTCENLA', 'DTFR', 'GPCFTDGSC', 'DDHCKNKEHLIK', 'GRCRDDFRC', 'WCTRNC', 'ATC']
print(lista.sort())

# QUESTÃO 8
lista = [1,4,6,3,4,5,7,8,9,5,6,7,4,3,5,6,7,8]
media = sum(lista) / len(lista)
print(f"A média é: {media}")