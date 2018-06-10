from zoo import hours as info
from collections import OrderedDict
from collections import defaultdict

#import zoo as menagerie

#menagerie.hours()

#hours()

info()

plain = {'a': 1, 'b': 2, 'c': 3}
print(plain)

fancy = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(fancy)

dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
print(dict_of_lists['a'])


