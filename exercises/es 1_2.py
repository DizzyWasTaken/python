#Il programma non prevede tutti i possibili casi dell'input
year = input("Inserire un anno [inserire 0 per uscire]: ")
while not year.isnumeric():
    print("Inserire per favore un anno composto di soli caratteri numerici")
    year = input("Inserire un anno [inserire 0 per uscire]: ")

year = int(year)
    
while year != 0:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
        print("L'anno inserito è bisestile ")
    else:
        print("L'anno inserito non è bisestile")
    year = input("Inserire un anno [inserire 0 per uscire]: ")
    while not year.isnumeric():
        print("Inserire per favore un anno composto di soli caratteri numerici")
        year = input("Inserire un anno [inserire 0 per uscire]: ")
    year = int(year)
    
