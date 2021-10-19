gencode = { 'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',   'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',   'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',   'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',   'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',   'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',   'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',   'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',   'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',   'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',   'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',   'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',   'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',   'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',   'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W' }


file = open('./hemoglobine.txt')

nucleotides = file.read().replace("\n", "")

file.close()

def decode(start = 0):
	decoded = ""

	for i in range(start, len(nucleotides), 3):
		code = nucleotides[i:i+3]
		
		if (gencode[code] == '*'):
			break

		decoded += gencode[code]

	return decoded


print(decode(start=0))
print(decode(start=1))
print(decode(start=2))

"""
Output:

TFASDTTVFTSNLKQTPWCI
HLLLTQLCSLATSNRHHGASDS
ICF
"""




