table = {
"UUU" : "F",
"CUU" : "L",
"AUU" : "I",
"GUU" : "V",
"UUC" : "F",
"CUC" : "L",
"AUC" : "I",
"GUC" : "V",
"UUA" : "L",
"CUA" : "L",
"AUA" : "I",
"GUA" : "V",
"UUG" : "L",
"CUG" : "L",
"AUG" : "M",
"GUG" : "V",
"UCU" : "S",
"CCU" : "P",
"ACU" : "T",
"GCU" : "A",
"UCC" : "S",
"CCC" : "P",
"ACC" : "T",
"GCC" : "A",
"UCA" : "S",
"CCA" : "P",
"ACA" : "T",
"GCA" : "A",
"UCG" : "S",
"CCG" : "P",
"ACG" : "T",
"GCG" : "A",
"UAU" : "Y",
"CAU" : "H",
"AAU" : "N",
"GAU" : "D",
"UAC" : "Y",
"CAC" : "H",
"AAC" : "N",
"GAC" : "D",
"UAA" : "Stop",
"CAA" : "Q",
"AAA" : "K",
"GAA" : "E",
"UAG" : "Stop",
"CAG" : "Q",
"AAG" : "K",
"GAG" : "E",
"UGU" : "C",
"CGU" : "R",
"AGU" : "S",
"GGU" : "G",
"UGC" : "C",
"CGC" : "R",
"AGC" : "S",
"GGC" : "G",
"UGA" : "Stop",
"CGA" : "R",
"AGA" : "R",
"GGA" : "G",
"UGG" : "W",
"CGG" : "R",
"AGG" : "R",
"GGG" : "G"
}

def rev_dna(dna) -> str:
    rev = ""
    complements = { "A" : "T", "C" : "G", "T" : "A", "G" : "C" }

    for n in reversed(dna):
        rev += complements[n]
    
    return rev

def dna2rna(dna) -> str:
    rna = ""
    for n in dna:
        if n == "T":
            rna += "U"
        else:
            rna += n
    return rna

def print_protein(rna, start=0):
    protein = ""
    for idx in range(start, len(rna), 3):
        if idx + 3 > len(rna):
            break

        key = rna[idx:idx+3]
        value = table[key]
        if value == "Stop":
            break
        else:
            protein += value
    print(protein)

def print_reading_frames(rna):
    start_rna = None
    for idx in range(0, len(rna), 3):
        key = rna[idx:idx+3]    
        value = table[key]
        
        if value == "M":
            start_rna = rna[idx+3:]
            print(start_rna)
            break

    bounded_rna=None    
    for idx in range(0, len(start_rna), 3):
        key = start_rna[idx:idx+3]
        value = table[key]
        
        if value == "Stop":
            bounded_rna = start_rna[:idx]
            print(bounded_rna)
            break
      

    print("M", end='')
    print_protein(bounded_rna)
    
    print("M", end='')
    print_protein(bounded_rna, start=1)
    
    print("M", end='')
    print_protein(bounded_rna, start=2)
    



f = open('./data/rosalind_orf.txt')

id = ""
dna = ""

for line in f:
    if line.startswith(">"):
        id = line[1:].strip()
    else:
        dna += line.strip()

rna = dna2rna(dna)
print_reading_frames(rna)

print('============')

#rdna = rev_dna(dna)
#rna = dna2rna(rdna)
#print_reading_frames(rna)




