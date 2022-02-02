from Bio import SeqIO

PDB_file_paths = ['lab14_protein2.pdb', 'lab14_protein3.pdb']

for path in PDB_file_paths:
    record =  next(SeqIO.parse(path, 'pdb-atom'))
    seq = str(record.seq)

    f = open(path.replace(".pdb", ".seq"), "w")
    f.write(seq)
    f.close()