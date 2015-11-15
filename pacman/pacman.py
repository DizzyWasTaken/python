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

    def __init__(self, arena:Arena, x:int, y:int):
        self._arena = arena
        self._x     = x
        self._y     = y
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
        pass

    def rect(self):
        return self._x, self._y, self.W, self.H
    
    def symbol(self):#TO-DO: Make 4 different sprites
        return 0, 64


class PacMan(Actor):  # ...
    W, H 		= 16, 16
    dx, dy      = 0, 0
    SPEED       = 2
    symbolPos   = 0

    def __init__(self, arena:Arena, x:int, y:int):
        self._arena     = arena
        self._x         = x
        self._y         = y
        self._symbolX   = 0
        arena.add(self)

    def move(self):
        if not going_to_wall(self._arena, self, self.dx, self.dy):
            self._x += self.dx
            self._y += self.dy
            if self.dx or self.dy != 0 and self.dx % 4 == 0 or self.dy % 4 == 0:
                if self.symbolPos > 0:
                    self.symbolPos = 0
                else:
                    self.symbolPos += 1
            
        self._symbolX = self.symbolPos * self.W

    def moveUp(self):
        self.dx , self.dy = 0, -self.SPEED
    
    def moveDown(self):
        self.dx , self.dy = 0, +self.SPEED
    
    def moveLeft(self):
        self.dx , self.dy = -self.SPEED, 0
    
    def moveRight(self):
        self.dx , self.dy = +self.SPEED, 0

    def collide(self, other):
        pass

    def rect(self):
        return self._x, self._y, self.W, self.H

    def symbol(self):
        return self._symbolX, 0

