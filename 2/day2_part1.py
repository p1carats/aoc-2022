file = open('2/data2.txt', 'r')
lines = file.readlines()

corresp = {'X':'A', 'Y':'B', 'Z':'C'}
table = {'A': 1, 'B': 2, 'C': 3}
outcome = []
score = 0

def game(adv, play):
    if play == 'A':
        # rock
        if adv == 'B':
            return False
        else:
            return True
    elif play == 'B':
        # paper
        if adv == 'C':
            return False
        else:
            return True
    elif play == 'C':
        if adv == 'A':
            return False
        else:
            return True

for line in lines:
    # reading
    for element in line:
        if not element.isspace():
            outcome.append(element)
    # convert second type
    outcome[1] = corresp[outcome[1]]
    # update total score
    if outcome[0] == outcome[1]:
        score += table[outcome[1]]
        score += 3
    else:
        score += table[outcome[1]]
        if game(outcome[0], outcome[1]) is True:
            score += 6
    # reset
    outcome = []

file.close()
print(score)