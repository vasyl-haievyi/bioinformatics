f = open('./data/rosalind_ini4.txt')
for line in f:
    a, b = list(map(int, line.split(' ')))

    odd_sum = sum(filter(lambda x: x%2 != 0, range(a, b)))
    print(odd_sum)
