f = open('./data/rosalind_ini2.txt')
for line in f:
    first, second = list(map(int, line.split(' ')))

    print(first ** 2 + second ** 2)
