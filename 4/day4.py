file = open('4/data4.txt', 'r')
lines = file.readlines()

res1 = 0
res2 = 0

for line in lines:
    tmp = line.strip().split(',')
    # section 1
    section1 = tmp[0].strip().split('-')
    section1 = range(int(section1[0]), int(section1[1])+1)
    section1 = set(section1)
    # section 2
    section2 = tmp[1].strip().split('-')
    section2 = range(int(section2[0]), int(section2[1])+1)
    section2 = set(section2)
    # check if one range fully contain the other
    if section1.issubset(section2) or section2.issubset(section1):
        res1 += 1
    # check if ranges overlap
    if len(section1.intersection(section2)) > 0:
        res2 += 1

file.close()
print(res1)
print(res2)