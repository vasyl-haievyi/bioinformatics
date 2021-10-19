f = open('./data/rosalind_subs.txt')

dna = f.readline().strip()
dna_subs = f.readline().strip()

for idx in range(0, len(dna) - len(dna_subs)):
    subs = dna[idx:idx + len(dna_subs)]
    if subs == dna_subs:
        print(idx + 1, end=' ')

print()