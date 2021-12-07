import numpy as np

with open('../Data/Day7.txt') as f:
    data = f.read().splitlines()

def part1(data):
    numbers = data[0].split(',')
    numbers = [int(x) for x in numbers]
    max_n = np.max(numbers)
    min_n = np.min(numbers)
    cost = 10000000000000
    for i in range(min_n, max_n):
        spot = i
        fuel_costs = [x - spot for x in numbers]
        fuel_costs = [np.abs(x) for x in fuel_costs]
        total = sum(fuel_costs)
        if total < cost:
            cost = total
    print(cost)

def part2(data):
    numbers = data[0].split(',')
    numbers = [int(x) for x in numbers]
    max_n = np.max(numbers)
    min_n = np.min(numbers)
    cost = 10000000000000
    for i in range(min_n, max_n):
        spot = i
        fuel_costs = [sum(range(np.abs(x-spot)+1)) for x in numbers]
        total = sum(fuel_costs)
        if total < cost:
            cost = total
    print(cost)

#part1(data)
part2(data)