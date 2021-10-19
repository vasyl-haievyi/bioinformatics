
text = open('./data/rosalind_revc.txt').read().strip()

complements = { "A" : "T", "C" : "G", "T" : "A", "G" : "C" }


for n in reversed(text):
    print(complements[n], end='')
print()
