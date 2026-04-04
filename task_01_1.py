from pymonad.tools import curry

@curry(2)
def concat_strings(a, b):
    return a + b

hello = concat_strings("Hello, ")

print(hello("Tanya"))