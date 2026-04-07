from pymonad.tools import curry
from pymonad.reader import Compose

@curry(2)
def tag(tag_name, value):
    return f"<{tag_name}>{value}</{tag_name}>"

bold = Compose(tag("b"))
italic = Compose(tag("i"))

print(bold("string"))
print(italic("string"))