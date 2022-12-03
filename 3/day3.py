import string

file = open('3/data3.txt', 'r')
lines = file.readlines()

i = 1
min = string.ascii_lowercase
maj = string.ascii_uppercase

values = {}
priorities = 0
badges = 0

for element in min:
    values.update({element : i})
    i += 1

for element in maj:
    values.update({element : i})
    i += 1

# part 1
for line in lines:
    half1 = set(line[:len(line)//2])
    half2 = set(line[len(line)//2:])
    tmp = list(half1.intersection(half2))
    priorities += int(values[tmp[0]])

# part 2
i = 1
for line in lines:
    if i%3 == 1:
        linem1 = set(line.strip())
    elif i%3 == 2:
        linem2 = set(line.strip())
    elif i%3 == 0:
        linem3 = set(line.strip())
        tmp = list(linem1.intersection(linem2.intersection(set(linem3))))
        badges += int(values[tmp[0]])
    i += 1

file.close()
print(priorities)
print(badges)