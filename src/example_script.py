import numpy

num = 10000

print('This script draws pairs of random integers between 0 and', num, 'until they are equal', '\n')
n1 = -1
n2 = -2
i = 0

while n1 != n2:
    n1 = numpy.random.randint(num)
    n2 = numpy.random.randint(num)
    i = i + 1
    if i % 1000 == 0:
        print(i, 'tries, still going')
print('done after' ,i, 'tries \n')
