year_lists = [1980, 1981, 1982, 1983, 1984]
print(year_lists[2])

sorted_year_lists = sorted(year_lists)
print(sorted_year_lists[0])

things = ['mozzarella', 'cinderella', 'salmonella']
things[1] = 'Cinderella'

print(things)

things[0] = 'MOZZARELLA'

print(things)

things.remove('salmonella')

print(things)

surprise = ['Groucho', 'Chico', 'Harpo']

surprise[2]= 'harpo'

print(surprise)

e2f = {'dog' : 'chien', 'cat' : 'chat', 'walrus' : 'morse'}

print(e2f)

print(e2f.get('walrus'))

new_list = list(e2f.items())

print(new_list)

print(e2f.keys())

