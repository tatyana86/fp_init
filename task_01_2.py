from pymonad.tools import curry

@curry(4)
def greeting(word, punctuation, end, name):
    return word + punctuation + " " + name + end


first_step = greeting
final = first_step("Hello")(",")("!")

print(final("Petya"))