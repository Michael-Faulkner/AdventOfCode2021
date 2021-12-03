
with open('../Data/Day3.txt') as f:
    data = f.read().splitlines()


def part1(data):
    memory = {}
    size = len(data[1])
    for i in range(size):
        memory[i] = 0
    for line in data:
        for i in range(len(line)):
            if int(line[i]) == 1:
                memory[i] = memory[i] + 1

    need = len(data)//2
    gamma = ''
    epsilon = ''
    for i in range(len(data[1])):
        if memory[i] > need:
            gamma = gamma+'1'
            epsilon = epsilon+'0'
        else:
            gamma = gamma + '0'
            epsilon = epsilon + '1'
    return gamma, epsilon

def part2(data):

    possible = data.copy().copy()
    i = 0

    while len(possible) > 1:

        count_1 = 0
        count_0 = 0
        for line in possible:
            if line[i] == '1':
                count_1 += 1
            else:
                count_0 += 1

        if count_1 >= count_0:
            most = '1'
        else:
            most = '0'

        new_possible = []
        for line in possible:
            if line[i] == most:
                new_possible.append(line)
        possible = new_possible
        i += 1

    possible2 = data.copy().copy()
    i = 0

    while len(possible2) > 1:

        count_1 = 0
        count_0 = 0
        for line in possible2:
            if line[i] == '1':
                count_1 += 1
            else:
                count_0 += 1

        if count_1 < count_0:
            most = '1'
        else:
            most = '0'

        new_possible = []
        for line in possible2:
            if line[i] == most:
                new_possible.append(line)
        possible2 = new_possible
        i += 1

    return possible, possible2

# 5852595

# x, y  = part1(data)
# print(int(x,2)*int(y, 2))
x,y = part2(data)
print(int(x[0],2)*int(y[0], 2))