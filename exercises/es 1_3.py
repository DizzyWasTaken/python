n = input("Inserire un numero: ")

while not n.isnumeric():
    n = input("Errore! Inserire un valore numerico: ")

n = int(n)

for i in range(1, n+1):
    if n % i == 0:
        print(i, " è divisore di n")
