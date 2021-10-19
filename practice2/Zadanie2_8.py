first, second = open("./data/rosalind_hamm.txt").read().strip().split('\n')

hamm_dist = 0
for a, b in zip(first, second):
    if a != b:
        hamm_dist += 1

print(hamm_dist)