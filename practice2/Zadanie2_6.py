text = open('./data/rosalind_dna.txt').read().strip()

for n in "ACGT":
    print(text.count(n), end=' ')
print()