# Versão Python 3.12.3

# QUESTÃO 1
sequencia_aminoacido = f"VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL"

# Questão 1 - a)
print(len(sequencia_aminoacido))

# Questão 1 - b)
print(sequencia_aminoacido.count("LL"))

# Questão 1 - c)
print(
    f"{sequencia_aminoacido.find("GG")} e {sequencia_aminoacido.find("RR")}"
)

# Questão 1 - d)
print(sequencia_aminoacido[:100])

# Questão 1 - e)
substituicao = sequencia_aminoacido.replace("SSSR", "AAAA")
print(substituicao)

# Questão 1 - f)
quebra = sequencia_aminoacido.split("SSSR")
print(quebra)

# QUESTÃO 2
texto = f"As proteínas são cadeias polipeptídicas formadas pela ligação peptídica entre resíduos de aminoácidos. \
Existem 20 tipos de aminoácidos comumente encontrados nos seres vivos. A esses aminoácidos, foram \
atribuídas abreviações de 3 letras e símbolos de 1 letra. As abreviações de 3 letras são bastante evidentes \
consistindo nas três primeiras letras do se nome."

# Questão 2 - a)
print(texto.upper())

# Questão 2 - b)
print(texto.lower())

# Questão 2 - c)
print(texto.title())

# Questão 2 - d)
print(texto.swapcase())

# QUESTÃO 3
insulin_signal = "MALWMRLLPLLALLALWGPDPAAA"

# Questão 3 - a)
print(len(insulin_signal))

# Questão 3 - b)
quebra = insulin_signal.split("LLALLALWG")
print(quebra)

# Questão 3 - c)
print(quebra[0] + quebra[1])

# Questão 3 - d)
print(insulin_signal.replace("DPAAA", "LLALL"))

# QUESTÃO 4
dna = "ATGGAACTTGACGTAAACCTATATT"
rna = dna.replace("T", "U")
print(rna)