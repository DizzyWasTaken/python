somma = 0
n = input("Inserire un numero: ")

while not n.isnumeric():
    n = input("Errore! Inserire un numero: ")

n = int(n)

for i in range(n):
    if i % 3 == 0 or i % 5 == 0:
        somma += i

print("La somma di tutti i numeri multipli di tre o di cinque minori del numero dato è: ", somma)
