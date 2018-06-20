test1 = 'THIS IS A TEST OF THE EMERGENCY TEXT SYSTEM'
print(len(test1))

outfile = open('test.txt', 'wt')
outfile.write(test1)
outfile.close()

with open('test.txt','rt') as infile:
    test2 = infile.read()

    len(test2)
    print(len(test2))


print(test1 == test2)

