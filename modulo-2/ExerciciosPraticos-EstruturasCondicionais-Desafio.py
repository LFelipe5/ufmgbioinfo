#  Versão Python 3.12.3
seqA = "LRSSSQNSSDKPVAHVVANHQVEEQLEWLSQRANALLANGMDLKDNQLVVPADGLYLVYSQVLFKGQGCPDYVLLTHTVSLRSSSDK"
seqB = "KPAAHLIGDPSKQNSLLWRANTDRAFLQDGFSLSNNSLLVPTSGIYFVYSQVVFSGKAYSPKATSSPLYLAHEVQLFSS"
seqC = "CPQGKYIHPQNNSICCTKCHKGTYLYNDCPGPGQDTDCRECESGSFTASENHLRHCLSCSKCRKEMGQVEISSCTVDRDTVCGCR"

# QUESTÃO 1
temp = []
if len(seqA) >= 80:
    temp.append(seqA)
if len(seqB) >= 80:
    temp.append(seqB)
if len(seqC) >= 80:
    temp.append(seqC)
print(temp)

# QUESTÃO 2
media = (len(seqA) + len(seqB) + len(seqC)) / 3
temp = []
if len(seqA) > media:
    temp.append(seqA)
if len(seqB) > media:
    temp.append(seqB)
if len(seqC) > media:
    temp.append(seqC)
print(temp)

# QUESTÃO 3
temp = []
if 'H' in seqA and 'P' in seqA:
    temp.append(seqA)
if 'H' in seqB and 'P' in seqB:
    temp.append(seqB)
if 'H' in seqC and 'P' in seqC:
    temp.append(seqC)
print(temp)

# QUESTÃO 4
if len(seqA) > len(seqB):
    if len(seqA) > len(seqC):
        print("A sequência mais longa é a seqA.")
    else:
        print("A sequência mais longa é a seqC.")
else:
    if len(seqB) > len(seqC):
        print("A sequência mais longa é a seqB.")
    else:
        print("A sequência mais longa é a seqC.")

# QUESTÃO 5
if len(seqA) >= len(seqB):
    if len(seqB) >= len(seqC):
        print("seqC <= seqB <= seqA")
        print(f"{seqC}\n{seqB}\n{seqA}")
    elif len(seqA) >= len(seqC):
        print("seqB <= seqC <= seqA")
        print(f"{seqB}\n{seqC}\n{seqA}")
    else:
        print("seqB <= seqA <= seqC")
        print(f"{seqB}\n{seqA}\n{seqC}")
else:
    if len(seqA) >= len(seqC):
        print("seqC <= seqA <= seqB")
        print(f"{seqC}\n{seqA}\n{seqB}")
    elif len(seqB) >= len(seqC):
        print("seqA <= seqC <= seqB")
        print(f"{seqA}\n{seqC}\n{seqB}")
    else:
        print("seqA <= seqB <= seqC")
        print(f"{seqA}\n{seqB}\n{seqC}")