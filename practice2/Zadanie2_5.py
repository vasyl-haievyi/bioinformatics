text = open('./data/rosalind_ini6.txt').read().strip()

occurences = {}

for word in text.split(' '):
    if word in occurences:
        occurences[word] += 1
    else:
        occurences[word] = 1

for word in occurences:
    print(word, occurences[word])