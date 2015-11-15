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
    W, H = 16, 16
    dx, dy = 1, 0

    def __init__(self, arena:Arena, x:int, y:int):
        self._arena = arena
        self._x     = x
        self._y     = y
        arena.add(self)

    def move(self):
        if going_to_wall(self._arena, self, self.dx, self.dy):
            self.dx = 0
            self.dy = 1
            
        self._x += self.dx
        self._y += self.dy

    def collide(self, other):
        pass

    def rect(self):
        return self._x, self._y, self.W, self.H
    
    def symbol(self):#TO-DO: Make 4 different sprites
        return 0, 64


class PacMan(Actor):  # ...
    W, H = 16, 16
    SPEED = 1

    def __init__(self, arena:Arena, x:int, y:int):
        self._arena = arena
        self._x     = x
        self._y     = y
        self._dx    = 0
        self._dy    = 0
        arena.add(self)

    def move(self):
        if going_to_wall()

    def moveUp(self):
        self._dx , self._dy = 0, +self.SPEED
    
    def moveDown(self):
        self._dx , self._dy = 0, -self.SPEED
    
    def moveLeft(self):
        self._dx , self._dy = -self.SPEED, 0
    
    def moveRight(self):
        self._dx , self._dy = +self.SPEED, 0

    def collide(self, other):
        pass

    def rect(self):
        return self._x, self._y, self.W, self.H

    def symbol(self):
        return 0, 0

