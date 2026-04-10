from pymonad.tools import curry
from pymonad.maybe import Just
from pymonad.list import ListMonad

@curry(2)
def add(x, y):
    return x + y

def add10(x):
    return x.map(add(10))

print(add10(Just(25)))
print(add10(ListMonad(1,2,3)))