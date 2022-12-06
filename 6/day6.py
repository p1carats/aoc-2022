file = open('6/data6.txt', 'r')
line = list(file.readline())

def check(list, marker):
    for i in range(0, len(list)):
        tmp = [*set(list[i:i+marker])]
        if len(tmp) == marker:
            return i+marker

file.close()

# part 1
print(check(line, 4))
# part 2
print(check(line, 14))