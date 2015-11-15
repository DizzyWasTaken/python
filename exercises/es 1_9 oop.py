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



class Entity:

    def __init__(self, x: int, y: int, placeholder: str):
        self._x = x
        self._y = y
        self._placeholder = placeholder

    @property
    def position(self) -> (int, int):
        return self._x, self._y

    @pos.setter  # if you also really need a setter
    def pos(self, val: (int, int)):
        self._x, self._y = val

    @property
    def placeholder(self) -> (str):
        return self._placeholder

    def move(self):     #Esistono senz'altro soluzioni migliori
        pass
        

class Character(Entity):

    def __int__(self, x: int, y: int, placeholder: str):
        Entity.__init__(self, x, y, placeholder)

    
    def move(self, direction: str):
        if direction    == "up":
            self._x -= 1
        elif direction  == "down":
            self._x += 1
        elif direction  == "left":
            self._y -= 1
        elif direction  == "right":
            self._y += 1
        else:
            raise RuntimeError('Wrong parameter')     #Raisare un'eccezione piu appropriata
        


class Map:

    def __init__(self, width: int, height : int, placeholder: str):
        self._width         = width #chiama x e y width e heigth
        self._height        = height
        self._placeholder   = placeholder
        self._entities      = []
        self._mat           = [[placeholder for i in range(width)] for i in range(height)] #Inizializzo la matrice

    def addEntity(self, e: Entity):
        '''
        for ent in self._entities:
            
            entX, entY = ent.position
            if self._mat[entX][entY] != self._placeholder:
                raise RuntimeError('Entity is being placed over another entity') from error     #Raisare un'eccezione piu appropriata
        '''
        conflict    = False     #Appena incontraun conflitto il ciclo si ferma, più efficente di un for se si hanno molte entità
        i           = 0

        while not conflict and i<len(self._entities):
            entX, entY = self._entities[i].position
            if self._mat[entX][entY] != self._placeholder:
                raise RuntimeError('Entity is being placed over another entity')      #Raisare un'eccezione piu appropriata
                conflict = True
            i += 1

        self._entities.append(e)
        entX, entY = e.position
        self._mat[entX][entY] = e.placeholder
        '''
        entX, entY = e.position
        
        while self._mat[entX][entY] != self._placeholder:       #Se l'entità non è collocata in una posizione vuota, la sua posizione
            entX, entY = randrange(self._width), randrange(self._height)    #verrà scelta casualmente
            
        self._mat[entX][entY] = e.placeholder
        '''
        
    def moveAll(self):
        pass

    def printMap(self):
        for e in self._entities:
            entX, entY = e.position
            
            self._mat[entX][entY] = e.placeholder
        
        for i in range(self._width):
            print('---', end="")
        print('--')

        for i in range(self._width):
            for j in range(self._height):
                if j == 0:
                    print('|', end="")
                print(self._mat[i][j],  end="")
            print('|')

        for i in range(self._width):
            print('---', end="")
        print('--')


mappa = Map(5, 5, PLACEHOLDER)

player      = Character(0, 0, PG)
treasure    = Entity(0, 0, TR)
#monster    = Entity(0, 0, MN)


mappa.addEntity(player)
while True:
    try:
        mappa.addEntity(treasure)
        break
    except RuntimeError:
        entX, entY = randrange(self._width), randrange(self._height)
        treasure.pos = (entX, entY)
        print("bella zio")


        
#mappa.addEntity(monster)
'''
while not dead and not win:
    direction = input("Inserire una direzione valida in cui muoversi [su = w, giù = s, sinistra = a, destra = d]: ")
    '''
    
mappa.printMap()

#################################################################
#parte iterativa
################################################################
'''
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

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
printMat(mat)

if win == True:
    print(WIN_MSG)
else:
    print(LOSE_MSG)
'''

