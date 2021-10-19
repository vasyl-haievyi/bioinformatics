f = open('./data/rosalind_gc.txt')


id = ""
dna = ""

gc_dict = {}

for line in f:
    if line.startswith(">"):
        new_id = line[1:].strip()
        if len(dna) != 0:
            gc_content = ((dna.count("G") + dna.count("C")) / len(dna)) * 100.0
            gc_dict[id] = gc_content
            dna = ""
        id = new_id
    else:
        dna += line.strip()

gc_content = ((dna.count("G") + dna.count("C")) / len(dna)) * 100.0
gc_dict[id] = gc_content

max_gc = max(gc_dict.items(), key= lambda x: x[1])



print(max_gc[0])
print(max_gc[1])