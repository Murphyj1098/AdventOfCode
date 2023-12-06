#!/usr/bin/env python3
'''
Advent of Code: Day 1
'''

import regex as re

def strToDigit(stringIn: str) -> str:
    LUT = {
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9'
    }
    try:
        return LUT[stringIn]
    except KeyError:
        return None


def part1() -> int:
    runningTotal = 0
    with open('input.txt', 'r') as f:
        for line in f:
            pattern = re.compile("[0-9]")
            lineList = pattern.findall(line, overlapped=True)
            runningTotal += int((lineList[0]+lineList[-1]))
    return runningTotal


def part2() -> int:
    runningTotal = 0
    indexer = 0
    with open('input.txt', 'r') as f:
        for line in f:
            pattern = re.compile("one|two|three|four|five|six|seven|eight|nine|[0-9]")
            lineList = pattern.findall(line, overlapped=True)
            
            firstDigit = lineList[0] if (strToDigit(lineList[0]) is None) else strToDigit(lineList[0])
            lastDigit = lineList[-1] if (strToDigit(lineList[-1]) is None) else strToDigit(lineList[-1])

            runningTotal += int((firstDigit + lastDigit))

    return runningTotal


if __name__ == '__main__':
    print("Part 1 Answer: {}".format(part1()))
    print("Part 2 Answer: {}".format(part2()))