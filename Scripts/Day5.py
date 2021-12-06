import numpy as np

with open('../Data/Day5.txt') as f:
    data = f.read().splitlines()

def part1(data):
    point_dict = {}
    for line in data:
        points = line.split(' -> ')
        first = points[0].split(',')
        second = points[1].split(',')
        first = [int(x) for x in first]
        second = [int(x) for x in second]


        if first[0] == second[0]:
            y_end = max(first[1], second[1])
            y_start = min(first[1], second[1])
            x = first[0]
            y_current = y_start

            while y_current <= y_end:
                value = point_dict.get((x, y_current),0)
                value += 1
                point_dict[(x,y_current)] = value
                y_current += 1

        elif first[1] == second[1]:
            x_end = max(first[0], second[0])
            x_start = min(first[0], second[0])
            y = first[1]
            x_current = x_start

            while x_current <= x_end:
                value = point_dict.get((x_current, y),0)
                value += 1
                point_dict[(x_current,y)] = value
                x_current += 1



    total = 0
    for key, value in point_dict.items():
        if value >= 2:
            total += 1

    print(total)



def part2(data):
    point_dict = {}
    for line in data:
        points = line.split(' -> ')
        first = points[0].split(',')
        second = points[1].split(',')
        first = [int(x) for x in first]
        second = [int(x) for x in second]

        first_dif = np.abs(first[0] - second[0])
        second_dif = np.abs(first[1] - second[1])


        if first[0] == second[0]:
            y_end = max(first[1], second[1])
            y_start = min(first[1], second[1])
            x = first[0]
            y_current = y_start

            while y_current <= y_end:
                value = point_dict.get((x, y_current),0)
                value += 1
                point_dict[(x,y_current)] = value
                y_current += 1

        elif first[1] == second[1]:
            x_end = max(first[0], second[0])
            x_start = min(first[0], second[0])
            y = first[1]
            x_current = x_start

            while x_current <= x_end:
                value = point_dict.get((x_current, y),0)
                value += 1
                point_dict[(x_current,y)] = value
                x_current += 1

        elif first_dif == second_dif:
            x_start = first[0]
            x_end = second[0]
            y_start = first[1]
            y_end = second[1]
            if y_start > y_end:
                y_mult = -1
            else:
                y_mult = 1

            if x_start > x_end:
                x_mult = -1
            else:
                x_mult = 1

            while x_start != x_end:
                value = point_dict.get((x_start, y_start), 0)
                value += 1
                point_dict[(x_start, y_start)] = value
                x_start += (1 * x_mult)
                y_start += (1 * y_mult)
            value = point_dict.get((x_start, y_start), 0)
            value += 1
            point_dict[(x_start, y_start)] = value



    total = 0
    for key, value in point_dict.items():
        if value >= 2:
            total += 1

    print(total)

#part1(data)
part2(data)