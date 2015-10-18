from math import sqrt
somma_q, cont = 0, 0

while somma_q < 100:
    n = input("Inserire un numero intero: ")
    while not n.isnumeric():
        n = input("Errore! Inserire un numero intero: ")
    n = int(n)
    cont +=1
    somma_q += n**2

print("Il numero dei valori inseriti è: ", cont, "e la loro media quadratica è: ", sqrt(somma_q/cont))
