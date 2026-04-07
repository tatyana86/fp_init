from pymonad.tools import curry
from pymonad.reader import Compose

@curry(3)
def tag(tag_name, attr, value):
    attrs = ""
    for key in attr:
        attrs = attrs + " " + key + '="' + attr[key] + '"'
    result = "<" + tag_name + attrs + ">" + value + "</" + tag_name + ">"
    return result

bold = Compose(tag("b")({}))
italic = Compose(tag("i")({}))

print(bold("string"))
print(italic("string"))
print(tag('li', {'class': 'list-group'}, 'item 23'))