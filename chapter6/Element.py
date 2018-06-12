class Thing:
    pass

print(Thing)

class Things2:
    letters = 'abc'

print(Things2.letters)

class Things3:
    def __init__(self):
        self.letters = 'xyz'

#print(Things3.letters)

showLetter = Things3()
print(showLetter.letters)


class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


hydrogen = Element('Hydrogen', 'H', 1)

print(hydrogen.name)

el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}

#hydrogen2 = Element(el_dict['name', el_dict['symbol'], el_dict['number'])

#print(hydrogen2.name)
