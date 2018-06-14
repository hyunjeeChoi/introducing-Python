import unicodedata
unicode_mystery = '\U0001f4a9'

print(unicode_mystery)
#unicodedata.name(unicode_mystery)

pop_bytes = unicode_mystery.encode('utf-8')
print(pop_bytes)

pop_string = pop_bytes.decode('utf-8')
print(pop_string)

if pop_string == unicode_mystery:
    print(True)

mammoth = '''
we have seen thee, queen of cheese, Lyving quetly at your ease, It's too long. cat call check cast crush finish
'''


import re
pat = r'\bc\w*'
print(re.findall(pat, mammoth))

pat = r'\bc\w{3}\b'
print(re.findall(pat, mammoth))

#def unicode_mystery(value):
 #   import unicodedata

  #  value = unicodedata.lookup('\U0001f4a9')


#print(unicode_mystery('\U0001f4a9'))