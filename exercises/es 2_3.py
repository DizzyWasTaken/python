from math import sqrt 

def hypotenuse(c1:float, c2:float) -> (float):
    return sqrt(c1 **2 + c2**2)

c1 = input("Inserire la dimensione del primo cateto: ")

#Manca il controllo sul numero positivo maggiore di zero

while True:
    try:
        c1 = float(c1)
        break
    except ValueError:
        c1 = input("Errore! Inserire un valore reale: ")

c2 = input("Inserire la dimensione del secondo cateto: ")

while True:
    try:
        c2 = float(c2)
        break
    except ValueError:
        c2 = input("Errore! Inserire un valore reale: ")

print("La dimensione dell'ipotenusa è: ", hypotenuse(c1, c2))
