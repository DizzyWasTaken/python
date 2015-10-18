line        = input("Inserire una riga di testo: ")
occurrences = [0] * 10

for c in line:
    if '0' <= c <= '9':
        print(ord(c))
        occurrences[ord(c)-48] += 1

print("Le occorrenze dei numeri inseriti nella stringa")
index = 0
for o in occurrences:
    print(index, ": ", o,"volta" if o == 1 else "volte")
    index += 1
