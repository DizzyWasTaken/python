from random import randrange
PLACEHOLDER = "cc "
PG = "PG "  #Personaggio
TR = "TR "  #Treasure = tesoro
MN = "MN "  #Monster = mostro
MAP_LIM_ERR = "Raggiunto il limite della mappa!"
WIN_MSG     = "Hai trovato il tesoro!"
LOSE_MSG    = "Sei stato ucciso da una Yandere"
X_LEN = 5
Y_LEN = 5
pg_x, pg_y, = 0, 0
dead = False
win = False

def printMat(mat):              #Stampa primitiva di una matrice assunti
    x_len = len(mat)            #delle dimensioni standard per le celle
    y_len = len(mat[0])

    for i in range(x_len):
        print('---', end="")
    print('--')
    
    for i in range(x_len):
        for j in range(y_len):
            if j == 0:
                print('|', end="")
            print(mat[i][j],  end="")
        print('|')

    for i in range(x_len):
        print('---', end="")
    print('--')

def generateRndCoord(mat, pg_x, pg_y, placeholder): #(matrice, PG_X, PG_Y, placeholder)
    while True:
        x = randrange(5)
        y = randrange(5)
        if x != 0 and y != 0 and mat[x][y] == placeholder:
            break

    return x, y
    

mat = [[PLACEHOLDER for i in range(Y_LEN)] for i in range(X_LEN)] #Inizializzo la matrice

screenMat = [[PLACEHOLDER for i in range(Y_LEN)] for i in range(X_LEN)] #Inizializzo la matrice che mostro sullo schermo

#Inizializziamo la posizione del tesoro del giocatore e del mostro
mat[pg_y][pg_x] = PG
screenMat[pg_y][pg_x] = PG

tr_x, tr_y = generateRndCoord(mat, pg_x, pg_y, PLACEHOLDER)
mat[tr_y][tr_x] = TR
                              
mn_x, mn_y = generateRndCoord(mat, pg_x, pg_y, PLACEHOLDER)
mat[mn_y][mn_x] = MN


#printMat(mat)
printMat(screenMat)

while not dead and not win:
    mat[pg_y][pg_x]         = PLACEHOLDER
    screenMat[pg_y][pg_x]   = PLACEHOLDER
    direction = input("Inserire una direzione valida in cui muoversi [su = w, giù = s, sinistra = a, destra = d]: ")

    if direction.upper() == "W":
        if pg_y > 0:
            pg_y -= 1
        else:
            print(MAP_LIM_ERR)
            
    elif direction.upper() == "A":
        if pg_x > 0:
            pg_x -= 1
        else:
            print(MAP_LIM_ERR)
        
    elif direction.upper() == "S":
        if pg_y < Y_LEN-1:
            pg_y += 1
        else:
            print(MAP_LIM_ERR)
            
    elif direction.upper() == "D":
        if pg_x < X_LEN-1:
            pg_x += 1
        else:
            print(MAP_LIM_ERR)
        
    else:
        print("comando non valido")

    if mat[pg_y][pg_x] == TR:
        win = True
    elif mat[pg_y][pg_x] == MN:
        dead = True
    
    mat[pg_y][pg_x]         = PG
    screenMat[pg_y][pg_x]   = PG

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    #printMat(mat)
    printMat(screenMat)



if win == True:
    print(WIN_MSG)
else:
    print(LOSE_MSG)

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
printMat(mat)
