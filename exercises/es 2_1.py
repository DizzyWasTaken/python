line = input("Inserire una riga di testo: ")
cont = 0

for c in line:
    if '0' <= c <= '9':
        cont += 1

print("Il numero complessivo di cifre presenti è: ", cont)
