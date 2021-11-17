f = open('./data/Zadanie3.txt')


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

matrix = matrixlist.pam250
pairWiseAlignments = airWiseAlignments = pairwise2.align.localds(sequences[0], sequences[1], matrix, -5, -5)

maxAlighment = max(pairWiseAlignments, key=lambda x: x.score)

start, stop = maxAlighment[3:]
print(maxAlighment.score)
print(maxAlighment[0][start:stop].replace("-", ""))
print(maxAlighment[1][start:stop].replace("-", ""))
