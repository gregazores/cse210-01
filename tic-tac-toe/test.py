test = ["x", "x", "x", "d", "e", "f", "g", "h", "i"]

newlist = [x for x in test if type(x) == int]

print(newlist)









"""

test = ["x", "x", "x", "d", "e", "f", "g", "h", "i"]

newlist = [x for x in test if type(x) != int]

if newlist == []:
    print('TRUE')

else:
    print('FALSE')


test = ["a", "b", "c", "o", "o", "o", "g", "h", "i"]

x1 = f'{test[0]}{test[1]}{test[2]}'
x2 = f'{test[3]}{test[4]}{test[5]}'
x3 = f'{test[6]}{test[7]}{test[8]}'
x4 = f'{test[0]}{test[3]}{test[6]}'
x5 = f'{test[1]}{test[4]}{test[7]}'
x6 = f'{test[2]}{test[5]}{test[8]}'
x7 = f'{test[0]}{test[4]}{test[8]}'
x8 = f'{test[2]}{test[4]}{test[6]}'

o1 = f'{test[0]}{test[1]}{test[2]}'
o2 = f'{test[3]}{test[4]}{test[5]}'
o3 = f'{test[6]}{test[7]}{test[8]}'
o4 = f'{test[0]}{test[3]}{test[6]}'
o5 = f'{test[1]}{test[4]}{test[7]}'
o6 = f'{test[2]}{test[5]}{test[8]}'
o7 = f'{test[0]}{test[4]}{test[8]}'
o8 = f'{test[2]}{test[4]}{test[6]}'

if x1 == "xxx" or x2 == "xxx" or x3 == "xxx" or x4 == "xxx" or x5 == "xxx" or x6 == "xxx" or x7 == "xxx" or x8 == "xxx":
    print('Winner X')

if o1 == "ooo" or o2 == "ooo" or o3 == "ooo" or o4 == "ooo" or o5 == "ooo" or o6 == "ooo" or o7 == "ooo" or o8 == "ooo":
    print('Winner o')


#test = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
test = "abcdefghi"
test2 = []
for x in range(0,3):
    test2.append("|".join(test[3*x:(3*x + 3)]))

print(f"\n-+-+-\n".join(te

test = "abcdefghi"
test2 = []
for x in range(0,3):
    "|".join(test2.append(test[3*x:(3*x + 3)]))

print(f"\n-+-+-\n".join(test2))

from cgitb import text
from genericpath import samefile


test = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
i = 0

test2 = []
for x in range(0, 9, 3):
    sample = ""
    for y in range(x, int((3*x + 3))):
        sample += f'{y}'
    print(sample)





from cgitb import text



test = [1,2,3,4,5,6,7,8,9]
i = 0

test2 = []
while i < len(test)/3:
    j = 0
    sample = ""
    while 3*i < j < (3*i + 3):
        sample += f'{test[j]}'
        j += 1
    test2.append(sample)
    i += 1


print(test2)

"""

"""


word = ["|".join("123"), "|".join("456"), "|".join("789")]
def print_grid():
    row_format = []
    line_breaker = f"\n-+-+-\n" 
    print(line_breaker.join(word))

word = [1,2,3,]
def print_grid():
    sample = ""
    for x in grid_array:
        sample =  sample + f'{x}'       
    print("|".join(sample))


"""
