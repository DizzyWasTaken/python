import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill((255, 255, 255))

rows = input("Inserire il numero di colonne [1, 10]: ")

#Manca il controllo sul numero positivo maggiore di zero

while True:
    try:
        rows = int(rows)
        break
    except ValueError:
        rows = input("Errore! Inserire un valore numerico: ")

cols = input("Inserire il numero di colonne [1, 10]: ")

#Manca il controllo sul numero positivo maggiore di zero

while True:
    try:
        cols = int(cols)
        break
    except ValueError:
        cols = input("Errore! Inserire un valore numerico: ")
        
#Si potrebbero mappare i valori
        '''
colourGradient  = 255
radiusCount     = 100
colourStep      = colourGradient//n
radiusStep      = radiusCount//n
'''
squareSide      = 40
squareSpace     = 1
greenGradient   = 0
greenStep       = 255//cols
blueGradient    = 0
blueStep        = 255//cols

for i in range(rows):
    for j in range(cols):
        pygame.draw.rect(screen, (0, greenGradient + i * greenStep, blueGradient + blueStep * j), (j * squareSide + squareSpace * j, i * squareSide + squareSpace * i, squareSide, squareSide))
        
'''
while n > 0:
    pygame.draw.circle(screen,(colourGradient, 0, 0), (100, 100), radiusCount)
    n -= 1
    colourGradient  -= colourStep
    radiusCount     -= radiusStep
'''

pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
