#!/usr/bin/env python3

'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import pygame
from arena import *
from pacman import *
from pacman_map import *

#Ghost sprites constants definition
redGhostY      = 64
redGhostHeigth = 16

redGhost = 0, redGhostY
pinkGhost = 0, redGhostY + redGhostHeigth
blueGhost = 0, redGhostY + (redGhostHeigth *2)
orangeGhost = 0, redGhostY + (redGhostHeigth * 3)

arena = Arena(232, 256)

for x, y, w, h in walls_pos:
    Wall(arena, x, y, w, h)
for x, y in cookies_pos:
    Cookie(arena, x, y)
for x, y in powers_pos:
    Power(arena, x, y)

pacman = PacMan(arena, 112, 184)
Ghost(arena, 112, 88, redGhost)
Ghost(arena, 112, 88, pinkGhost)
Ghost(arena, 112, 88, blueGhost)
Ghost(arena, 112, 88, orangeGhost)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(arena.size())
background = pygame.image.load('pacman_background.png')
sprites = pygame.image.load('pacman_sprites.png')

playing = True
while playing:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            playing = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                pacman.moveUp()
            elif e.key == pygame.K_DOWN:
                pacman.moveDown()
            elif e.key == pygame.K_LEFT:
                pacman.moveLeft()
            elif e.key == pygame.K_RIGHT:
                pacman.moveRight()
        #elif e.type == pygame.KEYUP:
            #turtle.stay()

    arena.move_all()  # Game logic

    screen.blit(background, (0, 0))
    for a in arena.actors():
        if not isinstance(a, Wall):
            x, y, w, h = a.rect()
            xs, ys = a.symbol()
            screen.blit(sprites, (x, y), area=(xs, ys, w, h))

    pygame.display.flip()
    clock.tick(30)
    
pygame.quit()

