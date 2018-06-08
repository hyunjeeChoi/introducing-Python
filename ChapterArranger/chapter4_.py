quess_me = 7

if (quess_me < 7) :
    print('too low')
elif (quess_me == 7) :
    print('just right')
else :
    print('too high')

start = 1

while (start < quess_me) :
    print('too low')
    start = start + 1
    if (start == quess_me) :
        print ('found it!')
        break

list = [3, 2, 1, 0]

for word in list :
    print(word)

number_list = [number for number in range(1, 11) if number % 2 == 0]
print(number_list)

squares = {key: key*key for key in range(10)}
print(squares)

test_set = {number for number in range(1, 10) if number % 2 == 1}
print(test_set)

for thing in ('Got %s' % number for number in range(10)):
    print(thing)

def good():
    return (['Harry', 'Ron', 'Hermione'])

print(good())

def get_odds():
    for number in range(1, 10, 2):
        yield number

for count, number in enumerate(get_odds(), 1):
    if count == 3:
        print("third data", number)
        break

def test(func):
    def inner_func(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return inner_func()

@test
def call():
    print('call')

call()