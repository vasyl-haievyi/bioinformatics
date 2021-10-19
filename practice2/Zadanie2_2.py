f = open('./data/rosalind_ini3.txt')
lines = f.read().strip().split('\n')
print(lines)

for idx in range(0, len(lines), 2):
    text = lines[idx]
    a, b, c, d = list(map(int, lines[idx + 1].split(' ')))
    print(text[a:b+1], text[c:d+1])