file = open('1/data1.txt', 'r')
lines = file.readlines()

elf = 1
calories = 0

winner = [0, 0, 0]
score = [0, 0, 0]

for line in lines:
    if not line.strip():
        if calories >= score[2]:
            score[2] = calories
            winner[2] = elf
        score.sort(reverse=True)
        winner.sort(reverse=True)
        calories = 0
        elf += 1
    else:
        calories += int(line.strip())
    # print(line.strip())

file.close()
print(winner[0], score[0])
print(winner, score[0]+score[1]+score[2])