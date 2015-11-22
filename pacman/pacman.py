'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from random import choice
from arena import *

# The following two functions may me adapted to be part of a subclass
# of Arena, specialized for the Pac-Man game

def rect_in_wall(arena: Arena, rect: (int, int, int, int)) -> bool:
    for other in arena.actors():
        if isinstance(other, Wall):
            x1, y1, w1, h1 = rect
            x2, y2, w2, h2 = other.rect()
            if (y2 < y1 + h1 and y1 < y2 + h2 and
                x2 < x1 + w1 and x1 < x2 + w2):
                return True
        else:
            return False  # walls must be the first actors in the list!


def going_to_wall(arena: Arena, actor: Actor, dx: int, dy: int) -> bool:
    x, y, w, h = actor.rect()
    return rect_in_wall(arena, (x + dx, y + dy, w, h))
#dice se sbattero in un muro la prossima volta

# Size and position hints for Pac-Man characters
# Everything needs yet to be fixed!

class Wall(Actor):  # ...

    def __init__(self, arena:Arena, x:int, y:int, w:int, h:int):
        self._arena = arena
        self._x     = x
        self._y     = y
        self._w     = w
        self._h     = h
        arena.add(self)

    def move(self):
        pass

    def collide(self, other):
        pass

    def rect(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        pass


class Cookie(Actor):  # ...
    W, H = 4, 4

    def __init__(self, arena:Arena, x:int, y:int):
        self._arena = arena
        self._x     = x
        self._y     = y
        arena.add(self)

    def move(self):
        pass

    def collide(self, other):
        pass

    def rect(self):
        return self._x, self._y, self.W, self.H
        
    def symbol(self):
        return 166, 54


class Power(Cookie):  # ...
    W, H = 8, 8

    def __init__(self, arena:Arena, x:int, y:int):
        super(Power, self).__init__(arena, x, y)

    def symbol(self):
        return 180, 52

class Ghost(Actor):  # ...
    W, H    = 16, 16
    dx, dy  = 2, 0
    SPEED	= 2

    def __init__(self, arena:Arena, x:int, y:int, symbol:tuple):
        self._arena     = arena
        self._x         = x
        self._y         = y
        self._symbol    = symbol
        arena.add(self)
                    
    def move(self):
        if going_to_wall(self._arena, self, self.dx, self.dy):
            self.dx = choice([-self.SPEED, 0, self.SPEED])
            self.dy = choice([-self.SPEED, 0, self.SPEED])
            while going_to_wall(self._arena, self, self.dx, self.dy) or self.dx == self.dy == 0:
                self.dx = choice([-self.SPEED, 0, self.SPEED])
                self.dy = choice([-self.SPEED, 0, self.SPEED])

        self._x += self.dx
        self._y += self.dy

    def collide(self, other):
        if isinstance(other, PacMan):
            self._arena.remove(other)

    def rect(self):
        return self._x, self._y, self.W, self.H
    
    def symbol(self):
        return self._symbol


class PacMan(Actor):  # ...
    W, H 		= 16, 16
    dx, dy      = 0, 0
    SPEED       = 2
    symbolPos   = 0
    userD       = 0
    mvngAlngY   = False
    STEPS       = 3 #number of cycles to wait in order to change mouth position

    def __init__(self, arena:Arena, x:int, y:int):
        self._arena     = arena
        self._x         = x
        self._y         = y
        self._symbolX   = False
        self._symbolY   = 0 #0 = dx, 1 = sx, 2 = up, 3 = down
        arena.add(self)

    def move(self):
        if self.userD != 0:
            if self.dx == 0 and self.dy == 0:
                self.userD = 0
            if self.mvngAlngY:
                if not going_to_wall(self._arena, self, 0, self.dy + self.userD):
                    self.dx = 0
                    self.dy = self.userD
                    if self.dy < 0:
                        self._symbolY = 2
                    else:
                        self._symbolY = 3
                    self.userD = 0
            else:
                if not going_to_wall(self._arena, self, self.dx + self.userD, 0):
                    self.dx = self.userD
                    self.dy = 0
                    if self.dx < 0:
                        self._symbolY = 1
                    else:
                        self._symbolY = 0
                    self.userD = 0
                    
        if not going_to_wall(self._arena, self, self.dx, self.dy):
            if self.dx or self.dy != 0:
                self._x += self.dx
                self._y += self.dy
                
                if self._x > self._arena.size()[0]:#se passo per il tunnel
                    self._x = - self.W
                elif self._x < - self.W :
                    self._x = self._arena.size()[0]
                    
                self.symbolPos += 1
                if self.symbolPos % self.STEPS == 0:
                    self._symbolX = not self._symbolX
                    if self.symbolPos > self.STEPS * 2:
                        self.symbolPos = 0
        else:
            self.dx, self.dy = 0, 0
        #self._symbolX = self.symbolPos // self.STEPS * self.W

    def moveUp(self):
        if going_to_wall(self._arena, self, 0, self.dy - self.SPEED) and (self.dx or self.dy != 0):
            self.userD = -self.SPEED
            self.mvngAlngY = True
        else:
            self.dx , self.dy = 0, -self.SPEED
            self._symbolY = 2
    
    def moveDown(self):
        if going_to_wall(self._arena, self, 0, self.dy + self.SPEED) and (self.dx or self.dy != 0):
            self.userD = +self.SPEED
            self.mvngAlngY = True
        else:
            self.dx , self.dy = 0, +self.SPEED
            self._symbolY = 3
    
    def moveLeft(self):
        if going_to_wall(self._arena, self, self.dx - self.SPEED, 0) and (self.dx or self.dy != 0):
            self.userD = -self.SPEED
            self.mvngAlngY = False
        else:
            self.dx , self.dy = -self.SPEED, 0
            self._symbolY = 1
    
    def moveRight(self):
        if going_to_wall(self._arena, self, self.dx + self.SPEED, 0) and (self.dx or self.dy != 0):
            self.userD = +self.SPEED
            self.mvngAlngY = False
        else:
            self.dx , self.dy = +self.SPEED, 0
            self._symbolY = 0

    def collide(self, other):
        if isinstance(other, Cookie):
            self._arena.remove(other)

    def rect(self):
        return self._x, self._y, self.W, self.H

    def symbol(self):
        #return self._symbolX, self._symbolY * self.H
        return self.W if self._symbolX else 0, self._symbolY * self.H

