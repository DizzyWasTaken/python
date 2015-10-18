n = input("Inserire un numero [inserire 0 per uscire]: ")

while not n.isnumeric():
    n = input("Errore! Inserire un numero [inserire 0 per uscire]: ")
n = int(n)

while n != 0:
    print("Il carattere corrispondente al numero inserito è: ", chr(n))

    n = input("Inserire un numero [inserire 0 per uscire]: ")

    while not n.isnumeric():
        n = input("Errore! Inserire un numero [inserire 0 per uscire]: ")
    n = int(n)
