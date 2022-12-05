from itertools import zip_longest
import string

file = open('5/data5.txt', 'r')
lines = file.readlines()

# we can't use sets as they don't preserve lists order
def intersection(list1, list2):
    res = [value for value in list1 if value in list2]
    res.reverse()
    return res

# crates layout parsing
def crates(input):
    crates = []
    transposed = list(zip_longest(*input))
    transposed = [list(sublist) for sublist in transposed]
    for i in range(len(transposed)):
        if len(intersection(transposed[i], list(string.ascii_uppercase))) > 0:
            crates.append(intersection(transposed[i], list(string.ascii_uppercase)))
    return crates

# part 1
def cratemover9000(list, quantity, source, dest):
    for i in range(1, quantity+1):
        tmp = list[source].pop()
        list[dest].append(tmp)
    return list

# part 2
def cratemover9001(list, quantity, source, dest):
    tmp = list[source][-quantity:]
    for i in range(1, quantity+1):
        list[source].pop()
    list[dest].extend(tmp)
    return list

instructions = lines[lines.index('\n')+1:]
crates1 = crates(lines[:lines.index('\n')])
crates2 = crates(lines[:lines.index('\n')])

for elem in instructions:
    elem = elem.strip().replace('move', '')
    elem = ''.join(elem.split())
    elem = elem.split('from')
    elem.extend(elem[1].split('to'))
    del elem[1]
    crates1 = cratemover9000(crates1, int(elem[0]), int(elem[1])-1, int(elem[2])-1)
    crates2 = cratemover9001(crates2, int(elem[0]), int(elem[1])-1, int(elem[2])-1)

file.close()

# print result
part1, part2 = '', ''

for elem in crates1:
    part1 += str(next(reversed(elem)))
print(part1)

for elem in crates2:
    part2 += str(next(reversed(elem)))
print(part2)