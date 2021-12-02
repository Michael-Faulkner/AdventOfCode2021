with open('../Data/Day2.txt') as f:
    data = f.read().splitlines()

def part1(data):
    h = 0
    v = 0
    for line in data:
        parts = line.split(' ')
        direction = parts[0]
        num = int(parts[1])
        if direction == 'forward':
            h += num
        elif direction == 'down':
            v += num
        else:
            v -= num

    print(v*h)

def part2(data):
    h = 0
    v = 0
    a = 0
    for line in data:
        parts = line.split(' ')
        direction = parts[0]
        num = int(parts[1])
        if direction == 'forward':
            h += num
            v += (a * num)
        elif direction == 'down':
            a += num
        else:
            a -= num

    print(v*h)



#part1(data)
part2(data)
