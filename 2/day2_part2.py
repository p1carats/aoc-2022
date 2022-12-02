file = open('2/data2.txt', 'r')
lines = file.readlines()

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
    # select how the round needs to end
    if outcome[1] == 'X':
        # lose
        if outcome[0] == 'A':
            outcome[1] = 'C'
        elif outcome[0] == 'B':
            outcome[1] = 'A'
        else:
            outcome[1] = 'B'
    elif outcome[1] == 'Y':
        # draw
        corresp = {'X':'A', 'Y':'B', 'Z':'C'}
        outcome[1] = outcome[0]
    elif outcome[1] == 'Z':
        # win
        if outcome[0] == 'A':
            outcome[1] = 'B'
        elif outcome[0] == 'B':
            outcome[1] = 'C'
        else:
            outcome[1] = 'A'
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