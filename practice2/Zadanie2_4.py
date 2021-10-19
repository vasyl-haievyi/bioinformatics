f = open('./data/rosalind_ini5.txt')
out = open('./data/rosalind_ini5.txt_out.txt', 'w')
for idx, line in enumerate(f, start=1):
    if idx %2 != 0:
        continue
    out.write(line)

