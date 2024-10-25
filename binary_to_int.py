x = "110011"

def Binary(x):
    lenght = len(x)
    wynik = 0
    for a in range(lenght):
        bit = int(x[a])
        wynik += bit * (2 ** (lenght - a - 1))
    print(wynik)

Binary(x)