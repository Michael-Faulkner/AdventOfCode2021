with open('Data/Day1.txt') as f:
    data = f.read().splitlines()

data = [int(x) for x in data]

def part1(data):
    count = 0
    i = 0

    while i < len(data) - 1:
        i += 1
        second_point = data[i]
        first_point = data[i-1]
        if second_point > first_point:
            count += 1

    print(count)

def part2(data):
    first_index = 0
    second_index = 1
    count = 0
    while second_index+2 < len(data):
        first_window = data[first_index:first_index+3]
        second_window = data[second_index:second_index+3]
        if sum(second_window) > sum(first_window):
            count += 1
        first_index += 1
        second_index += 1

    print(count)


#part1(data)
part2(data)