f = open('./data/rosalind_glob.txt')


id = ""
sequence = ""
sequences = []


for line in f:
    if line.startswith(">"):
        new_id = line[1:].strip()
        if len(sequence) != 0:
            sequences.append(sequence)
            sequence = ""
        id = new_id
    else:
        sequence += line.strip()
if sequence:
    sequences.append(sequence)

print(len(sequences))


from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matrixlist

matrix = matrixlist.blosum62
pairWiseAlignments = pairwise2.align.globalds(sequences[0], sequences[1], matrix, -5, -5)

print(max(pairWiseAlignments).score)
