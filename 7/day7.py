file = open('7/data7.txt', 'r')
lines = file.readlines()

filesystem = {}

currentpos = []
for line in lines:
    line = line.strip()
    if line.startswith('$'):
        line = line.strip('$ ')
        if line.startswith('cd'):
            directory = line.strip('cd ')
            if directory != '..':
                currentpos.append(directory)
            else:
                currentpos.pop()
            filesystem.setdefault('/'.join(currentpos).replace('//', '/'), 0)
        elif line.startswith(' '):
            continue
    else:
        line = line.split(' ')
        if line[0].isnumeric():
            filesystem['/'.join(currentpos).replace('//', '/')] += int(line[0])

# part 1
part1 = 0
for elem1 in filesystem:
    for elem2 in filesystem:
        if elem1 != elem2 and elem2.startswith(elem1):
            filesystem[elem1] += filesystem[elem2]
    if filesystem[elem1] <= 100000:
        part1 += filesystem[elem1]
print(part1)

# part 2
part2 = 70000000
for item1 in filesystem:
    if filesystem[item1] > 30000000-(70000000-filesystem['/']):
        part2 = min(part2, filesystem[item1])
print(part2)