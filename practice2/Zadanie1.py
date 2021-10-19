    #============Zadanie 1=============
def zadanie1():
    a = 'TATATAAAAAAAAGGGGGAT'

    #a
    print(a[::-1])

    #b
    print(a[:5])

    #c
    print(a[::3])

    #d
    print()
    for i in range(0, len(a), 3):
        print(a[i: i + 3])
    print()

    #e
    unique = {n for n in a}
    for nucl in unique:
        print(nucl, a.count(nucl))
