# clock count and register
cycle = 0
X = 1

# part 1
signal_strengh = 0

# part 2
CRT = [str(''.ljust(40, '.'))]*6

def draw(CRT, cycle, X):
    cursor = (cycle%40)-1
    sprite = {X-1, X, X+1}
    if cursor in sprite:
        tmp = list(CRT[cycle//40])
        tmp[cursor] = '#'
        CRT[cycle//40] = ''.join(tmp)
    return CRT

# fetch program from txt
program = []
with open('data/input10.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        if line == 'noop':
            tmp = [line]
            program.append(tmp)
        else:
            tmp = line.split(' ')
            program.append(tmp)

for inst in program:
    if inst[0] == 'noop':
        cycle += 1
        CRT = draw(CRT, cycle, X)
        if cycle == 20 or (cycle-20)%40 == 0:
            signal_strengh += (X*cycle)
    elif inst[0] == 'addx':
        V = int(inst[1])
        for i in range(0, 2):
            cycle += 1
            CRT = draw(CRT, cycle, X)
            if cycle == 20 or (cycle-20)%40 == 0:
                signal_strengh += (X*cycle)
            if i == 1:
                X += V

print(signal_strengh)
for elem in CRT:
    print(*elem)