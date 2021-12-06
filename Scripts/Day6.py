import numpy as np
import pandas as pd
from collections import defaultdict

with open('../Data/Day6.txt') as f:
    data = f.read().splitlines()


def part1(data):
    data = data[0].split(',')
    fish = [int(x) for x in data]
    fish_track = defaultdict(int)

    for x in fish:
        fish_track[x] += 1

    for i in range(80):
        new_fish = defaultdict(int)
        for key, value in fish_track.items():
            if key == 0:
                new_fish[8] += value
                new_fish[6] += value
            else:
                new_fish[key-1] += value
        fish_track = new_fish


    print(sum(fish_track.values()))

def part2(data):
    data = data[0].split(',')
    fish = [int(x) for x in data]
    fish_track = defaultdict(int)

    for x in fish:
        fish_track[x] += 1

    for i in range(256):
        new_fish = defaultdict(int)
        for key, value in fish_track.items():
            if key == 0:
                new_fish[8] += value
                new_fish[6] += value
            else:
                new_fish[key-1] += value
        fish_track = new_fish


    print(sum(fish_track.values()))

part2(data)
#1639854996917