def getNum():
    n = input("Inserire un numero: ")

    while not n.isnumeric():
        n = input("Errore! Inserire un numero: ")

    return int(n)

n = getNum()
x = getNum()

a, b, i, somma = 1, 1, 1, 0

while i < n and a < n:
    if a % x == 0:
        somma += a
    print(a)
    a, b = b, a+b
    
print("La somma dei numeri di fibonacci divisibili per ", x, "è: ", somma)
