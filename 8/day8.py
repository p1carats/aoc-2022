import numpy as np

# generate matrix from file
matrix = []
with open('8/data8.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        matrix.append(list(line))
    matrix = np.array(matrix)

trees = 0
scenic_score = 0

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        height = int(matrix[i][j])
        current = []
        part1 = []
        part2 = 1
        # left
        current.append(matrix[i,:][j+1:].tolist())
        # right
        current.append(matrix[i,:][:j].tolist())
        current[1].reverse()
        # top
        current.append(matrix[:,j][i+1:].tolist())
        # bottom
        current.append(matrix[:,j][:i].tolist())
        current[3].reverse()
        # part 1 - check if tree is visible
        for k in range(0, len(current)):
            count = 0
            part1.append(int(max(current[k], default=-1)))
        if height > min(part1):
            trees += 1
        # part 2 - look for the best scenic place
        current = list(filter(None, current))
        for k in range(0, len(current)):
            for l in range(0, len(current[k])):
                if int(current[k][l]) >= height:
                    counter = l+1
                    break
                else:
                    counter = len(current[k])
            part2 *= counter
        if part2 >= scenic_score:
            scenic_score = part2

print(trees)
print(scenic_score)