dna = open('./data/rosalind_rna.txt').read().strip()

for n in dna:
    if n == "T":
        print("U", end='')
    else:
        print(n, end='')

print()