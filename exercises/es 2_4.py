import pygame

pygame.init()
screen = pygame.display.set_mode((200, 200))
screen.fill((255, 255, 255))

n = input("Inserire il numero di cerchi da disegnare [1, 100]: ")

#Manca il controllo sul numero positivo maggiore di zero

while True:
    try:
        n = int(n)
        break
    except ValueError:
        n = input("Errore! Inserire un valore numerico: ")
#Si potrebbero mappare i valori
colourGradient  = 255
radiusCount     = 100
colourStep      = colourGradient//n
radiusStep      = radiusCount//n

while n > 0:
    pygame.draw.circle(screen,(colourGradient, 0, 0), (100, 100), radiusCount)
    n -= 1
    colourGradient  -= colourStep
    radiusCount     -= radiusStep

pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
